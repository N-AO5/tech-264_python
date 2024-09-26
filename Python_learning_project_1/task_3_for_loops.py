
list_data = [1, 2, 3, 4, 5]

embedded_lists = [[1,2,3],[4,5,6]]

dict_data = {1: {"name": "Bronson", "money": "$0.05"}, 2: {"name": "Masha", "money": "$3.66"}, 3: {"name": "Roscoe", "money": "$1.14"}}

#1.
for num in list_data:
    print(num + num)
#2.
for data in embedded_lists:
    print(data)

#3.
for data in embedded_lists:
    print(data)
    for items in data:
        print(items)
#4.
for key in dict_data:
    print(key)

#5.
for key in dict_data.values():
    print(key)

#6.
for key in dict_data.values():
 for values in key.values():
        print(values)

#7.
for data in dict_data.values():
    print(data["money"])

#8
for data in list_data:
    if data < 3:
        print("less than 3")
    elif data == 3:
        print("I found 3")
    elif data > 3:
        print("greater than 3")

#8 (option)
for data in list_data:
    if data < 3:
        print("less than 3")
    elif data == 3:
        print("I found 3")
    else:
        print("greater than 3")




