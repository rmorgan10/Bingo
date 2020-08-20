# A module to make a randomized BINGO card from predetermined sayings

import matplotlib.pyplot as plt
import numpy as np
import random
import sys
import textwrap

# Parse command line arguments for a outfile name
save = True
try:
    outfile = sys.argv[1]
except:
    save = False

# Read all the predetermined sayings
infile = 'squares.txt'
stream = open(infile, 'r')
sayings = stream.readlines()
stream.close()

# Do some clean up
sayings = [x for x in [y.strip() for y in sayings] if x != '']

# Choose a random set of 24 without replacement
chosen_sayings = random.sample(sayings, 24)

# Add the FREE space to the center
card = chosen_sayings[0:12] + ["FREE"] + chosen_sayings[12:]

# Wrap the text to be 18 characters wide at most
card = ['\n'.join(textwrap.wrap(x, 18)) for x in card]

# Make the main figure
plt.figure(figsize=(10,8))

# Add text to figure
x_coord = 0
y_coord = 0
for entry in card:
    plt.text(x_coord, y_coord, entry, horizontalalignment='center', verticalalignment='center')
    x_coord += 1
    if x_coord == 5:
        y_coord += 1
        x_coord = 0

# Add thicc gridlines
for line in np.linspace(-0.5, 4.5, 6):
    plt.axvline(x=line, color='black', lw=4)
    plt.axhline(y=line, color='black', lw=4)

# Remove ticks and ticklabels
plt.xticks([])
plt.yticks([])

# Set boundaries
plt.xlim(-0.5, 4.5)
plt.ylim(-0.5, 4.5)

# Add a checkerboard color scheme
color = random.choice(['blue', 'gray', 'red', 'orange', 'green', 'purple'])
for bounds in [(-0.5, 0.5), (1.5, 2.5), (3.5, 4.5)]:
    plt.axvspan(bounds[0], bounds[1], color=color, alpha=0.1)
    plt.axhspan(bounds[0], bounds[1], color=color, alpha=0.1)


# Add a title
plt.title("Cosmology Journal Club BINGO", fontsize=36)

# Add a message
width = 120
message = """
You can add a message like this! The text will automatically
wrap around to the correct width using the textwrap package.
"""
message = '\n'.join(textwrap.wrap(message, width))

plt.xlabel('\n' + message)

plt.tight_layout()

# Save if given an outifle name
if save:
    plt.savefig("{0}.pdf".format(outfile))
else:
    plt.show()
