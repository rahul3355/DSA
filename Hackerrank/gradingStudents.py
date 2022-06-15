def breakingRecords(scores):
    high, count_high, low, count_low = scores[0],0,scores[0],0
    present = scores[0]
    for score in scores:
        if score > high:
            high = score
            count_high += 1
        if score < low:
            low = score
            count_low += 1
    
    highlow = []
    highlow.append(count_high)
    highlow.append(count_low)
    return highlow