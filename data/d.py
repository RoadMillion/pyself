nums = input("249 045 157 035 079").split()
for num in nums:
    for i in range(9):
        a = (int(num[0]) + 1) % 10
        b = (int(num[1]) + 1) % 10
        c = (int(num[2]) + 1) % 10
        num = str(a) + str(b) + str(c)
        print(num)
