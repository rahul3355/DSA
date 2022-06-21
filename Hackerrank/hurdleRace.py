def hurdleRace(k, height):
    # Write your code here
    if max(height) > k:
        return max(height) - k
    else:
        return 0