def angryProfessor(k, a):
    # Write your code here
    count = 0
    for student in a:
        if student <= 0:
            count += 1
    if count >= k:
        return "NO"
    else:
        return "YES"