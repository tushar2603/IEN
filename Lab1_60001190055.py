import random
from pyvis.network import Network
import webbrowser

print("Tushar Kumar\n 60001190055\nIEN LAB 1")

numberOfNodes = 26
numberOfNodes_1 = 10
numberOfNodes_2 = 6
numberOfNodes_3 = 10


listOfConnectedNodes = {}
listOfConnectedNodes_1 = {}
listOfConnectedNodes_2 = {}
listOfConnectedNodes_3 = {}

minConnection = 2
maxConnection = 3
maxLinkCost = 5

node_position = {}

def createGraph(num, start_num):
    global node_position, nt
    cornerNode = chr(random.randint(start_num, start_num + num - 1))
    graph = {}

    for i in range(num):
        graph[chr(start_num + i)] = {}

    mat = [[None]*3 for _ in range(3)]
    temp = list(graph.keys())
    temp.remove(cornerNode)

    for i in range(3):
        for j in range(3):
            ranNode = random.choice(temp)
            mat[i][j] = ranNode
            temp.remove(ranNode)

    temp = [(0,2),(1,2),(2,2)]
    temp.remove(random.choice(temp))
    for i in temp:
        ran = random.randint(1, 5)
        graph[cornerNode][mat[i[0]][i[1]]] = ran
        graph[mat[i[0]][i[1]]][cornerNode] = ran

    for k in range(3):
        for i in range(3):
            for j in range(3):
                if len(graph[mat[i][j]]) > k:
                    continue
                neighbour = showNeighbour(mat,(i,j),3)
                for l in neighbour.copy():
                    if len(graph[l]) > 2:
                        neighbour.remove(l)
                for m in graph[mat[i][j]]:
                    if m in neighbour:
                        neighbour.remove(m)

                if len(neighbour) == 0:
                    if k == 2:
                        continue
                    else:
                        neighbour = checkLeftConnection(graph,2,cornerNode)
                        neighbour.remove(mat[i][j])

                ranNode = random.choice(neighbour)
                ran = random.randint(1, 5)
                graph[ranNode][mat[i][j]] = ran
                graph[mat[i][j]][ranNode] = ran

    for i in range(3):
        for j in range(3):
            if start_num == 65:
                shift = 0
                mul = 1
                y1 = random.randint(200,600)
                node_position[cornerNode] = (900,y1)
                colour = "Red"
                nt.add_node(ord(cornerNode), label=cornerNode, font='30px', x=900, y=y1, color = colour)
            else:
                shift = 3000
                mul = -1
                y1 = random.randint(200, 600)
                node_position[cornerNode] = (shift - 900, y1)
                colour = "Green"
                nt.add_node(ord(cornerNode), label=cornerNode, font='30px', x=shift - 900, y=y1, color = colour)
            x1 = shift + mul*(j*300 + random.randint(0,200))
            y1 = i*300 + random.randint(0,200)
            node_position[mat[i][j]] = (x1, y1)
            nt.add_node(ord(mat[i][j]), label=mat[i][j], font='30px', x= x1 , y=y1, color = colour)


    for i in graph:
        for j in graph[i]:
            nt.add_edge(ord(i),ord(j) , color = colour, width = 3)
    return (cornerNode,graph)


def showNeighbour(mat,pos, limit):
    avail = []
    x_, y_, x, y = False, False, False, False

    if pos[0] - 1 >= 0:
        avail.append([pos[0] - 1, pos[1]])
        x_ = True
    if pos[1] - 1 >= 0:
        avail.append([pos[0], pos[1] - 1])
        y_ = True
    if pos[0] + 1 < limit:
        avail.append([pos[0] + 1, pos[1]])
        x = True
    if pos[1] + 1 < limit:
        y = True
        avail.append([pos[0], pos[1] + 1])
    if x_ and y_:
        avail.append([pos[0] - 1, pos[1] - 1])
    if x and y:
        avail.append([pos[0] + 1, pos[1] + 1])


    availNode = []
    for i in avail:
        availNode.append(mat[i[0]][i[1]])
    return availNode


def checkLeftConnection(graph,conn, cornerNode):
    left = []
    for i in graph:
        if len(i) < conn and i != cornerNode:
            left.append(i)
    return left

