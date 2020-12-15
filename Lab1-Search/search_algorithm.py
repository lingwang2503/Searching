import pygame
import graphUI
import math
from node_color import white, yellow, black, red, blue, purple, orange, green

"""
Feel free print graph, edges to console to get more understand input.
Do not change input parameters
Create new function/file if necessary
"""


def BFS(graph, edges, edge_id, start, goal):
    """
    BFS search
    """
    openQueue = [] #tập đỉnh kề đang mở
    path = [] #đường đi
    visitedQueue = [] #tập đỉnh đã thăm

    for i in graph: 
        path.append(-1)

    node = start
    graph[node][3]=orange #đỉnh start
    graphUI.updateUI()
    visitedQueue.append(node)

    while node != goal or len(openQueue) != 0:
        graph[node][3] = yellow #đỉnh đang duyệt
        graphUI.updateUI()
        for i in graph[node][1]:
            if i not in visitedQueue: #nếu đỉnh kề chưa có trong visited thì thêm đỉnh đó vào open và visited
                openQueue.append(i)
                visitedQueue.append(i)
                path[i] = node #lưu lại đỉnh trước đỉnh i
                edges[edge_id(node,i)][1] = white #tô màu cạnh kề
                graph[i][3] = red #tô màu đỉnh trong Queue
                graphUI.updateUI()

        graph[node][3] = blue #đỉnh đã duyệt qua
        graphUI.updateUI()
        
        node = openQueue.pop(0) #lấy khỏi open đỉnh đầu tiên để duyệt tiếp
        
        #nếu đỉnh đó là goal thì tô màu tím và dừng vòng lặp     
        if node == goal:
            graph[node][3] = purple
            graphUI.updateUI()
            break

    check = goal 
    graph[start][3] = orange #tô màu đỉnh Start
    graphUI.updateUI()

    #tô màu đường đi từ goal tói start 
    while check != start:
        edges[edge_id(path[check],check)][1] = green
        graphUI.updateUI()    
        check = path[check]
        if check == start:
            break        
    
    print("Implement BFS algorithm.")
    pass


def DFS(graph, edges, edge_id, start, goal):
    """
    DFS search
    """
    nodeStack = [] #tập đỉnh kề đang mở
    path = [] #đường đi
    visited = [] #tập đỉnh đã thăm

    for i in graph:
        path.append(-1)

    node = start
    visited.append(node)
    nodeStack.append(node)
    graph[node][3]=orange 
    graphUI.updateUI()
    
    while node != goal:                   
        find = False #đặt biến find để kiểm tra đỉnh kề,nếu đỉnh i có đỉnh kề chưa thăm thì find = True
        for i in graph[node][1]:         
            if i not in visited: 
                find = True 
                nodeStack.append(i)
                visited.append(i)
                path[i] = node #lưu đường đi
                edges[edge_id(node,i)][1] = white
                graph[i][3] = red 
                graphUI.updateUI()
                node = i #thay đỉnh đang duyệt thành đỉnh i, duyệt lại tập đỉnh kề của i
                graph[node][3] = yellow 
                graphUI.updateUI()
                break
                                
        if find == False: #nếu i không còn đỉnh kề chưa thăm thì pop đỉnh mới nhất trong stack ra để duyệt
            if len(nodeStack) == 0: 
                break
            node = nodeStack.pop()
                        
        graph[node][3] = blue 
        graphUI.updateUI()                    
        if node == goal:
            graph[node][3] = purple
            graphUI.updateUI()

    check = goal
    graph[start][3] = orange
    graphUI.updateUI()

    #tô màu đường đi từ goal tói start bằng list path
    while check != start:
        edges[edge_id(path[check],check)][1] = green
        graphUI.updateUI()    
        check = path[check]
        if check == start:
            break       

    print("Implement DFS algorithm.")
    pass


def UCS(graph, edges, edge_id, start, goal):
    """
    Uniform Cost Search search
    """
    nodeQueue = [] #tập đỉnh kề đang mở
    path = [] #đường đi
    visited = [] #tập đỉnh đã thăm
    cost = [] #chi phí
    
    for i in graph:
        cost.append([i,0])
        path.append(-1)

    node = start
    visited.append(node)
    graph[node][3]=orange 
    graphUI.updateUI()

    while node != goal:
 
        for i in graph[node][1]:
            if i not in visited:
                #cập nht65 chi phí từ đỉnh Start đến đỉnh con i
                cost[i][1]=cost[node][1] + math.sqrt(pow((graph[i][0][0] - graph[node][0][0]),2) + pow((graph[i][0][1] - graph[node][0][1]),2))
                if i not in nodeQueue:
                    nodeQueue.append(i)
                    path[i] = node
                edges[edge_id(node,i)][1] = white
                graph[i][3] = red 
                graphUI.updateUI()

        x = [] #xác định đỉnh có chi phí thấp nhất trong queue
        for i in nodeQueue:
            x.append(cost[i][1])
        minCost = min(x)

        for i in nodeQueue:
            if cost[i][1] == minCost: #lấy ra đỉnh có chi phí thấp nhất để duyệt tiếp             
                node = i
                nodeQueue.remove(i)
                visited.append(i)
                graph[node][3] = yellow 
                graphUI.updateUI()
                break

        graph[node][3] = blue 
        graphUI.updateUI()                    
        if node == goal:
            graph[node][3] = purple
            graphUI.updateUI()
            break

    check = goal
    graph[start][3] = orange
    graphUI.updateUI()

    #tô màu đường đi từ goal tói start bằng list path
    while check != start:
        edges[edge_id(path[check],check)][1] = green
        graphUI.updateUI()    
        check = path[check]
        if check == start:
            break       
    
    print("Implement Uniform Cost Search algorithm.")
    pass


