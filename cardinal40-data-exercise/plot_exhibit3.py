"""
EXHIBIT 3 -- "Backing American Founders Pays Twice"
Two-panel scorecard: FOR INVESTORS (returns) | FOR AMERICA (society).
Colors are a navy/red checkerboard (each column carries one navy + one red stat),
so neither side is single-colored. One real chart (2.1x return gap); rest typographic.
Figures are curated from primary sources; full provenance in SOURCES.md.
Run:  python plot_exhibit3.py   ->   figures/exhibit3.png
"""
import numpy as np, pandas as pd, matplotlib.pyplot as plt
from pathlib import Path
from matplotlib.patches import FancyBboxPatch, Circle, Rectangle, Polygon, Wedge
from matplotlib.lines import Line2D

NAVY, RED, INK, GREY, LGREY = "#1b3b6b", "#cb2128", "#16181d", "#8a8d91", "#cfd3da"
NAVY_T, RED_T = "#e8eef6", "#fbe9eb"
plt.rcParams.update({"font.family": "DejaVu Sans", "axes.edgecolor": "#cccccc",
                     "figure.dpi": 160, "savefig.dpi": 160})
FW, FH = 14.0, 9.0
tint = lambda c: RED_T if c == RED else NAVY_T

# ---------- load every headline number from data/ (so each is traceable) ----------
HERE = Path(__file__).resolve().parent; DATA = HERE/"data"; FIGS = HERE/"figures"
_ret = pd.read_csv(DATA/"exhibit3_returns.csv")
PEERS   = float(_ret[_ret.group.str.contains("Non-founder")].tsr_multiple_since_2015.iloc[0])
FOUNDER = float(_ret[_ret.group.str.contains("Founder-led")].tsr_multiple_since_2015.iloc[0])
_w = pd.read_csv(DATA/"sp500_founder_built_weights.csv")
PCT_BUILT = int(_w.index_weight_pct.sum() + 0.5)          # 33 = sum of published index weights
NAMES = "  |  ".join(_w.company.tolist())
_soc = pd.read_csv(DATA/"exhibit3_societal.csv").set_index("metric")
PATENTS = int(_soc.loc["patents","value"]); JOBS = int(_soc.loc["jobs","value"])

# ---------- drawn icons (square inset axes) ----------
def sq(x, y, w=0.05):
    a = fig.add_axes([x, y, w, w*FW/FH]); a.axis("off"); a.set_xlim(0,1); a.set_ylim(0,1); a.set_aspect("equal"); return a
def i_bars(a, c):
    a.add_patch(Circle((0.5,0.5),0.47, color=tint(c), ec=c, lw=1.6))
    for xx,h in [(0.28,0.16),(0.43,0.26),(0.58,0.37)]: a.add_patch(Rectangle((xx,0.27),0.10,h, color=c))
    a.annotate("", xy=(0.74,0.70), xytext=(0.30,0.52), arrowprops=dict(arrowstyle="-|>", color=c, lw=1.7))
def i_star(a, c):
    a.add_patch(Circle((0.5,0.5),0.47, color=tint(c), ec=c, lw=1.6))
    pts=[(0.5+(0.30 if k%2==0 else 0.13)*np.cos(np.pi/2+k*np.pi/5),
          0.5+(0.30 if k%2==0 else 0.13)*np.sin(np.pi/2+k*np.pi/5)) for k in range(10)]
    a.add_patch(Polygon(pts, color=c))
def i_build(a, c):
    a.add_patch(Circle((0.5,0.5),0.47, color=tint(c), ec=c, lw=1.6))
    a.add_patch(Rectangle((0.34,0.26),0.32,0.46, color=c))
    for wy in (0.34,0.46,0.58):
        for wx in (0.40,0.50,0.60): a.add_patch(Rectangle((wx-0.02,wy),0.045,0.05, color="white"))
def i_bulb(a, c):
    a.add_patch(Circle((0.5,0.5),0.47, color=tint(c), ec=c, lw=1.6))
    a.add_patch(Circle((0.5,0.56),0.17, color=c)); a.add_patch(Rectangle((0.43,0.30),0.14,0.10, color=c))
    a.add_patch(Rectangle((0.45,0.26),0.10,0.045, color=c))
