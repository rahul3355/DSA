def repeatedString(s, n):
    # Write your code here
    return (s.count("a") * (n // len(s)) + s[:n % len(s)].count("a"))