def middleArea(num, start_num):
    colour = "Blue"
    global node_position, nt
    graph = {}
    for i in range(num):
        graph[chr(start_num + i)] = {}
    temp = list(graph.keys())

    cornerNode1 = chr(random.randint(0,num-1) + start_num)
    temp.remove(cornerNode1)
    cornerNode2 = cornerNode1
    while cornerNode1 == cornerNode2:
        cornerNode2 = chr(random.randint(0, num - 1) + start_num)
    temp.remove(cornerNode2)


    y1 = random.randint(200, 600)
    node_position[cornerNode1] = (1100, y1)
    node_position[cornerNode2] = (1900, y1)
    nt.add_node(ord(cornerNode1), label=cornerNode1, font='30px', x=1100, y=y1, color = colour)
    nt.add_node(ord(cornerNode2), label=cornerNode2, font='30px', x=1900, y=y1, color = colour)



    mat = [[None] * 2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            ran_temp = random.choice(temp)
            mat[i][j] = ran_temp
            temp.remove(ran_temp)
            shift = 1250

            x1 = shift + (j * 300 + random.randint(0, 200))
            y1 = i * 400 + random.randint(0, 200)
            node_position[mat[i][j]] = (x1, y1)
            nt.add_node(ord(mat[i][j]), label=mat[i][j], font='30px', x=x1, y=y1, color = colour)

    ran = random.randint(1,5)
    graph[cornerNode1][mat[0][0]] = ran
    graph[mat[0][0]][cornerNode1] = ran
    nt.add_edge(ord(mat[0][0]), ord(cornerNode1) , color = colour, width = 3)

    ran = random.randint(1, 5)
    graph[cornerNode1][mat[1][0]] = ran
    graph[mat[1][0]][cornerNode1] = ran
    nt.add_edge(ord(mat[1][0]), ord(cornerNode1) , color = colour, width = 3)

    ran = random.randint(1, 5)
    graph[cornerNode2][mat[1][1]] = ran
    graph[mat[1][1]][cornerNode2] = ran
    nt.add_edge(ord(mat[1][1]), ord(cornerNode2) , color = colour, width = 3)

    ran = random.randint(1, 5)
    graph[cornerNode2][mat[0][1]] = ran
    graph[mat[0][1]][cornerNode2] = ran
    nt.add_edge(ord(mat[0][1]), ord(cornerNode2) , color = colour, width = 3)


    for k in range(3):
        for i in range(2):
            for j in range(2):
                if len(graph[mat[i][j]]) > k:
                    continue
                neighbour = showNeighbour(mat,(i,j),2)
                for l in neighbour.copy():
                    if len(graph[l]) > 2:
                        neighbour.remove(l)
                for m in graph[mat[i][j]]:
                    if m in neighbour:
                        neighbour.remove(m)

                if len(neighbour) == 0:
                    if k == 2:
                        continue
                    else:
                        neighbour = checkLeftConnection(graph,2,cornerNode)
                        neighbour.remove(mat[i][j])

                ranNode = random.choice(neighbour)
                ran = random.randint(1, 5)
                graph[ranNode][mat[i][j]] = ran
                graph[mat[i][j]][ranNode] = ran
                nt.add_edge(ord(ranNode),ord(mat[i][j]), color = colour, width = 3)
    return (cornerNode1,cornerNode2,graph)


def addAreaSeperation():
    global nt
    nt.add_node(1, label=None, size=1, x=1000, y=-200)
    nt.add_node(2, label=None, size=1, x=1000, y=1100)
    nt.add_edge(1, 2, color='Black')
    nt.add_node(3, label=None, size=1, x=2000, y=-200)
    nt.add_node(4, label=None, size=1, x=2000, y=1100)
    nt.add_edge(3, 4, color='Black')


nt = Network('900px','1800px', heading = "60001190055 - Tushar Kumar")
nt.toggle_physics(False)

(cor_area1,listOfConnectedNodes_1) = createGraph(numberOfNodes_1, 65)
(cor1_mid,cor2_mid,listOfConnectedNodes_2) = middleArea(6, 65+numberOfNodes_1)
(cor_area3,listOfConnectedNodes_3) = createGraph(numberOfNodes_1, 65+numberOfNodes_1+numberOfNodes_2)
addAreaSeperation()

listOfConnectedNodes.update(listOfConnectedNodes_1)
listOfConnectedNodes.update(listOfConnectedNodes_2)
listOfConnectedNodes.update(listOfConnectedNodes_3)

ran = random.randint(1,5)
listOfConnectedNodes[cor1_mid][cor_area1] = ran
listOfConnectedNodes[cor_area1][cor1_mid] = ran
nt.add_edge(ord(cor1_mid), ord(cor_area1), color = "Blue", width = 5)

ran = random.randint(1,5)
listOfConnectedNodes[cor2_mid][cor_area3] = ran
listOfConnectedNodes[cor_area3][cor2_mid] = ran
nt.add_edge(ord(cor2_mid), ord(cor_area3), color = "Blue", width = 5)

print("The Network: ")

nt.show('network.html')
webbrowser.open('network.html')

def dijkstra(startNode, listOfConnectedNodes):
    nodeWeightDict = {}
    nodeConnections = {}
    alternatePath = {}
    for node in listOfConnectedNodes:
        if node == startNode:
            nodeWeightDict[node] = 0
            nodeConnections[node] = [startNode]
            alternatePath[node] = [[startNode]]
        else:
            nodeWeightDict[node] = 999
            nodeConnections[node] = []
            alternatePath[node] = []

    nodeWeightDict_temp = nodeWeightDict.copy()

    while(len(nodeWeightDict_temp)>1):
        minWeightedNode = min(nodeWeightDict_temp, key=nodeWeightDict_temp.get)

        for node in listOfConnectedNodes[minWeightedNode]:
            if nodeWeightDict[node] > nodeWeightDict[minWeightedNode] + listOfConnectedNodes[minWeightedNode][node]:
                nodeWeightDict[node] = nodeWeightDict[minWeightedNode] + listOfConnectedNodes[minWeightedNode][node]
                nodeWeightDict_temp[node] = nodeWeightDict[minWeightedNode] + listOfConnectedNodes[minWeightedNode][node]
                nodeConnections[node] = nodeConnections[minWeightedNode] + [node]
                alternatePath[node] = [nodeConnections[node]]
            elif nodeWeightDict[node] == nodeWeightDict[minWeightedNode] + listOfConnectedNodes[minWeightedNode][node] and nodeConnections[minWeightedNode] + [node] not in alternatePath[node]:
                alternatePath[node].append(nodeConnections[minWeightedNode] + [node])

        nodeWeightDict_temp.pop(minWeightedNode)
    return alternatePath


def bellmanFord(startNode, listOfConnectedNodes, numberOfNodes):
    nodeWeightDict = {}
    nodeConnections = {}
    alternatePath = {}
    for node in listOfConnectedNodes:
        if node == startNode:
            nodeWeightDict[node] = 0
            nodeConnections[node] = [startNode]
            alternatePath[node] = [[startNode]]
        else:
            nodeWeightDict[node] = 999
            nodeConnections[node] = []
            alternatePath[node] = []

    for i in range(numberOfNodes-1):
        for nodes in listOfConnectedNodes:
            for node in listOfConnectedNodes[nodes]:
                if nodeWeightDict[node] > nodeWeightDict[nodes] + 1:
                    nodeWeightDict[node] = nodeWeightDict[nodes] + 1
                    nodeConnections[node] = nodeConnections[nodes] + [node]
                    alternatePath[node] = [nodeConnections[node]]
                elif nodeWeightDict[node] == nodeWeightDict[nodes] + 1 and nodeConnections[nodes] + [node] not in alternatePath[node]:
                    alternatePath[node].append(nodeConnections[nodes] + [node])

    return alternatePath

def pathFollow(path):
    global node_position, nt, listOfConnectedNodes
    for i in node_position:
        if i == path[0][0] or i == path[0][-1]:
            colour = "Silver"
        else:
            giv = False
            for j in path:
                if i in j:
                    colour = "Green"
                    giv = True
                elif not giv:
                    colour = "Black"
        nt.add_node(ord(i), label=i, font='30px', x=node_position[i][0], y=node_position[i][1], color = colour)

    addAreaSeperation()

    for i in range(len(path)):
        for j in range(len(path[i])):
            if j == 0:
                continue
            nt.add_edge(ord(path[i][j-1]), ord(path[i][j]), color="Green", width=10)

    for i in listOfConnectedNodes:
        for j in listOfConnectedNodes[i]:
            nt.add_edge(ord(i), ord(j), color="Black", width=3)


end = False

while True:
    print()
    valid = False
    while not valid:
        startNode = input("Enter the starting node: ").upper()
        if startNode == "END":
            end = True
            break
        if startNode in listOfConnectedNodes_2:
            print("Start node cannot be in middle area")
            continue
        if startNode not in listOfConnectedNodes:
            print("Enter a valid node")
            continue
        valid = True

    if end:
        break

    valid = False
    while not valid:
        endNode = input("Enter the ending node: ").upper()
        if endNode == "END":
            end = True
            break
        if endNode in listOfConnectedNodes_2:
            print("End node cannot be in middle area")
            continue
        if endNode not in listOfConnectedNodes:
            print("Enter a valid node")
            continue
        valid = True

    if end:
        break

    algorithm = input("Enter algorithm (DVR,LSR): ").upper()
    if algorithm == "END":
        end = True
        break
    if algorithm == 'DVR':
        shortestPath = bellmanFord(startNode,listOfConnectedNodes,numberOfNodes)
    else:
        shortestPath = dijkstra(startNode, listOfConnectedNodes)

    if end:
        break


    print("Shotest Path:", shortestPath[endNode])



    nt = Network('900px','1800px', heading = "60001190055")
    nt.toggle_physics(False)
    pathFollow(shortestPath[endNode])

    print("The shortest path is shown")
    nt.show("shortest.html")
    webbrowser.open('shortest.html')