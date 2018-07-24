path=raw_input("Search through zero or limited steps? (Default limit 200 steps)\n>>> ")
input=map(int,raw_input("\nInput sequence (separate by space)\n>>> ").split(' '))
def ducci_search(input,steps=200):
    seq=input
    print("Start: {}".format(seq))

    for j in range(1,steps+1):
        temp=[]
        for i in range(0,len(seq)):
            if(i==len(seq)-1):
                temp.append(abs(seq[i]-seq[0]))
            else:
                temp.append(abs(seq[i]-seq[i+1]))
        seq=temp
        print("Step {}: {}".format(j,temp))
        if(seq==([0]*(len(seq)))):
            break
    print("\nCompleted {} steps".format(j))

if("steps" in path):
    path=path.split(' ')
    ducci_search(input,int(path[1]))
else:
    ducci_search(input)
