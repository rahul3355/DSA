# Sort

arr = [5,4,7,3,8]
arr.sort()
print(arr)

arr.sort(reverse=True)
print(arr)

arr = ["bob", "alice", "jane", "doe"]
arr.sort()
print(arr)

arr.sort(key=lambda x: len(x))
print(arr)
