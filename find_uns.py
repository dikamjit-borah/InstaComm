file1 = open('him_likers', 'r', newline='')
list1 = []
file2 = open('him_following', 'r')
list2 = []
file3 = open('him_followers', 'r')
list3 = []

for i in file1:
    if(i!=''):
        i = i.replace('\r', '')
        list1.append(i)
list1 = list(dict.fromkeys(list1))


for i in file2:
    if(i!=''):
        list2.append(i)
list2 = list(dict.fromkeys(list2))

unlikers = []

for i in list2:
    if i not in list1:
            unlikers.append(i)

unfollowers =[]

for i in file3:
    if(i!=''):
        i = i.replace('\r', '')
        list3.append(i)
list3 = list(dict.fromkeys(list3))



# x = len(set(list1).difference(list2))
# print(x)

# y =set(list2).difference(list3)

# print(len(list3))
# print((y))