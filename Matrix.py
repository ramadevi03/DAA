# Importing Module
from bisect import bisect_right as upper_bound

# Function To Find Median In The Matrix
def binaryMedian( Matrix , R , C ):
	min = Matrix[0][0]
	max = 0

	for i in range(R):
		if Matrix[i][0] < min:
			min = Matrix[i][0]
		if Matrix[i][C-1] > max :
			max = Matrix[i][C-1]

	desired = (R * C + 1) // 2

	while (min < max):
		mid = min + (max - min) // 2
		place = [0];
		for i in range(R):
			j = upper_bound(Matrix[i], mid)
			place[0] = place[0] + j
		if place[0] < desired:
			min = mid + 1
		else:
			max = mid
	print ("Median is : ", min)
	return

# Input Of The Matrix
R = int(input("Enter no.of rows : "))
C = int(input("Enter no.of Columns : "))
print("Enter the elements of the matrix : ")
Matrix = []
for i in range(R):
    a = []
    for j in range(C):
        a.append(int(input()))
    Matrix.append(a)
binaryMedian( Matrix , R , C )