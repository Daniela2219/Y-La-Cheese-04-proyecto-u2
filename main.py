print("Hello, what would you like to interact with?\n")
import ds_queue
import ds_stack
import ds_linkedlist

myQueue=ds_queue.Queue()
myStack=ds_stack.Stack()
mylinkedlist=ds_linkedlist.LinkedList()

checkmenu = True

 
def show_menu():
    print("1. Queue")
    print("2. Stack")
    print("3. Linked list")
    print("4. Exit")
    option = input("Enter which number you would like to realize\n")
    if option == "1" :
      show_menu_queue()
    elif option == "2":
      show_menu_stack()
    elif option == "3":
      show_menu_linkedlist()
    else:
      checkmenu = False
    



def show_menu_queue():
    global checkmenu
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Return")
    print("5. Exit")
    option = input("Enter which number you would like to realize\n")
    if option == "1":
      data = input("What element would you like to add\n")
      myQueue.enqueue(data)
    elif option == "2":
     myQueue.dequeue()
    elif option == "3":
     data = print(myQueue.peek())
    elif option == "4":
      show_menu()
    elif option == "5":
      checkmenu = False
      
    else:
      print("Invalid option, try again\n")
      
    if checkmenu:
      show_menu_queue()



def show_menu_stack():
     global checkmenu
     print("1 .Push")
     print("2. Pop")
     print("3. Peek")
     print("4. Return")
     print("5. Exit")
     option = input("Enter which number you would like to realize\n")
     if option == "1":
       data = input("What element would you like to push?\n")
       myStack.push(data)
     elif option == "2":
       myStack.pop()
     elif option == "3":
      print(myStack.peek())
     elif option == "4":
       show_menu()
     elif option == "5":
       checkmenu = False
     else: 
       print("Invalid option, try again\n")
    
     if checkmenu:
      show_menu_stack()


def show_menu_linkedlist():
     global checkmenu
     print("1. Insert at beginning")
     print("2. Insert at end")
     print("3. Insert after node")
     print("4. Delete node")
     print("5. Display") 
     print("6. Return")
     print("7. Exit")
     option = input("Enter which number you would like to realize\n")
     if option == "1":
       data = input("What element would you like to insert at the beginning?\n")
       mylinkedlist.insert_at_beginning(data)
     elif option == "2":
       data = input("What element would you like to insert at the end?\n")
       mylinkedlist.insert_at_end(data)
     elif option == "3":
       data = input("What element would you like to insert?\n")
       targetData = input("after what node?")
       mylinkedlist.insert_after_node(targetData,data)
     elif option == "4":
       data = input("What elemenet would you like to delete?\n")
       mylinkedlist.delete_node(data)
     elif option == "5":
       data = mylinkedlist.display()
     elif option == "6":
       show_menu()
     elif option == "7":
       checkmenu = False
     else: 
       print("Invalid option, try again\n")


     if checkmenu:
      show_menu_linkedlist()


while checkmenu:
   show_menu()