def i_people(a, c):
    a.add_patch(Circle((0.5,0.5),0.47, color=tint(c), ec=c, lw=1.6))
    for cx in (0.31,0.5,0.69):
        a.add_patch(Circle((cx,0.60),0.085, color=c)); a.add_patch(Wedge((cx,0.34),0.135,0,180, color=c))
def i_trophy(a, c):
    a.add_patch(Circle((0.5,0.5),0.47, color=tint(c), ec=c, lw=1.6))
    a.add_patch(Polygon([(0.37,0.66),(0.63,0.66),(0.585,0.46),(0.415,0.46)], color=c))
    a.add_patch(Circle((0.35,0.60),0.055, fill=False, ec=c, lw=2.3)); a.add_patch(Circle((0.65,0.60),0.055, fill=False, ec=c, lw=2.3))
    a.add_patch(Rectangle((0.47,0.34),0.06,0.13, color=c)); a.add_patch(Rectangle((0.40,0.30),0.20,0.05, color=c))

fig = plt.figure(figsize=(FW, FH)); fig.patch.set_facecolor("white")
axBG = fig.add_axes([0,0,1,1]); axBG.axis("off"); axBG.set_xlim(0,1); axBG.set_ylim(0,1)

# ---------- title ----------
fig.text(0.035, 0.95, "EXHIBIT 3", fontsize=13, color="white", fontweight="bold",
         bbox=dict(boxstyle="round,pad=0.5", fc=NAVY, ec="none"))
fig.text(0.125, 0.943, "Backing American Founders Pays Twice", fontsize=25, fontweight="bold", color=INK)
fig.text(0.035, 0.895, "Founder-led companies deliver stronger returns for investors \u2014 and more innovation and jobs for the country.",
         fontsize=12.5, color="#555")

# ---------- divider ----------
axBG.add_line(Line2D([0.508,0.508],[0.165,0.83], color="#e2e2e2", lw=1.3))

# ===================== LEFT: FOR INVESTORS =====================
i_bars(sq(0.037, 0.785), NAVY)
fig.text(0.105, 0.815, "FOR INVESTORS", fontsize=16, fontweight="bold", color=NAVY)
fig.text(0.105, 0.783, "Stronger returns", fontsize=12, color=GREY, style="italic")

# the one real chart (navy)
axR = fig.add_axes([0.05, 0.52, 0.165, 0.17])
axR.bar(0, PEERS, 0.62, color=LGREY); axR.bar(1, FOUNDER, 0.62, color=NAVY)
axR.text(0, PEERS+0.06, f"{PEERS:.1f}\u00d7", ha="center", fontsize=12.5, fontweight="bold", color=GREY)
axR.text(1, FOUNDER+0.06, f"{FOUNDER:.1f}\u00d7", ha="center", fontsize=14, fontweight="bold", color=NAVY)
axR.set_xticks([0,1]); axR.set_xticklabels(["Non-founder\npeers","Founder-led\ncompanies"], fontsize=10, fontweight="bold")
axR.set_ylim(0,2.55); axR.set_xlim(-0.65,1.65); axR.set_yticks([])
for s in ["top","right","left"]: axR.spines[s].set_visible(False)
axR.tick_params(length=0)
fig.text(0.05, 0.705, "Total shareholder return since 2015,\nvs. non-founder peers", fontsize=11, color=INK)
# callout box beside the chart
axC = fig.add_axes([0.255, 0.535, 0.215, 0.135]); axC.axis("off"); axC.set_xlim(0,1); axC.set_ylim(0,1)
axC.add_patch(FancyBboxPatch((0.02,0.06),0.96,0.88, boxstyle="round,pad=0.02,rounding_size=0.08",
                             fc="#f4f6f9", ec="#e2e2e2", lw=1.1, mutation_aspect=0.55))
axC.text(0.08, 0.66, f"{FOUNDER:.1f}\u00d7", fontsize=28, fontweight="bold", color=NAVY, va="center")
axC.text(0.46, 0.66, "higher\nreturns", fontsize=13, fontweight="bold", color=INK, va="center")
axC.text(0.10, 0.24, "(2.6\u00d7 among technology companies)", fontsize=10, color="#666", va="center")

