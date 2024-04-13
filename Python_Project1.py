fname="suryansh.txt"

with open(fname,"w") as ipl:
    n=int(input("enter number of teams : "))
    
    for i in range(n):
        name=input("enter the name of team : ")
        matches=int(input("enter the number of matches : "))
        win=int(input("enter win : "))
        loss=int(input("enter loss: "))
        draw=int(input("enter draw : "))
        point=win*2+draw
        ipl.write(name+","+str(matches)+","+str(win)+","+str(loss)+","+str(draw)+","+str(point)+"\n")
        
with open(fname, 'r') as file:
    lines = file.readlines()

sorted_lines = sorted(lines, key=lambda x: -int(x.split(',')[5]))  

with open(fname, 'w') as file:
    for line in sorted_lines:
        file.write(line)

with open(fname,"r") as ipl:
    for i in ipl:
        l=[]
        l=i.split(",")
        print("\nteam name= ",l[0],"\tmatches",l[1],"\twin= ",l[2],"\tloss= ",l[3],"\tdraw= ",l[4],"\tpoints= ",l[5])

with open(fname,"r") as ipl:
    for i in ipl:
        n=1
        l=i.split(",")
        print("team",l[0],"rank",n)
        n=n+1