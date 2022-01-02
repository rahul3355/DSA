def canFinish(numCourses, prerequisites):
	preMap = {i:[] for i in range(5)}
	print(preMap)

	for crs, pre in prerequisites:
		preMap[crs].append(pre)
		print(preMap)
	
	print(preMap)

canFinish(5, [[0,1],[0,2],[1,2],[2,3],[2,4]])


