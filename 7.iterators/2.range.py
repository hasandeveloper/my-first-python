print(list(range(1,11)))

# print even and odd

for n in range(20):
    if n % 2 == 0:
        print(n)
    else:
        print(n)

n = [1,2,3,4,5,6]

for x in n:
    print(x * 10)

nums = [1,35,12,24,31,51,70,100]

# You are provided with the nums list. Define a function called count() containing a while loop to count the number of values in the nums list that are lower than 20.
def count(nums):
    n = 0
    c = 0
    while n < len(nums):
        if nums[n] < 20:
            c += 1
        n+=1
    return c 

print(count(nums))