
"""
patterns = [
        "n^2",
        "n^3"
        ]
"""

patterns = [ f"n^{exp}" for exp in range(1, 10 + 1) ]

print("patterns:")
print(patterns)


for pattern in patterns:
    
