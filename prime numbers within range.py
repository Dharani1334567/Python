start=int(input("enter:"))
end=int(input("enter:"))
for i in range(start,end+1):
    if i==1:
        print(i)
    elif i>1:
        for j in range(2,i):
            if i%j==0:
                break
            else:
                print(i)
                break
        

    
