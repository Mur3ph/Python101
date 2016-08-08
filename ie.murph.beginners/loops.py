__author__ = 'Paul'

grocery = ["Water Melon", "Raspberries", "Tuna", "Advocado", "Red Pepper"]

for i in grocery:
    print("First loop: ", i)
    print("Length of each item in the list", len(i))

for i in grocery[:2]:
    print("Second loop: ", i)

for i in grocery[2:3]:
    print("Third loop: ", i)

#Using the range in
# Zero to ten
for x in range(11):
    print(x)

# One to ten
for x in range(1, 11):
    print(x)

# Count from 1 to 11 with increments of 3's
for x in range(1, 11, 3):
    print(x)

num = 5
while num < 10:
    print("Still..")
    num += 1

magic_number = 8
for i in range(21):
    if i is magic_number:
        print(i, "is the magic number")
        break
    else:
        print(i, "not so magic")


team_number = [2, 6, 13, 15, 19]
for i in range(1,21):
    if i in team_number:
        continue
    print(i, "is the team number")


for i in range(101):
    if i % 3 == 0 and i % 5 == 0:
        print(i, "is a multiple of both 3 AND 5")
    elif i % 5 == 0:
        print(i, "is a multiple of JUST 5")
    elif i % 3 == 0:
        print(i, "is a multiple of JUST 3")
    else:
        print(i, "not multiples")

