import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import FancyArrowPatch


import numpy as np

plt.rcParams.update({"font.size": 18, "font.family":"serif",
                     "mathtext.fontset": "dejavuserif"})

xr = (0.7, 2)

x_fine = np.linspace(*xr, 100)
x = np.linspace(*xr, 7)

f_fine = np.sin(x_fine)
f = np.sin(x)

fig, ax = plt.subplots(layout="constrained")

ax.set_xlabel("")
ax.set_ylabel("$f\,(x)$")
labels = [r"$x_{i%+d}$" % (i-3) for i in range(len(x))]
labels[3] = r"$x_i$"

ax.set_xticks(ticks=x, labels=labels)
ax.set_yticks(ticks=[], labels=[])

ax.set_ylim(0.6, 1.02)

for i, (xi, fi, label) in enumerate(zip(x, f, labels)):
    line = Line2D((xi, xi), (0, fi), color="grey", linestyle="--")
    ax.add_line(line)
    txt = ax.text(xi, fi+0.01, label.replace("x", "f"), horizontalalignment="right", verticalalignment="bottom")

    if i >= 3:
        txt.set_horizontalalignment("center")

    if i >= 5:
        txt.set_horizontalalignment("left")

ax.plot(x_fine, f_fine, "-")
ax.plot(x, f, 'o')

dx = x[1] - x[0]
arrow = FancyArrowPatch((x[1], f[1] - 0.1), (x[2], f[1] - 0.1), arrowstyle='<->', mutation_scale=20)
ax.add_patch(arrow)
ax.text(x[1] + dx/2, f[1] - 0.1, r"$\Delta x$", horizontalalignment="center", verticalalignment="bottom")

ax.spines["right"].set_visible(False)
ax.spines["top"].set_visible(False)

print(ax.yaxis.get_view_interval())
bottom = ax.yaxis.get_view_interval()[0]
ax.plot(x, [bottom]*len(x), 'o', clip_on=False, color="C0")

xax = ax.xaxis.get_view_interval()
yax = ax.yaxis.get_view_interval()

arrow = FancyArrowPatch((xax[0], yax[0]), (xax[0], yax[1]), arrowstyle='-|>', mutation_scale=20, clip_on=True)
ax.add_patch(arrow)
plt.savefig("../source/images/func_on_grid.png")

plt.show()

