from snorkel.models import Bbox
from snorkel.contrib.babble import Explanation

# Box X = Person (category_id = 1)
# Box Y = Bike (category_id = 2)

A = Bbox(top=100, bottom=200, left=100, right=200)
B = Bbox(top=150, bottom=250, left=150, right=250)
C = Bbox(top=300, bottom=350, left=300, right=350)
D = Bbox(top=250, bottom=450, left=250, right=450)

"""


        ----------
        | A       |
        |     ----|-----
        |    |    |    |
        -----|----     |
             |       B |
             __________-----------------
                       | D              |
                       |    ----        |
                       |   | C  |       |
                       |    ----        |
                       |                |
                       |                |
                       -----------------
      
"""

a_and_b = (A, B)
a_and_c = (A, C)
d_and_c = (D, C)


edges = [
    # Edges of same box
    Explanation(
        condition="the bottom of box x is below the top of box x",
        label=True,
        candidate=a_and_b,
        semantics=None),
    # Edges of different boxes
    Explanation(
        condition="the top of box y is below the top of box x",
        label=True,
        candidate=a_and_b,
        semantics=None),
]

points = [
    # Corner to Corner
    Explanation(
        condition="the bottom right corner of box x, is below the left top corner of box x",
        label=True,
        candidate=a_and_b,
        semantics=None),
    # Center to Center
    Explanation(
        condition="the center of box y is below the center of box x",
        label=True,
        candidate=a_and_b,
        semantics=None),
    # Center to Corner
    Explanation(
        condition="the center of box y is below the top right corner of box x",
        label=True,
        candidate=a_and_b,
        semantics=None),
    # Center to Edge
    Explanation(
        condition="the center of box y is below the top edge of box x",
        label=True,
        candidate=a_and_b,
        semantics=None),
]

boxes = [
    # Box above
    Explanation(
        condition="box x is above box y",
        label=True,
        candidate=a_and_b,
        semantics=None),
    # Box below
    Explanation(
        condition="box y is below box x",
        label=True,
        candidate=a_and_b,
        semantics=None),
    # Box left
    Explanation(
        condition="box x is left of box y",
        label=True,
        candidate=a_and_b,
        semantics=None),
    # Box right
    Explanation(
        condition="box y is to the right of box x",
        label=True,
        candidate=a_and_b,
        semantics=None),
    # Box near (point and box)
    Explanation(
        condition="box x is near the top left corner of box y",
        label=True,
        candidate=a_and_b,
        semantics=None),
    # Box near (box and box)
    Explanation(
        condition="box x is in the same place as box y",
        label=True,
        candidate=d_and_c,
        semantics=None),
    # Box far
    Explanation(
        condition="box x is far away from box y",
        label=True,
        candidate=a_and_c,
        semantics=None),
    # Box within
    Explanation(
        condition="box x is not within box y",
        label=True,
        candidate=a_and_b,
        semantics=None),
]

comparisons = [
    # Top
    Explanation(
        condition="the top of box x is above the top of box y",
        label=True,
        candidate=a_and_b,
        semantics=None),
    # Bottom
    Explanation(
        condition="the bottom of box y is below the bottom of box x",
        label=True,
        candidate=a_and_b,
        semantics=None),
    # Past (bottom)
    Explanation(
        condition="box y is past the bottom of box x",
        label=True,
        candidate=a_and_b,
        semantics=None),
    # Left
    Explanation(
        condition="the left of box x is to the left of the left edge of box y",
        label=True,
        candidate=a_and_b,
        semantics=None),
    # Right
    Explanation(
        condition="the right edge of box y is to the right of the left edge of box x",
        label=True,
        candidate=a_and_b,
        semantics=None),
    # Near
    Explanation(
        condition="the center of box x is near the top left corner of box y",
        label=True,
        candidate=a_and_b,
        semantics=None),
    # Far
    Explanation(
        condition="the top left corner of box x is far from the bottom right corner of box y",
        label=True,
        candidate=a_and_b,
        semantics=None),
]

quantified = [
    # Larger
    Explanation(
        condition="box x is larger than box y",
        label=True,
        candidate=a_and_c,
        semantics=None),
    # Much Larger
    # Explanation(
    #     condition="box x is much larger than box y",
    #     label=True,
    #     candidate=a_and_c,
    #     semantics=None),
    # Smaller
    Explanation(
        condition="box Y is smaller than box X",
        label=True,
        candidate=a_and_c,
        semantics=None),
    # Same Area
    Explanation(
        condition="box X is the same size as box Y",
        label=True,
        candidate=a_and_b,
        semantics=None),
    # # Smaller
    # Explanation(
    #     condition="box y is much smaller than box x",
    #     label=True,
    #     candidate=a_and_c,
    #     semantics=None),
    # Taller
    Explanation(
        condition="box x is taller than box y",
        label=True,
        candidate=a_and_c,
        semantics=None),
    # Wider
    Explanation(
        condition=" Box X is wider than Box Y",
        label=True,
        candidate=a_and_c,
        semantics=None),
    # Same Width
    Explanation(
        condition="box X is as wide as box Y",
        label=True,
        candidate=a_and_b,
        semantics=None),
    # Overlaps (0.25 thresh)
    Explanation(
        condition="box x overlaps with box y",
        label=True,
        candidate=a_and_b,
        semantics=None),
    # Within
    Explanation(
        condition="box y is within with box x",
        label=True,
        candidate=d_and_c,
        semantics=None),
    # Surrounds
    Explanation(
        condition="box x surrounds box y",
        label=True,
        candidate=d_and_c,
        semantics=None),
]

parser = [
    #Period at the end of the sentence, explanation 121
    Explanation(
        condition="Box X is much wider than Box Y.",
        label=True,
        candidate=a_and_c,
        semantics=None),
        #Period at the end of the sentence, explanation 121
    Explanation(
        condition="Box Y is to the right of Box X.",
        label=True,
        candidate=a_and_c,
        semantics=None),
]

possessives = [
    # Bbox's side
    Explanation(
        condition="Box x's top edge is above box y's center.",
        label=True,
        candidate=a_and_c,
        semantics=None),
    # Bbox's center
    Explanation(
        condition="the center of box y is below box x's center",
        label=True,
        candidate=a_and_b,
        semantics=None),
    # Bbox's corner
    Explanation(
        condition="the bottom right corner of box x, is below box x's left top corner",
        label=True,
        candidate=a_and_b,
        semantics=None),
    # Bbox's left/right
    Explanation(
        condition="box y is to box x's right",
        label=True,
        candidate=a_and_b,
        semantics=None),
]

explanations = (edges + points + comparisons + boxes + quantified + parser + possessives)