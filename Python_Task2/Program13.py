class Inventory:
    def __init__(self):
        self.list={}
    def ADD(self,item,quan):
        if item in self.list:
            self.list[item]+=quan
            print(f'UPDATED item: {item}')
        else:
            self.list[item]=quan
    def DELETE(self,item,quan):
        if item not in self.list :
            print(f'{item} does not exist ')
        elif self.list[item]<quan:
            print(f'Not enough quantity; {item} has quantity of {self.list[item]}')
        else:
            self.list[item]-=quan
            print(f'{self.list[item]} of {item} is DELETED')
    def display(self):
        for i,q in self.list.items():
            print(i,q)


list=Inventory()
list.ADD('Cornflakes',20)
list.ADD('Honey',20)
list.ADD('Sausage',10)
list.ADD('Shampoo',30)

print('''
1)Add item
2)Delete item
3)Display list1
4)exit''')
ch=0
while(ch!=4):
    ch=int(input("\nEnter choice:"))
    if ch==1:
        item=input("Enter item:")
        quan=int(input("Enter Quantity:"))
        list.ADD(item,quan)
    elif ch==2:
        item=input("Enter item to delete:")
        quan=int(input("Enter Quantity to Delete:"))
        list.DELETE(item,quan)
    elif ch==3:
        list.display()
    elif ch==4:
        print('exit')
    else:
        print('Invalid Choice')
