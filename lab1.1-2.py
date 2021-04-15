list=[] 
n=int(input("Enter the no.of integers:")) 
for i in range(0,n):
    list.append(int(input("Enter the integer:"))) 
print("Postive integers are") 
for i in list: 
    if(i>0): 
        print(i,end=" ")
