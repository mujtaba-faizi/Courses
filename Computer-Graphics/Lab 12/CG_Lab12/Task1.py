def bresenham(x1,y1,x2,y2,n):
    dx=x2-x1
    dy=y2-y1
    pk=(2*dy)-dx
    for a in range(n):
        if pk<0:
            if x1+1>x2:
                print("the between point lies outside the given range of points, because of greater specified n value")
                return
            print(x1+1,y1)
            x1+=1
            pk=pk+(2*dy)
        else:
            if x1+1>x2 or y1+1>y2:
                print("the between point lies outside the given range of points, because of greater specified n value")
                return
            print(x1+1,y1+1)
            x1+=1
            y1+=1
            pk=pk+((2*dy)-(2*dx))

x1 = input("Enter x1: ")
x2 = input("Enter y1: ")
y1 = input("Enter x2: ")
y2 = input("Enter y2: ")
n = input("Enter number of points inside the range to display(n): ")

bresenham(int(x1),int(x2),int(y1),int(y2),int(n))





