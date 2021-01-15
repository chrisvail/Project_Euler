from itertools import combinations

connections = 0

nodes = []
leaves = set()

with open("Problem107.txt", 'r', encoding = 'utf8') as file:
    for line in file:
        nodes.append([])
        line = (line.strip('\n')).split(',')
        for item in line:
            try:
                item = int(item)
            except ValueError:
                item = None
            
            nodes[-1].append(item)

loop = []

def main():
    
    global connections
    global loop

    start = 0
    for i in nodes:
        for j in i:
            if j is not None:
                start += j

    start = start // 2
    """ trim_leaves()

    for length in range(3, 5):

        for node_num in combinations(list(range(40)), 2):
            
            #node_list = [nodes[x] for x in node_num]
            if length == 3:
                test_tri(node_num)
                #trim_leaves(length)

            elif length == 4:
                test_quad(node_num)
                #trim_leaves(length)

        trim_leaves() """


    while connections != 39:
        loop = []
        find_loop()
        loop = loop[loop.index(loop[-1]):]
        dist = [nodes[loop[a]][loop[a + 1]] for a in range(len(loop) - 1)]
        
        
        try:
            index = dist.index(max(dist))
            
            nodes[loop[index]][loop[index + 1]] = None
            nodes[loop[index + 1]][loop[index]] = None
        except TypeError as e:
            print("Error loop:", loop)
            print("Error dist:", dist)
            
            #print(2, [x for x in enumerate(nodes[2]) if x[1] is not None])
            #print(3, [x for x in enumerate(nodes[3]) if x[1] is not None])
            #print(9, [x for x in enumerate(nodes[9]) if x[1] is not None])
            #print(26, [x for x in enumerate(nodes[26]) if x[1] is not None])

            #for i in nodes:
            #    print([x[0] for x in enumerate(i) if x[1] is not None])


            break
            

        trim_leaves(False)
    
    end = 0

    for i in nodes:
        for j in i:
            if j is not None:
                end += j
    
    end = end // 2

    print(start - end)

        

    

    #for index, i in enumerate(nodes):
    #    print(index, [x[0] for x in enumerate(i) if x[1] is not None and x[0] > index])


def trim_leaves(flag = True):

    global connections
    connections = 0
    for index, i in enumerate(nodes):
        
        #if sum([x is not None for x in i]) == 1:
        #    leaves.add(index)

        for j in i:
            if j is not None:
                connections += 1
            

    connections = connections // 2

    if flag:
        print("Connections: {} \tNon leaf: {}".format(connections, len(leaves)))

def test_tri(node_num):
    if nodes[node_num[0]][node_num[1]] is None:
        return
    
    else:
        for i in range(40):
            if nodes[node_num[0]][i] is not None and \
               nodes[node_num[1]][i] is not None:

                if nodes[node_num[0]][i] > nodes[node_num[1]][i] and \
                   nodes[node_num[0]][i] > nodes[node_num[0]][node_num[1]]:

                    #print("Removing link between {} and {}".format(node_num[0], i))
                    #print(nodes[node_num[0]][i], )
                    nodes[node_num[0]][i] = None
                    nodes[i][node_num[0]] = None 

                elif nodes[node_num[1]][i] > nodes[node_num[0]][i] and \
                     nodes[node_num[1]][i] > nodes[node_num[0]][node_num[1]]:
                    
                    #print("Removing link between {} and {}".format(node_num[1], i))
                    nodes[node_num[1]][i] = None
                    nodes[i][node_num[1]] = None 

                else:
                    
                    #print("Removing link between {} and {}".format(node_num[0], node_num[1]))
                    nodes[node_num[0]][node_num[1]] = None
                    nodes[node_num[1]][node_num[0]] = None

                break
        else:
            return

        test_tri(node_num)

def test_quad(node_num):
    if nodes[node_num[0]][node_num[1]] is None:
        possible = []

        for i in range(40):
            if nodes[node_num[0]][i] is not None and \
               nodes[node_num[1]][i] is not None:
               #print(nodes[node_num[0]][i], nodes[node_num[1]][i])
               #print()
               possible.append(i)

            if len(possible) == 2:

                #print(node_num)
                #print(nodes[node_num[0]][possible[0]])
                #print(nodes[node_num[1]][possible[0]])
                #print(nodes[node_num[0]][possible[1]])
                #print(nodes[node_num[1]][possible[1]])
                #print()

                if nodes[node_num[0]][possible[0]] > nodes[node_num[0]][possible[1]] and \
                   nodes[node_num[0]][possible[0]] > nodes[node_num[1]][possible[0]] and \
                   nodes[node_num[0]][possible[0]] > nodes[node_num[1]][possible[1]]:

                   nodes[node_num[0]][possible[0]] = None
                   nodes[possible[0]][node_num[0]] = None
                
                elif nodes[node_num[1]][possible[0]] > nodes[node_num[0]][possible[0]] and \
                     nodes[node_num[1]][possible[0]] > nodes[node_num[0]][possible[1]] and \
                     nodes[node_num[1]][possible[0]] > nodes[node_num[1]][possible[1]]:

                    nodes[node_num[1]][possible[0]] = None
                    nodes[possible[0]][node_num[1]] = None

                elif nodes[node_num[0]][possible[1]] > nodes[node_num[0]][possible[0]] and \
                     nodes[node_num[0]][possible[1]] > nodes[node_num[1]][possible[0]] and \
                     nodes[node_num[0]][possible[1]] > nodes[node_num[1]][possible[1]]:

                    nodes[node_num[0]][possible[1]] = None
                    nodes[possible[1]][node_num[0]] = None

                else:
                    
                    nodes[node_num[1]][possible[1]] = None
                    nodes[possible[1]][node_num[1]] = None

                break
            
        else:
            return

        test_quad(node_num)


def find_loop(node_num = 0, prev = -1):
    global loop

    if prev == -1:
        loop.append(0)
    
    
    for new_node in [x[0] for x in enumerate(nodes[node_num]) if x[1] is not None and x[0] != prev]:
    
        #print("Node: {}  \tNew Node: {}\tPossible Nodes: {}".format(node_num, new_node, loop))

        # exit condition
        if new_node in loop:
            loop.append(new_node)
            return True

        # loop[loop.index(new_node):]    
        # bury down 
        else:
            loop.append(new_node)

            if find_loop(new_node, node_num):
                return True
            else:
                loop = loop[:-1]

    return False


if __name__ == '__main__':
    main()