"""
EXHIBIT 2 -- "While China Leads in Inputs, America is Better at Building Companies"
Diverging 'tug-of-war' across the founder journey; each bar = how far ahead the leader is,
normalized for population / economy size. Ratios from data/q2_calculations.csv.
Run:  python plot_exhibit2.py   ->   figures/exhibit2.png
"""
import re, pandas as pd, matplotlib.pyplot as plt
from pathlib import Path
from matplotlib.patches import FancyBboxPatch, Polygon, Circle, Rectangle

NAVY, RED, INK, GREY = "#1b3b6b", "#cb2128", "#16181d", "#8a8d91"
PINK, BLUE = "#fdeef0", "#eef3fa"
plt.rcParams.update({"font.family": "DejaVu Sans", "axes.edgecolor": "#cccccc",
                     "figure.dpi": 150, "savefig.dpi": 150})

# Each ratio + leader is read from data/q2_calculations.csv (formula + source live there).
HERE = Path(__file__).resolve().parent; DATA = HERE/"data"; FIGS = HERE/"figures"
_calc = pd.read_csv(DATA/"q2_calculations.csv").set_index("stage")
ratio = lambda k: float(re.search(r"([\d.]+)x\s*$", _calc.loc[k, "result"]).group(1))
side  = lambda k: "cn" if "China" in str(_calc.loc[k, "leader"]) else "us"
# (y, display title, display subnote, stage key in the CSV)
_defs = [
    (10.2, "Engineers & scientists",           "PhDs/yr: 77k vs 40k",        "Staff"),
    (9.2,  "Investment",                        "40% vs 21% of GDP",          "Capital"),
    (8.2,  "Manufacturing",                     "29% vs 16% of world",        "Manufacturing"),
    (6.0,  "Startup funding",                   "0.72% vs 0.19% of GDP",      "Fund"),
    (5.0,  "Growing into billion-dollar firms", "2.2 vs 0.24 per million",    "Scale"),
    (4.0,  "Ways to cash out",                  "markets 190% vs 65% of GDP", "Exit"),
    (3.0,  "Second chances after failure",      "81\u00a2 vs 37\u00a2 recovered",  "Recycle"),
    (2.0,  "Company profits",                   "18% vs 8% return on equity", "Durability"),
]
rows = [(y, t, sub, side(k), ratio(k)) for (y, t, sub, k) in _defs]
LX = -9.6
FW, FH = 10.5, 15.0
fig = plt.figure(figsize=(FW, FH)); fig.patch.set_facecolor("white")
ax = fig.add_axes([0.04, 0.155, 0.93, 0.70]); ax.set_xlim(-10, 10.6); ax.set_ylim(1.1, 11.9)

# bands
ax.axhspan(7.7, 10.8, color=PINK, zorder=0)
ax.axhspan(1.5, 6.6, color=BLUE, zorder=0)
# parity line
ax.axvline(0, color="#333", lw=1.5, zorder=4)
ax.text(0, 11.35, "Parity", ha="center", fontsize=12, color="#444", fontweight="bold")

for y, title, sub, side, val in rows:
    v = -val if side == "cn" else val
    c = RED if side == "cn" else NAVY
    ax.barh(y, v, height=0.52, color=c, zorder=3)
    if side == "cn":
        ax.text(v-0.3, y, f"{val}\u00d7", ha="right", va="center", fontsize=18, fontweight="bold", color=c, zorder=5)
    else:
        ax.text(v+0.3, y, f"{val}\u00d7", ha="left", va="center", fontsize=18, fontweight="bold", color=c, zorder=5)
    ax.text(LX, y+0.22, title, ha="left", va="center", fontsize=13, fontweight="bold", color=INK, zorder=5)
    ax.text(LX, y-0.2, sub, ha="left", va="center", fontsize=10, color="#666", zorder=5)

# group headers
ax.text(LX+1.7, 11.0, "CHINA LEADS THE INPUTS", fontsize=15, fontweight="bold", color=RED, zorder=5)
ax.text(LX, 10.62, "the raw ingredients: people, money, factories", fontsize=10.5, style="italic", color="#777", zorder=5)
ax.text(LX+1.7, 6.8,  "AMERICA BUILDS THE COMPANIES", fontsize=15, fontweight="bold", color=NAVY, zorder=5)
ax.text(LX, 6.42, "turning those inputs into funded, fast-growing, profitable firms", fontsize=10.5, style="italic", color="#777", zorder=5)

# annotations
ax.text(0.6, 9.4, "\u2192 but the US still attracts\n    the best: most top US startups\n    were founded by immigrants",
        fontsize=11, color=RED, style="italic", va="center", zorder=5)
ax.text(9.4, 4.45, "and China has ~4\u00d7\nthe people", fontsize=10.5, color=NAVY, style="italic", ha="right", va="center", zorder=5)
ax.text(3.6, 2.0, "\u2190 driven by a home market\n   1.7\u00d7 larger (consumer\n   spending: 68% vs 40% of GDP)",
        fontsize=10.5, color=NAVY, style="italic", va="center", zorder=5)

