from opimodel import colors, fonts, rules, widgets
from renderers.css import render
import os

# Read the color and font data CSStudio configuration files
example_dir = os.path.dirname(os.path.realpath(__file__))
colors.parse_css_color_file(os.path.join(example_dir, 'color.def'))
fonts.parse_css_font_file(os.path.join(example_dir, 'font.def'))

# Create the root widget
d = widgets.Display(100, 100)
# Add a rectangle.
w = widgets.Rectangle(0, 0, 10, 10)
w.set_fg_color(colors.YELLOW_LED_OFF)
d.add_child(w)

# Add a grouping container.
group = widgets.GroupingContainer(30, 30, 90, 90)

# Add two action buttons to the grouping container.
ab = widgets.ActionButton(30, 30, 30, 30, 'hello')
ab.add_write_pv('hello', 'bye')
group.add_child(ab)
ab2 = widgets.ActionButton(60, 60, 60, 60, 'ls')
ab2.add_shell_command('ls')
group.add_child(ab2)

# Add a rule to the grouping container.
group.rules = []
group.rules.append(
    rules.GreaterThanRule('visible', 'SR-CS-FILL-01:COUNTDOWN', 300))
d.add_child(group)

# Add a label with fonts and colour from the config files
l = widgets.Label(100, 100, 200, 20, "test_label")
l.set_font(fonts.FINE_PRINT)
d.add_child(l)

# Write the OPI file.
o = render.get_opi_renderer(d)
o.write_to_file("cssgen_example.opi")
