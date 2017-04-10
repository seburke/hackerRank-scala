


def mergeSort(l, inversions):
	if len(l) < 2:
		return l, inversions
	result = []
	mid = len(l) / 2 
	left, li = mergeSort(l[:mid], inversions)
	right, ri = mergeSort(l[mid:], inversions)
	inversions += li
	inversions += ri
	i = 0
	j = 0
	leftLen = len(left)
	rightLen = len(right)
	while i < leftLen and j < rightLen:
		#This calls for inversions based on size of left
		if right[j] < left[i]: 
			result.append(right[j])
			j += 1
			inversions += leftLen - i
		else:
			result.append(left[i])
			i += 1
	result += left[i:]
	result += right[j:] 
	return result, inversions





def count_inversions(a):
	r, inversions = mergeSort(a, 0)
	return inversions



t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    arr = map(int, raw_input().strip().split(' '))
    print count_inversions(arr)

