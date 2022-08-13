nums = [int(i) for i in input().split()]

if len(nums) < 2:
    print('Ошибка. Кучек слишком мало, чтобы можно было решить задачу.')
else:
    if (len(nums) % 2 == 1) or (sum(nums) % 2 == 0 and len(nums) != 2) or (len(nums) == 2 and nums[0] == nums[1]):
        c = 0
        while len(set(nums)) > 1:
            nums[nums.index(min(nums))] += 1
            nums[nums.index(min(nums))] += 1
            c += 1
        print(c, max(nums))
    else:
        print('Кучки нельзя уравнять')