# x-axis ticks + direction
ax.set_yticks([])
ax.set_xticks([-9,-6,-3,0,3,6,9])
ax.set_xticklabels(["9\u00d7","6\u00d7","3\u00d7","Parity","3\u00d7","6\u00d7","9\u00d7"], fontsize=11)
ax.tick_params(length=0)
for s in ["top","right","left"]: ax.spines[s].set_visible(False)
ax.spines["bottom"].set_color("#cccccc")
ax.text(-5.5, 0.55, "\u25c0  China ahead", transform=ax.transData, fontsize=12.5, fontweight="bold", color=RED, ha="center")
ax.text(5.5, 0.55, "America ahead  \u25b6", transform=ax.transData, fontsize=12.5, fontweight="bold", color=NAVY, ha="center")
ax.set_clip_on(False)
for t in ax.texts: t.set_clip_on(False)

# ---- icons (drawn, square inset axes) ----
def sq_axes(x, y, w=0.05):
    a = fig.add_axes([x, y, w, w*FW/FH]); a.axis("off"); a.set_xlim(0,1); a.set_ylim(0,1); a.set_aspect("equal"); return a
def factory(a, c):
    a.add_patch(Circle((0.5,0.5),0.46, color=PINK, ec=c, lw=1.6))
    a.add_patch(Rectangle((0.28,0.34),0.44,0.20, color=c))
    a.add_patch(Polygon([(0.28,0.54),(0.40,0.54),(0.34,0.66)], color=c))
    a.add_patch(Polygon([(0.46,0.54),(0.58,0.54),(0.52,0.66)], color=c))
    a.add_patch(Rectangle((0.62,0.54),0.06,0.16, color=c))
def rocket(a, c):
    a.add_patch(Circle((0.5,0.5),0.46, color=BLUE, ec=c, lw=1.6))
    a.add_patch(Polygon([(0.5,0.74),(0.40,0.46),(0.60,0.46)], color=c))
    a.add_patch(Rectangle((0.43,0.30),0.14,0.18, color=c))
    a.add_patch(Polygon([(0.40,0.40),(0.33,0.30),(0.40,0.30)], color=c))
    a.add_patch(Polygon([(0.60,0.40),(0.67,0.30),(0.60,0.30)], color=c))
    a.add_patch(Circle((0.5,0.56),0.05, color="white"))
def target(a, c):
    a.add_patch(Circle((0.5,0.5),0.46, color="#eef3fa", ec=c, lw=1.6))
    for r,col in [(0.34,c),(0.24,"white"),(0.13,c)]: a.add_patch(Circle((0.5,0.5),r, color=col))
factory(sq_axes(0.038, 0.778), RED)
rocket(sq_axes(0.038, 0.506), NAVY)

# ---- title ----
fig.text(0.04, 0.965, "EXHIBIT 2", fontsize=13, color="white", fontweight="bold",
         bbox=dict(boxstyle="round,pad=0.5", fc=NAVY, ec="none"))
fig.text(0.155, 0.967, "While China Leads in Inputs,", fontsize=23, fontweight="bold", color=INK)
fig.text(0.155, 0.945, "America is Better at Building Companies", fontsize=23, fontweight="bold", color=INK)
fig.text(0.04, 0.915, "US vs China across the founder's journey \u2014 each bar shows how far ahead the leader is,\nadjusted for population and economy size",
         fontsize=12.5, color="#555")

# ---- takeaway box ----
axT = fig.add_axes([0.04, 0.05, 0.93, 0.092]); axT.axis("off"); axT.set_xlim(0,1); axT.set_ylim(0,1)
axT.add_patch(FancyBboxPatch((0.005,0.06),0.99,0.88, boxstyle="round,pad=0.01,rounding_size=0.04",
                             fc="white", ec="#cfd3da", lw=1.3, mutation_aspect=0.20))
target(sq_axes(0.052, 0.076), NAVY)
axT.text(0.095, 0.80, "China supplies more of the raw inputs.", fontsize=11.5, color=INK)
axT.text(0.095, 0.56, "But America is far better at turning them into funded, fast-growing, profitable",
         fontsize=11.5, fontweight="bold", color=NAVY)
axT.text(0.095, 0.37, "companies that recycle into the next ones \u2014 and that is the harder thing to copy.",
         fontsize=11.5, fontweight="bold", color=NAVY)
axT.text(0.095, 0.15, "Startup formation itself is about even (US leads the rate, China the raw count).", fontsize=10, style="italic", color="#555")

# ---- sources ----
fig.text(0.04, 0.022, "Sources: CSET; World Bank; UN/CSIS; KPMG/CB Insights; Hurun; Damodaran/CEIC; World Bank Doing Business 2020.", fontsize=9, color=GREY)
fig.text(0.04, 0.006, "Note: VC and recovery-rate data carry caveats noted in sources. Full provenance in SOURCES_Q2.md and data/q2_calculations.csv.", fontsize=9, color=GREY)

import os; os.makedirs(FIGS, exist_ok=True)
fig.savefig(FIGS/"exhibit2.png", facecolor="white", bbox_inches="tight")
print("saved")
