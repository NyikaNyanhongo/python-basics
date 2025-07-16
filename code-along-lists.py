#create an empty list 

todo_list = []
print("your to do list:" , todo_list)

#append items to the list 

todo_list.append("Buy groceries")
todo_list.append("Finish homework")
todo_list.append("Call Mom")

print("Updated list:", todo_list) 

#insert an item

todo_list.insert
print("After inserting an item:", todo_list)


# using indexes and slicing

print("First task:", todo_list[0])
print("Last two tasks:", todo_list[-2:1])

#mark task as done

done_task = todo_list.pop(2)
print("You completed:", done_task)
print("Todo list after removal:", todo_list) 

#update an existing task

print(todo_list[1])
todo_list[1] = "Read a book"
#print("Updated to do list value:", todo_list[1])
print("Updated to do list value:", todo_list)

#print a task list 

print("Here's what you still need to do:")
for task in todo_list:
    print ("- ", task)