arr = [5,4,3,4,24,566,5,32,4,0,2]
print("Original Array -> ", arr)

print("\n\nappend()")
arr.append(69)
print("Appended Array -> ", arr)


print("\n\ncopy()")
arr2 = arr.copy()
print("Copied Array -> ", arr2)

print("\n\ncount()")
n = arr.count(4)
print("Count number of 4s -> ", n)


print("\n\nextend()")
arr3 = [5,5,5,5,5]
arr.extend(arr3)
print("Extended Array -> ", arr)


print("\n\nindex()")
m = arr.index(3)
print("Index of 3 -> ", m)

print("\n\ninsert()")
arr.insert(0,420)
print("Insert Array -> ", arr)

print("\n\npop()")
arr.pop(3)
print("Popped Array -> ", arr)

print("\n\nremove()")
arr.remove(4)
print("Removed Array -> ", arr)

print("\n\nreverse()")
arr.reverse()
print("Reversed Array -> ", arr)

print("\n\nSort()")
arr.sort()
print("Sorted Array -> ", arr)