def countingValleys(steps, path):
    # Write your code here
    current_level, valley = 0, 0
    for i in range(len(path)):
        if path[i] == "D":
            current_level -= 1
        if path[i] == "U":
              current_level += 1
        if current_level == 0 and path[i]=="U":
            valley += 1
    return valley