'''Car Pooling

There is a car with capacity empty seats. The vehicle only drives east
(it cannot turn around and drive west).

You are given an integer capacity and an array trips where:

trips[i] = [numPassengers, from, to]

means:
- numPassengers passengers are picked up at location from
- and dropped off at location to

Return true if it is possible to complete all trips without exceeding
the vehicle capacity at any point, otherwise return false.


Example 1:

Input:
trips = [[2,1,5],[3,3,7]]
capacity = 4

Output:
false


Example 2:

Input:
trips = [[2,1,5],[3,3,7]]
capacity = 5

Output:
true


Example 3:

Input:
capacity = 5
trips = [
 [1,2,4],
 [3,4,6],
 [2,1,5]
]

Output:
true'''


capacity = int(input())
n = int(input())
trips = []

result = []

for _ in range(n):
    lst = list(map(int, input().split()))
    trips.append(lst[:])

for trip in trips:
    passn, strt, drp = trip
    result.append([strt, passn])
    result.append([drp, -1 * passn])

result = sorted(result)

cap = 0

for i in result:
    cap += i[1]
    if cap > capacity:
        print("false")
        exit()

print("true")