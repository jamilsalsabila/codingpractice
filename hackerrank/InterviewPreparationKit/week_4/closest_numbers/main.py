def closestNumbers(arr):
    result = []
    arr.sort()
    min_diff = abs(arr[1] - arr[0])
    for i in range(2, len(arr)):
        if abs(arr[i] - arr[i-1]) == min_diff:
            result.append(arr[i-1])
            result.append(arr[i])
        elif abs(arr[i] - arr[i-1]) < min_diff:
            result.clear()
            result.append(arr[i-1])
            result.append(arr[i])
            min_diff = abs(arr[i] - arr[i-1])
    if abs(arr[1] - arr[0]) == min_diff:
        result.insert(1, arr[1])
        result.insert(0, arr[0])
    return result
    
print(*closestNumbers([1,2,3,4,5]))
print(*closestNumbers([-20, -3916237, -357920, -3620601, 7374819, -7330761, 30, 6246457, -6461594, 266854]))
print(*closestNumbers([-20,-3916237,-357920,-3620601,7374819,-7330761,30,6246457,-6461594,266854,-520,-470]))
print(*closestNumbers([5,4,3,2]))
    
