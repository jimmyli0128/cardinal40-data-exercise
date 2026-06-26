"""
EXHIBIT 1 -- "The US Has Fallen Behind in Critical-Tech Research"
Reproduces the exhibit from data/ CSVs (ASPI Critical Technology Tracker).
  A: technologies-led flip (bars) + center callout + current research-share (big numbers)
  B: scoreboard of who leads where + thin-gap bars for the 7 US-led fields
Run:  python plot_exhibit1.py   ->   figures/exhibit1.png
"""
import pandas as pd, matplotlib.pyplot as plt
from pathlib import Path
HERE = Path(__file__).resolve().parent; DATA = HERE/"data"; FIGS = HERE/"figures"
from matplotlib.patches import FancyBboxPatch
from matplotlib.lines import Line2D

NAVY, RED, INK, GREY, BG = "#1b3b6b", "#cb2128", "#16181d", "#8a8d91", "#f3f3f1"
plt.rcParams.update({"font.family": "DejaVu Sans", "axes.edgecolor": "#cccccc",
                     "figure.dpi": 170, "savefig.dpi": 170})

# ---------- data ----------
flip = pd.read_csv(DATA/"aspi_tech_flip.csv")
def led(period, country):
    return int(flip[(flip.period == period) & (flip.country == country)].technologies_led.iloc[0])
us03, cn03 = led("2003-2007", "United States"), led("2003-2007", "China")
us19, cn19 = led("2019-2023", "United States"), led("2019-2023", "China")

cat = pd.read_csv(DATA/"aspi_categories.csv")
clear   = [("Hypersonic detection & tracking", 73), ("Electric batteries", 68), ("Advanced aircraft engines", 63)]
flipped = [("High-performance computing", 31), ("Advanced ICs (semiconductors)", 24), ("Space launch systems", 23)]
usleads = [("Genetic engineering", 37), ("Quantum computing", 34), ("Atomic clocks", 30)]

gap = pd.read_csv(DATA/"aspi_us_led_gap.csv")
us_avg, cn_avg = round(gap.us_share.mean(), 1), round(gap.china_share.mean(), 1)   # 28.8 / 20.2

# research share, 2019-23 (computed from ASPI Appendix 1; see SOURCES.md)
us_research, cn_research = 13, 39

fig = plt.figure(figsize=(16, 9)); fig.patch.set_facecolor("white")

# ===================== TITLE =====================
fig.text(0.032, 0.945, "EXHIBIT 1", fontsize=13, color="white", fontweight="bold",
         bbox=dict(boxstyle="round,pad=0.5", fc=NAVY, ec="none"))
fig.text(0.115, 0.935, "The US Has Fallen Behind in Critical-Tech Research", fontsize=27, fontweight="bold", color=INK)
fig.text(0.032, 0.862, "A.   In 20 years, China went from leading 3 to 57 of 64 critical technologies",
         fontsize=15.5, fontweight="bold", color=NAVY)

# ===================== A-LEFT: technologies-led bars =====================
axL = fig.add_axes([0.05, 0.545, 0.205, 0.245])
gxx = [0, 1.15]; w = 0.42
for i, (u, c) in enumerate([(us03, cn03), (us19, cn19)]):
    axL.bar(gxx[i]-0.23, u, w, color=NAVY); axL.bar(gxx[i]+0.23, c, w, color=RED)
    axL.text(gxx[i]-0.23, u+2, str(u), ha="center", fontsize=15, fontweight="bold", color=NAVY)
    axL.text(gxx[i]+0.23, c+2, str(c), ha="center", fontsize=15, fontweight="bold", color=RED)
axL.set_xticks(gxx); axL.set_xticklabels(["2003\u20132007", "2019\u20132023"], fontsize=12, fontweight="bold")
axL.set_ylim(0, 80); axL.set_yticks([0,20,40,60,80]); axL.set_xlim(-0.7, 1.85)
axL.tick_params(length=0, labelsize=10)
for s in ["top","right"]: axL.spines[s].set_visible(False)
fig.text(0.05, 0.81, "Technologies Led (out of 64)", fontsize=13.5, fontweight="bold", color=INK)
axBG = fig.add_axes([0,0,1,1], zorder=5); axBG.axis("off"); axBG.set_xlim(0,1); axBG.set_ylim(0,1)
# legend inside the chart, in the empty valley between the two tall bars
axL.scatter(0.42, 73, marker="s", s=150, color=NAVY); axL.text(0.53, 73, "United States", va="center", fontsize=11, color=INK)
axL.scatter(0.42, 64, marker="s", s=150, color=RED);  axL.text(0.53, 64, "China", va="center", fontsize=11, color=INK)