def AStar(graph, edges, edge_id, start, goal):
    """
    A star search
    """
    nodeQueue = [] 
    path = []
    visited = [] 
    cost = []
    f = []
    
    for i in graph:
        cost.append([i,0])
        f.append([i,0])
        path.append(-1)

    node = start
    visited.append(node)
    graph[node][3]=orange 
    graphUI.updateUI()

    while node != goal:
        for i in graph[node][1]:
            if i not in visited:
                #cập nhật chi phí đường đi và f(n) của đỉnh i
                cost[i][1]=cost[node][1] + math.sqrt(pow((graph[i][0][0] - graph[node][0][0]),2) + pow((graph[i][0][1] - graph[node][0][1]),2))
                f[i][1] = cost[i][1] + math.sqrt(pow((graph[goal][0][0] - graph[i][0][0]),2) + pow((graph[goal][0][1] - graph[i][0][1]),2))
                if i not in nodeQueue:
                    nodeQueue.append(i)
                    path[i] = node
                edges[edge_id(node,i)][1] = white
                graph[i][3] = red 
                graphUI.updateUI()

        x = []
        for i in nodeQueue:
            x.append(f[i][1]) 
        minf = min(x) #lấy giá trị f(n) thấp nhất trong hàng đợi
                    
        for i in nodeQueue:
            if f[i][1] == minf:
                node = i #lấy ra khỏi hàng đợi đỉnh có f(n) thấp nhất để duyệt
                nodeQueue.remove(i)
                visited.append(i)
                graph[node][3] = yellow 
                graphUI.updateUI()
                break

        graph[node][3] = blue 
        graphUI.updateUI()                    
        if node == goal:
            graph[node][3] = purple
            graphUI.updateUI()
            break

    check = goal
    graph[start][3] = orange
    graphUI.updateUI()

    #tô màu đường đi từ goal tói start bằng list path
    while check != start:
        edges[edge_id(path[check],check)][1] = green
        graphUI.updateUI()    
        check = path[check]
        if check == start:
            break       
    print("Implement A* algorithm.")
    pass


def example_func(graph, edges, edge_id, start, goal):
    """
    This function is just show some basic feature that you can use your project.
    @param graph: list - contain information of graph (same value as global_graph)
                    list of object:
                     [0] : (x,y) coordinate in UI
                     [1] : adjacent node indexes
                     [2] : node edge color
                     [3] : node fill color
                Ex: graph = [
                                [
                                    (139, 140),             # position of node when draw on UI
                                    [1, 2],                 # list of adjacent node
                                    (100, 100, 100),        # grey - node edged color
                                    (0, 0, 0)               # black - node fill color
                                ],
                                [(312, 224), [0, 4, 2, 3], (100, 100, 100), (0, 0, 0)],
                                ...
                            ]
                It means this graph has Node 0 links to Node 1 and Node 2.
                Node 1 links to Node 0,2,3 and 4.
    @param edges: dict - dictionary of edge_id: [(n1,n2), color]. Ex: edges[edge_id(0,1)] = [(0,1), (0,0,0)] : set color
                    of edge from Node 0 to Node 1 is black.
    @param edge_id: id of each edge between two nodes. Ex: edge_id(0, 1) : id edge of two Node 0 and Node 1
    @param start: int - start vertices/node
    @param goal: int - vertices/node to search
    @return:
    """

    # Ex1: Set all edge from Node 1 to Adjacency node of Node 1 is green edges.
    node_1 = graph[1]
    for adjacency_node in node_1[1]:
        edges[edge_id(1, adjacency_node)][1] = green
    graphUI.updateUI()

    # Ex2: Set color of Node 2 is Red
    graph[2][3] = red
    graphUI.updateUI()

    # Ex3: Set all edge between node in a array.
    path = [4, 7, 9]  # -> set edge from 4-7, 7-9 is blue
    for i in range(len(path) - 1):
        edges[edge_id(path[i], path[i + 1])][1] = blue
    graphUI.updateUI()
