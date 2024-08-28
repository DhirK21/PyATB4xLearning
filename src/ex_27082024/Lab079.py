my_shopping_list = ["bread", "milk", "butter"]
# To remove the duplicate from the list -> set - data
print(my_shopping_list[0])
print(len(my_shopping_list))


def bring_more_food(my_list):
    more_item = input("Enter the item: ")
    my_list.append(more_item)
    # my_list.remove(more_item)
    # my_list.insert(0, more_item)
    return my_list


print("*******************")
l = bring_more_food(my_shopping_list)
print(l)