# ===================== A-CENTER: flipped callout =====================
axC = fig.add_axes([0.295, 0.58, 0.115, 0.165]); axC.axis("off"); axC.set_xlim(0,1); axC.set_ylim(0,1)
axC.add_patch(FancyBboxPatch((0.06, 0.10), 0.88, 0.82, boxstyle="round,pad=0.03,rounding_size=0.10",
                             fc=BG, ec="#dcdcd8", lw=1.3, mutation_aspect=0.7))
axC.text(0.5, 0.66, "China's lead\nflipped from", ha="center", va="center", fontsize=13.5, color=INK, fontweight="bold")
axC.text(0.5, 0.28, "3 to 57", ha="center", va="center", fontsize=21, color=RED, fontweight="bold")
# 90-degree orthogonal connector from the "2003-2007" label to the center callout box
# Traces a sharp, stepped path: Down from label -> Across -> Straight up into the box center
axBG.add_line(Line2D([0.11, 0.11, 0.35, 0.35], [0.53, 0.50, 0.50, 0.57], 
                     ls="--", color="#b9b9b9", lw=1.5))

# Sharp vertical arrowhead cap pointing directly into the bottom center of the box
axBG.annotate("", xy=(0.35, 0.58), xytext=(0.35, 0.565),
             arrowprops=dict(arrowstyle="-|>", color="#b9b9b9", lw=1.5, mutation_scale=12))

# ===================== A-RIGHT: research-share big numbers =====================
fig.text(0.455, 0.81, "Current Share of High-Impact Research (%)", fontsize=13.5, fontweight="bold", color=INK)
fig.text(0.455, 0.782, "2019\u20132023", fontsize=11, color=GREY)
fig.text(0.53, 0.66, f"{us_research}%", fontsize=44, fontweight="bold", color=NAVY, ha="center")
fig.text(0.53, 0.615, "United States", fontsize=12.5, color=INK, ha="center")
fig.text(0.66, 0.66, f"{cn_research}%", fontsize=44, fontweight="bold", color=RED, ha="center")
fig.text(0.66, 0.615, "China", fontsize=12.5, color=INK, ha="center")
# "~3x larger" callout
axW = fig.add_axes([0.48, 0.495, 0.235, 0.085]); axW.axis("off"); axW.set_xlim(0,1); axW.set_ylim(0,1)
axW.add_patch(FancyBboxPatch((0.02, 0.08), 0.96, 0.84, boxstyle="round,pad=0.02,rounding_size=0.10",
                             fc=BG, ec="#dcdcd8", lw=1.2, mutation_aspect=0.3))
axW.scatter(0.11, 0.5, s=620, facecolor="white", edgecolor=INK, lw=1.6, zorder=2)
axW.text(0.11, 0.5, "\u2191", ha="center", va="center", fontsize=16, color=INK, zorder=3)
axW.text(0.22, 0.5, "China's share is ~3\u00d7 larger\nand the gap is widening.", ha="left", va="center",
         fontsize=12, color=INK)

# ===================== A far-right: info =====================
axI = fig.add_axes([0.75, 0.575, 0.185, 0.20]); axI.axis("off"); axI.set_xlim(0,1); axI.set_ylim(0,1)
axI.scatter(0.07, 0.86, s=230, facecolor="white", edgecolor="#9aa0a8", lw=1.4, zorder=2)
axI.text(0.07, 0.86, "i", ha="center", va="center", fontsize=11, style="italic", color="#5a6068", zorder=3)
axI.text(0.16, 0.90, "High-impact papers are in the top\n10% most-cited research papers\n\u2014 a leading indicator of future\ncapability.",
         ha="left", va="top", fontsize=11.5, color="#555")

# ===================== B =====================
fig.text(0.032, 0.44, "B.   China now leads most technologies\u2014and is close behind in the rest",
         fontsize=15.5, fontweight="bold", color=NAVY)
