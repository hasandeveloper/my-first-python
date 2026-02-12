Numbers = [10, 25, 40, 50]
Numbers[-3]

Numbers = [10, 25, 40, 50]
Numbers[0] = 15

Numbers = [10, 25, 40, 50]
del Numbers[1]


# Like push

Numbers.append(60) # like push
# op [10, 25, 40, 50, 60]

Numbers.extend([70,80])
# op [10, 25, 40, 50, 60, 70, 80]

Numbers = [15, 40, 50]
Numbers.append(100)

# check length
len(Numbers)
# 6

Numbers[1:3]
# op [40,50]

Numbers[:2]
# op [15,40] you will get first two elements and exluding second index element

Numbers[1:]
# op [40,50,100] you will get from second index elements and including second

Numbers[-2:]
# op [50,100] last two elements

Numbers.index(50)
# 2

Fruits = ["Apple", "banana"]

data = [Numbers, Fruits]
# [[15, 40, 50,100], ["Apple", "banana"]]

[2,1,3].sort()
# op [1,2,3]

[2,1,3].sort(reverse=True)
# op [3,2,1]



