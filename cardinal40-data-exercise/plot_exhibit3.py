"""
EXHIBIT 3 -- "Backing American Founders Pays Twice"
Two columns: FOR INVESTORS (navy) | FOR AMERICA (red).
One real chart (the 2.1x return gap) is the hero of the top-left cell; every other stat is a
centered row of [icon | big number | label + supporting text], all sharing one vertical center.
Every headline number is read from data/ (see CSVs); full provenance in SOURCES.md.
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
ICON_W = 0.05
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
def sq(x, y, w=ICON_W):
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

# ---------- helpers: everything centers on a shared vertical line Yc ----------
def icon_centered(x, fn, c, Yc):
    fn(sq(x, Yc - (ICON_W*FW/FH)/2), c)
def block(wx, Yc, lines, lh=0.034):
    """lines = [(text, fontsize, weight, color)], vertically centered as a group at Yc."""
    top = Yc + (len(lines)-1)/2*lh
    for i,(t,fs,w,col) in enumerate(lines):
        fig.text(wx, top - i*lh, t, fontsize=fs, fontweight=w, color=col, va="center")
def stat_row(ix, ic, nx, num, wx, lines, Yc, c, num_fs=48):
    icon_centered(ix, ic, c, Yc)
    fig.text(nx, Yc, num, fontsize=num_fs, fontweight="bold", color=c, va="center")
    block(wx, Yc, lines)
def head(x, ic, c, title, sub, Yc=0.80):
    icon_centered(x, ic, c, Yc)
    fig.text(x+0.072, Yc+0.014, title, fontsize=16, fontweight="bold", color=c, va="center")
    fig.text(x+0.072, Yc-0.021, sub, fontsize=12, color=GREY, style="italic", va="center")

# ---------- title ----------
fig.text(0.035, 0.95, "EXHIBIT 3", fontsize=13, color="white", fontweight="bold",
         bbox=dict(boxstyle="round,pad=0.5", fc=NAVY, ec="none"))
fig.text(0.125, 0.943, "Backing American Founders Pays Twice", fontsize=25, fontweight="bold", color=INK)
fig.text(0.035, 0.895, "Founder-led companies deliver stronger returns for investors \u2014 and more innovation and jobs for the country.",
         fontsize=12.5, color="#555")

# dividers
axBG = fig.add_axes([0,0,1,1]); axBG.axis("off"); axBG.set_xlim(0,1); axBG.set_ylim(0,1)
axBG.add_line(Line2D([0.508,0.508],[0.16,0.84], color="#e2e2e2", lw=1.3))
axBG.add_line(Line2D([0.035,0.485],[0.45,0.45], color="#e8e8e8", lw=1))
axBG.add_line(Line2D([0.532,0.965],[0.45,0.45], color="#e8e8e8", lw=1))

YT, YB = 0.60, 0.33   # shared centers for the top and bottom rows

# ===================== LEFT: FOR INVESTORS (navy) =====================
head(0.037, i_bars, NAVY, "FOR INVESTORS", "Stronger returns")

# top-left cell: the bar chart is the hero (enlarged) + a compact callout
fig.text(0.05, 0.730, "Total shareholder return since 2015,", fontsize=11.5, color=INK)
fig.text(0.05, 0.703, "vs. non-founder peers", fontsize=11.5, color=INK)
axR = fig.add_axes([0.05, 0.505, 0.245, 0.185])
axR.bar(0, PEERS, 0.62, color=LGREY); axR.bar(1, FOUNDER, 0.62, color=NAVY)
axR.text(0, PEERS+0.07, f"{PEERS:.1f}\u00d7", ha="center", fontsize=14, fontweight="bold", color=GREY)
axR.text(1, FOUNDER+0.07, f"{FOUNDER:.1f}\u00d7", ha="center", fontsize=17, fontweight="bold", color=NAVY)
axR.set_xticks([0,1]); axR.set_xticklabels(["Non-founder\npeers","Founder-led\ncompanies"], fontsize=11, fontweight="bold")
axR.set_ylim(0,2.6); axR.set_xlim(-0.7,1.7); axR.set_yticks([])
for s in ["top","right","left"]: axR.spines[s].set_visible(False)
axR.tick_params(length=0)
# compact callout, vertically centered with the chart
axC = fig.add_axes([0.345, 0.545, 0.135, 0.115]); axC.axis("off"); axC.set_xlim(0,1); axC.set_ylim(0,1)
axC.add_patch(FancyBboxPatch((0.04,0.06),0.92,0.88, boxstyle="round,pad=0.02,rounding_size=0.10",
                             fc="#f4f6f9", ec="#e2e2e2", lw=1.1, mutation_aspect=0.85))
axC.text(0.5, 0.74, f"{FOUNDER:.1f}\u00d7", ha="center", va="center", fontsize=26, fontweight="bold", color=NAVY)
axC.text(0.5, 0.45, "higher returns", ha="center", va="center", fontsize=11.5, fontweight="bold", color=INK)
axC.text(0.5, 0.20, "(2.6\u00d7 in tech)", ha="center", va="center", fontsize=9.5, color="#666")

# bottom-left cell: 33% (navy), centered row + names beneath
stat_row(0.037, i_build, 0.108, f"{PCT_BUILT}%", 0.25,
         [("of the S&P 500", 14, "bold", INK), ("is founder-built", 14, "bold", INK)], YB, NAVY)
fig.text(0.037, 0.205, "7 of the 10 most valuable US companies were built by their founders:", fontsize=11, color="#555")
fig.text(0.037, 0.168, NAMES, fontsize=11.5, fontweight="bold", color=NAVY)

# ===================== RIGHT: FOR AMERICA (red) =====================
head(0.535, i_star, RED, "FOR AMERICA", "A stronger country")

# top-right cell: 31% patents (red)
stat_row(0.535, i_bulb, 0.595, f"{PATENTS}%", 0.735,
         [("more patents", 14, "bold", INK),
          ("Founder-led firms out-innovate", 11, "normal", "#555"),
          ("the rest, with more R&D spend.", 11, "normal", "#555")], YT, RED)

# bottom-right cell: ~3M jobs (red)
stat_row(0.535, i_people, 0.595, f"~{JOBS}M", 0.735,
         [("net new jobs a year", 14, "bold", INK),
          ("Young firms create nearly all of", 11, "normal", "#555"),
          ("America's jobs; 6.6M new in 2025.", 11, "normal", "#555")], YB, RED)

# ===================== takeaway band =====================
axT = fig.add_axes([0.035, 0.052, 0.93, 0.075]); axT.axis("off"); axT.set_xlim(0,1); axT.set_ylim(0,1)
axT.add_patch(FancyBboxPatch((0.004,0.08),0.992,0.84, boxstyle="round,pad=0.01,rounding_size=0.06",
                             fc=NAVY_T, ec="#cdd8e8", lw=1.2, mutation_aspect=0.28))
icon_centered(0.052, i_trophy, NAVY, 0.090)
axT.text(0.11, 0.62, "Backing American founders compounds investor returns and national strength at the same time \u2014",
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