def bresenham(r, n):
    r=int(r)
    n=int(n)-1
    x = 0
    y = r
    print(x,y," ",y,x," ",-x,y,"   ",y,-x," ",-x,-y,"  ",-y,-x," ",x,-y," ",-y,x)

    pk = (5 / 4) - int(r)
    for a in range(n):
        if pk < 0:
            if x+1>r:
                 print("the between point lies outside the given radius axis, because of greater specified n value")
                 return
            x += 1
            pk = pk + (2 * x) + 1
            print(x, y, " ", y, x, " ", -x, y, " ", y, -x, " ", -x, -y, " ", -y, -x, " ", x, -y, " ", -y, x)
        else:
            if x+1>r:
                 print("the between point lies outside the given range of points, because of greater specified n value")
                 return
            x += 1
            y -= 1
            pk = pk + (2 * x) + 1 - (2 * (y + 2))
            print(x, y, " ", y, x, " ", -x, y, " ", y, -x, " ", -x, -y, " ", -y, -x, " ", x, -y, " ", -y, x)

r = input("Enter radius: ")
n = input("Enter number of points inside the range to display(n): ")

bresenham(r, n)