# horizontal divider
axBG.add_line(Line2D([0.035,0.485],[0.475,0.475], color="#e8e8e8", lw=1))

# 33% concentration (RED)
i_build(sq(0.037, 0.315), RED)
fig.text(0.105, 0.30, f"{PCT_BUILT}%", fontsize=50, fontweight="bold", color=RED)
fig.text(0.25, 0.345, "of the S&P 500", fontsize=14, fontweight="bold", color=INK)
fig.text(0.25, 0.305, "is founder-built", fontsize=14, fontweight="bold", color=INK)
fig.text(0.037, 0.215, "7 of the 10 most valuable US companies were built by their founders:", fontsize=11, color="#444")
fig.text(0.037, 0.175, NAMES, fontsize=11.5, fontweight="bold", color=NAVY)

# ===================== RIGHT: FOR AMERICA =====================
i_star(sq(0.532, 0.785), NAVY)
fig.text(0.60, 0.815, "FOR AMERICA", fontsize=16, fontweight="bold", color=NAVY)
fig.text(0.60, 0.783, "A stronger country", fontsize=12, color=GREY, style="italic")

# 31% patents (RED)
i_bulb(sq(0.532, 0.595), RED)
fig.text(0.60, 0.58, f"{PATENTS}%", fontsize=50, fontweight="bold", color=RED)
fig.text(0.745, 0.625, "more patents", fontsize=15, fontweight="bold", color=INK, va="center")
fig.text(0.60, 0.53, "Founder-led firms out-innovate the rest \u2014 more,", fontsize=11.5, color="#444")
fig.text(0.60, 0.497, "higher-value patents and more R&D.", fontsize=11.5, color="#444")

# horizontal divider
axBG.add_line(Line2D([0.532,0.965],[0.475,0.475], color="#e8e8e8", lw=1))

# ~3M jobs (NAVY)
i_people(sq(0.532, 0.295), NAVY)
fig.text(0.60, 0.28, f"~{JOBS}M", fontsize=50, fontweight="bold", color=NAVY)
fig.text(0.765, 0.325, "net new jobs", fontsize=15, fontweight="bold", color=INK, va="center")
fig.text(0.765, 0.285, "a year", fontsize=15, fontweight="bold", color=INK, va="center")
fig.text(0.60, 0.225, "Young firms create essentially all of America's net new", fontsize=11.5, color="#444")
fig.text(0.60, 0.192, "jobs. 6.6M new businesses were started in 2025.", fontsize=11.5, color="#444")

# ===================== takeaway band =====================
axT = fig.add_axes([0.035, 0.052, 0.93, 0.075]); axT.axis("off"); axT.set_xlim(0,1); axT.set_ylim(0,1)
axT.add_patch(FancyBboxPatch((0.004,0.08),0.992,0.84, boxstyle="round,pad=0.01,rounding_size=0.06",
                             fc=NAVY_T, ec="#cdd8e8", lw=1.2, mutation_aspect=0.28))
i_trophy(sq(0.052, 0.066), NAVY)
axT.text(0.11, 0.66, "Backing American founders compounds investor returns and national strength at the same time \u2014",
         fontsize=13, fontweight="bold", color=NAVY, va="center")
axT.text(0.11, 0.30, "the rare bet that does both.", fontsize=13, fontweight="bold", color=NAVY, va="center")

# ===================== sources =====================
fig.text(0.035, 0.028, "Sources: Bain & Company (return gap); S&P 500 index weights, June 2026 (concentration);", fontsize=8.6, color=GREY)
fig.text(0.035, 0.011, "Purdue / Harvard Business Review (patents); Kauffman Foundation / U.S. Census BDS (jobs).", fontsize=8.6, color=GREY)
fig.text(0.55, 0.028, "Returns & patents: founder-led public companies.", fontsize=8.6, color=GREY)
fig.text(0.55, 0.011, "Jobs: startups / young firms (the broader founder ecosystem). Full provenance in SOURCES.md.", fontsize=8.6, color=GREY)

import os; os.makedirs(FIGS, exist_ok=True)
fig.savefig(FIGS/"exhibit3.png", facecolor="white", bbox_inches="tight")
print("saved")
