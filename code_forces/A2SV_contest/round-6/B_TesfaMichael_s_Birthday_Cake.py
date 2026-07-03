def solve():
    n, k = map(int, input().split())
    s = input()

    nums = []
    off = ord('a')-1
    for l in s:
        nums.append(ord(l)-off)

    nums.sort()

    if k == 1:
        print(nums[0])
        return
    
    res = nums[0]
    stack = [nums[0]]
    for i in range(1, n):
        if nums[i] > (stack[-1]+1):
            res += nums[i]
            stack.append(nums[i])
        
        if len(stack) == k:
            print(res)
            return
    print(-1)

solve()