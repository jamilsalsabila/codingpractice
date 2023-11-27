n = int(input().strip())
for _ in range(n):
    time = list(map(lambda n: int(n), input().strip().split()))
    ans = [0, 0, 0, 0]
    for i in range(7, 3, -1):
        if time[i]-time[i-4] < 0:
            ans[i-4] = 60-(-(time[i]-time[i-4]))
            time[i-1] = time[i-1]-1
        else:
            ans[i-4] = time[i]-time[i-4]
    print(f"({ans[0]} {ans[1]} {ans[2]} {ans[3]}) ")