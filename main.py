matrix=['put your matrix here']
active_node=[]
start_node=[]
end_node=[]
forbidden_list={}
active_list={}
check_list=[]
one=1
calc=True
check=False
for x in range(23):
    for y in range(20):
        if matrix[y][x]=='*':
            active_node.append([x,y])
            start_node.append([x,y])
            forbidden_list = {(x,y): [0, 0, 0, [x,y]]}
        if matrix[y][x]=='@':
            end_node.append([x,y])
def path(dictionary,start_node,end_node):
    for i in dictionary:
        if i!=tuple(start_node[0]):
            if i==tuple(end_node[0]):
                print(i)
                end=[dictionary[i][3]]
                path(dictionary,start_node,end)
while one:
    if calc:
        for x in range(active_node[0][0]-1,active_node[0][0]+2):
            for y in range(active_node[0][1]-1,active_node[0][1]+2):
                try:
                    if not (x,y) in forbidden_list:
                        if matrix[y][x]=='@':
                            forbidden_list[(x,y)]=[0,0,0,active_node[0]]
                            path(forbidden_list,start_node,end_node)
                            one=False
                        else:
                            if matrix[y][x] != '1':
                                length0=forbidden_list[tuple(active_node[0])][1]
                                list1 = [abs(x - active_node[0][0]), abs(y - active_node[0][1])]
                                list1.sort()
                                length = list1[0] * 14 + (list1[1] - list1[0]) * 10
                                actual_length=length0+length
                                list2 = [abs(x - end_node[0][0]), abs(y - end_node[0][1])]
                                list2.sort()
                                length2 = list2[0] * 14 + (list2[1] - list2[0]) * 10
                                sum=actual_length+length2
                                if (x,y) in active_list:
                                    if actual_length<active_list[(x,y)][1]:
                                        active_list[(x, y)][0]=sum
                                        active_list[(x,y)][1]=actual_length
                                        active_list[(x, y)][3]=active_node[0]
                                    else:
                                        pass
                                else:
                                    active_list[(x, y)] = [sum,actual_length,length2, active_node[0]]
                except IndexError:
                    pass
        check=True
        calc=False
    if check:
        for i in active_list:
            check_list.append(active_list[i][0])
        check_list.sort()
        for i in active_list:
            if active_list[i][0]==check_list[0]:
                check_list.clear()
                forbidden_list[i]=active_list[i]
                active_node[0]=list(i)
                del active_list[i]
                calc=True
                check=False
                break

