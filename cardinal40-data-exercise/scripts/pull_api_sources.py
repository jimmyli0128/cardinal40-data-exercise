"""
pull_api_sources.py
-------------------
Pulls the three fully-open, machine-readable sources for the Cardinal40 exhibits:
  (5) World Bank WDI   -> China/US/World household consumption % of GDP
  (6) UN WPP 2024      -> China/India working-age population (15-64), medium variant
  (7) IMF COFER        -> currency composition of FX reserves, latest

Each function writes a full-series CSV to ../data/ and prints CHECKPOINT values that
should match data/SOURCES.md and the *_checkpoints.csv files.

NOTE: endpoints were verified to exist as of 2026-06-23 but were NOT executed in the
build environment (no network egress). Run locally. Where an API path may have shifted
(esp. IMF, which revamped its portal in 2025), a manual CSV-export fallback is noted.

Requires: requests, pandas   ->   pip install requests pandas
"""

import json
import requests
import pandas as pd

OUT = "../data"
TIMEOUT = 60


# ---------------------------------------------------------------------------
# (5) World Bank WDI  -- household consumption % of GDP  (indicator NE.CON.PRVT.ZS)
# ---------------------------------------------------------------------------
def pull_worldbank():
    url = ("https://api.worldbank.org/v2/country/CHN;USA;WLD/"
           "indicator/NE.CON.PRVT.ZS?format=json&per_page=500")
    r = requests.get(url, timeout=TIMEOUT)
    r.raise_for_status()
    payload = r.json()[1]  # [0] is metadata, [1] is the data array
    rows = [
        {"entity": d["country"]["value"], "year": int(d["date"]), "value": d["value"]}
        for d in payload if d["value"] is not None
    ]
    df = pd.DataFrame(rows).sort_values(["entity", "year"])
    df.to_csv(f"{OUT}/worldbank_household_consumption_full.csv", index=False)

    chk = df[(df.entity == "China") & (df.year == 2023)]
    print("[World Bank] CHECKPOINT  China household consumption %GDP 2023 = "
          f"{chk['value'].iat[0]:.2f}   (expected ~39.57)")
    return df


# ---------------------------------------------------------------------------
# (6) UN WPP 2024  -- working-age population 15-64, medium variant
# ---------------------------------------------------------------------------
def pull_unwpp():
    # UN Data Portal. Location M49 codes: China=156, India=356.
    # Indicator 46 = "Population by 1-year age groups and sex" (commonly used);
    # confirm against https://population.un.org/dataportalapi/api/v1/indicators
    # We request both sexes (sex id 3), ages 15-64, years 2024 & 2050, medium variant.
    base = "https://population.un.org/dataportalapi/api/v1"
    indicator = 46
    locations = "156,356"
    url = (f"{base}/data/indicators/{indicator}/locations/{locations}"
           f"/start/2024/end/2050?format=json")
    r = requests.get(url, timeout=TIMEOUT)
    r.raise_for_status()
    data = r.json().get("data", [])

    df = pd.DataFrame(data)
    # Filter: both sexes, medium variant, working age 15-64, target years.
    if not df.empty:
        df = df[(df["sex"] == "Both sexes")
                & (df["variant"] == "Median")  # 'Median'/'Medium' per portal labels
                & (df["ageStart"] >= 15) & (df["ageStart"] <= 64)
                & (df["timeLabel"].isin(["2024", "2050"]))]
        wa = (df.groupby(["location", "timeLabel"])["value"].sum()
                .div(1_000_000).round(0).reset_index()
                .rename(columns={"value": "working_age_15_64_millions"}))
        wa.to_csv(f"{OUT}/unwpp_working_age_full.csv", index=False)
        print("[UN WPP] CHECKPOINT  working-age 15-64 (millions):")
        print(wa.to_string(index=False),
              "\n   (expected China 2024~984 / 2050~745; India 2024~990 / 2050~1130)")
        return wa
    print("[UN WPP] No data returned -- confirm indicator id / labels against "
          "the /indicators endpoint, or use the bulk CSV download center.")
    return df


# ---------------------------------------------------------------------------
# (7) IMF COFER -- currency composition of FX reserves
# ---------------------------------------------------------------------------
def pull_imf_cofer():
    # IMF revamped its data portal in 2025 (data.imf.org, dataset IMF.STA:COFER).
    # Legacy SDMX-JSON endpoint below often still resolves; if it 404s, export CSV
    # manually from the COFER dashboard: https://data.imf.org/en/dashboards/cofer%20dashboard
    url = ("https://dataservices.imf.org/REST/SDMX_JSON.svc/CompactData/"
           "COFER/Q.W00.RAXG_USD")  # quarterly, world, allocated reserves by currency
    try:
        r = requests.get(url, timeout=TIMEOUT)
        r.raise_for_status()
        raw = r.json()
        with open(f"{OUT}/imf_cofer_raw.json", "w") as f:
            json.dump(raw, f)
        print("[IMF COFER] Raw SDMX pulled -> data/imf_cofer_raw.json "
              "(parse series; CHECKPOINT USD 2025Q4 = 56.77%, CNY = 1.95%)")
    except Exception as e:
        print(f"[IMF COFER] API path needs confirming ({e}). "
              "Fallback: export CSV from the COFER dashboard. "
              "CHECKPOINT USD 2025Q4 = 56.77%, CNY = 1.95%.")


if __name__ == "__main__":
    for fn in (pull_worldbank, pull_unwpp, pull_imf_cofer):
        try:
            fn()
        except Exception as e:
            print(f"[{fn.__name__}] failed: {e}")
