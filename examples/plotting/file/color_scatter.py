
import numpy as np
from six.moves import zip
from bokeh.plotting import *

N = 4000

x = np.random.random(size=N) * 100
y = np.random.random(size=N) * 100
radii = np.random.random(size=N) * 1.5
colors = ["#%02x%02x%02x" % (r, g, 150) for r, g in zip(np.floor(50+2*x), np.floor(30+2*y))]

output_file("color_scatter.html", title="color_scatter.py example")

TOOLS="crosshair,pan,wheel_zoom,box_zoom,reset,tap,previewsave,box_select,poly_select"
scatter(x,y, radius=radii, radius_units="data",
       fill_color=colors, fill_alpha=0.6,
        line_color=None, Name="color_scatter_example", tools=TOOLS)

show()  # open a browser
