def migratoryBirds(arr):
    count, currentBird = arr[0], arr[0]
    set_arr = set(arr)
    for bird in set_arr:
        x = arr.count(bird)
        if x > count:
            count = x
            currentBird = bird
    return currentBird