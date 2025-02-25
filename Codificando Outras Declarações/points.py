points = 7600
points_needed = 8000

if points >= points_needed:
    print("You're level 2")
else:
    left = points_needed - points
    print("Points till level 2:")
    print(left)