import draw

"""
patterns = [
        "n^2",
        "n^3"
        ]
"""

patterns = [ f"{t}n+1" for t in range(1, 20 + 1) ]
# patterns = [ f"math.pow(n, {exp})" for exp in range(1, 20 + 1) ]
# patterns = [ f"n ** {exp}" for exp in range(1, 3 + 1) ]

print("patterns:")
print(patterns)


for pattern in patterns:
    draw.draw_class(pattern=pattern, n=500, radius=400)
