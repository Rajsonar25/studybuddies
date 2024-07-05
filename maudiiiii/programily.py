#DISPLAY I:
for i in range(0,6):
    for j in range(0,6):
        if((i==0)and (j>=0))or ((i==5)and (j>=0))or ((j==3)and(i>=0)):
            print("🧩",end="   ")
        else:
            print(" ",end="   ")
    print("\n")
#DISPLAY L:
for i in range(0,6):
    for j in range(0,6):
        if((i>=0)and (j==0))or ((i==5)and (j>=0)):
            print("🐭",end="   ")
        else:
            print(" ",end="   ")
    print("\n")
#DISPLAY Y:
for i in range(0,6):
    for j in range(0,7):
        if((j==3)and((i>=3)))or (((j==2)or(j==4))and (i==2))or (((j==1)or(j==5))and (i==1))or (((j==0)or(j==6))and (i==0)):
            print("🥹",end="   ")
        else:
            print(" ",end="   ")
    print("\n")
#DISPLAY <3heartssss:
for row in range(0,6):
    for col in range(0,7):
        if((row==0)and((col>0)and(col%3!=0)))or ((row==1)and(col%3==0))or (row-col==2)or (row+col==8):
            print("🩷",end="   ")
        else:
            print(" ",end="   ")
    print("\n")

