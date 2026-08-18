n=int(input("enter 0 to print trangular star pattern\nenter 1 to print reverse trangular star pattern"))
num=int(input("enter number of rows"))
if(n==0):
    print("trangular star pattern")
    for i in range(1,num,1):
        for j in range(1,i+1,1):
            print("* ", end=" ")
        print()
elif(n==1):
    print("reverse trangular star pattern")
    for i in range(num,1,-1):
        for j in range(1,i,1):
            print("* ", end=" ")
        print()