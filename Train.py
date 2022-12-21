# Function to find the minimum number of platforms needed
def findMinPlatforms(arrival, departure):
    arrival.sort()
    departure.sort()
    count = 0
    platforms = 0
    i = j = 0
    while i < len(arrival):
        if arrival[i] < departure[j]:
            count = count + 1
            platforms = max(platforms, count)
            i = i + 1
        else:
            count = count - 1
            j = j + 1
 
    return platforms
 
 
if __name__ == '__main__':
    a=int(input("Enter no.of elements : "))
    print("Enter the arrival timings : ")
    arrival=[]
    for i in range(a):
        arrival.append(int(input()))
    print("Enter the departure timings : ")
    departure=[]
    for i in range(a):
        departure.append(int(input()))
    print("The minimum platforms needed is", findMinPlatforms(arrival, departure))