axB = fig.add_axes([0.03, 0.05, 0.945, 0.37]); axB.axis("off"); axB.set_xlim(0,1); axB.set_ylim(0,1)

def column(x, icon, icol, head, sub, items, pcol, items_x=None):
    # If items_x isn't specified, it defaults to the header's x position
    if items_x is None:
        items_x = x
        
    # Header elements (uses the 'x' parameter)
    axB.scatter(x+0.013, 0.88, s=540, color=icol, zorder=2)
    axB.text(x+0.013, 0.88, icon, ha="center", va="center", color="white", fontsize=13, fontweight="bold", zorder=3)
    axB.text(x+0.05, 0.905, head, ha="left", va="center", fontsize=13, fontweight="bold", color=icol)
    axB.text(x+0.05, 0.79, sub, ha="left", va="center", fontsize=10.5, style="italic", color="#777")
    
    # Technology list elements (uses the separate 'items_x' parameter)
    for i, (name, sh) in enumerate(items):
        yy = 0.58 - i*0.165
        axB.text(items_x, yy, name, ha="left", va="center", fontsize=12, color=INK)
        axB.text(items_x+0.21, yy, f"{sh}%", ha="right", va="center", fontsize=12.5, fontweight="bold", color=pcol)

# Draw the columns
column(0.00, "\u2605", RED, "CHINA LEADS CLEARLY", "Decisive margins", clear, RED)

# Title is shifted to 0.225, but technologies stay anchored at 0.255
column(0.225, "\u00bb", RED, "CHINA JUST PASSED THE US", "Overtook in the 2020s \u2014 narrow", flipped, RED, items_x=0.255)

column(0.50, "\u25c6", NAVY, "U.S. STILL LEADS", "7 of 64", usleads, NAVY)
# col 4: thin-gap bars
x4 = 0.745
axB.text(x4, 0.94, "Even in the US's strengths,", ha="left", fontsize=13, fontweight="bold", color=INK)
axB.text(x4, 0.875, "the lead is thin", ha="left", fontsize=13, fontweight="bold", color=INK)
axB.text(x4, 0.745, "Avg. share of high-impact papers across\nthe 7 US-led technologies (2019\u201323)", ha="left", va="top", fontsize=9.8, color="#777")
def gbar(y, val, c, lab):
    bx = x4+0.055; ww = (val/30.0)*0.115
    axB.text(x4, y+0.035, "US" if c==NAVY else "China", ha="left", va="center", fontsize=11, color="#444")
    axB.add_patch(plt.Rectangle((bx, y), ww, 0.075, color=c))
    axB.text(bx+ww+0.008, y+0.037, lab, ha="left", va="center", fontsize=12, fontweight="bold", color=c)
gbar(0.40, us_avg, NAVY, f"{us_avg}%")
gbar(0.24, cn_avg, RED, f"{cn_avg}%")
bxr = 0.975
for ya,yb in [((0.255,0.495))]:
    axB.add_line(Line2D([bxr,bxr],[ya,yb], color="#999", lw=1.1))
    axB.add_line(Line2D([bxr-0.01,bxr],[yb,yb], color="#999", lw=1.1))
    axB.add_line(Line2D([bxr-0.01,bxr],[ya,ya], color="#999", lw=1.1))
axB.text(bxr+0.008, 0.375, f"Gap:\n{round(us_avg-cn_avg,1)} pts", ha="left", va="center", fontsize=11, color="#555")

# ===================== source =====================
fig.text(0.032, 0.028, "Source: ASPI Critical Technology Tracker (two-decade report, Aug 2024).", fontsize=9, color=GREY)
fig.text(0.032, 0.008, "Note: Research-share figures: 2019\u201323 computed from ASPI Appendix 1; \u201cleads\u201d = highest share of top-cited research, a leading indicator (not deployed capability).",
         fontsize=9, color=GREY)

import os; os.makedirs(FIGS, exist_ok=True)
fig.savefig(FIGS/"exhibit1.png", facecolor="white", bbox_inches="tight")
print("saved  US/China led:", (us03,cn03), "->", (us19,cn19), "| gap:", us_avg, cn_avg)
