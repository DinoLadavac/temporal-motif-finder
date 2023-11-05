import networkx as nx
import matplotlib.pyplot as plt

def ReverseListElement(edge):
    return [edge[1], edge[0], edge[2]]

def TriSearch(first_edge, second_edge, matrix, timestamp_start, timestap_stop, visited):
    for edges in matrix:
        motif = [first_edge,second_edge,edges]
        to_check = {frozenset(inner_list) for inner_list in motif}
        reversed_edge = ReverseListElement(edges)
        if (edges[2]>=timestamp_start and edges[2]<timestap_stop) and (to_check not in visited) and (edges!=first_edge and edges!=second_edge) and (((first_edge[1] == edges[0] and second_edge[1] == edges[1]) or (first_edge[0:2] == second_edge[0:2] and first_edge[0:2]==edges[0:2])) or (first_edge[0:2] == second_edge[0:2] and second_edge[0:2]==reversed_edge[0:2])):
                    #print("Motifs: ", first_edge, second_edge, edges, visited)
                    #print("to_check: ", to_check, "visited:", visited)
                    visited.append(to_check)
                    triple = [first_edge, second_edge, edges]
                    sorted_triple = sorted(triple, key = lambda x: x[-1])
                    reversed_triplet=ReverseListElement(sorted_triple[2])
                    #print("Sorted Edges in Motif: ", sorted_triple)
                    if sorted_triple[0][0] == sorted_triple[2][0] and sorted_triple[1][0] == sorted_triple[2][1]:
                        M13.append(sorted_triple)
                    elif sorted_triple[0][0] == sorted_triple[2][1] and sorted_triple[1][0] == sorted_triple[2][0]:
                        M14.append(sorted_triple)
                    elif sorted_triple[0][0] == sorted_triple[2][0] and sorted_triple[1][1] == sorted_triple[2][1] and sorted_triple[0][0:2] != sorted_triple[1][0:2]:
                        M23.append(sorted_triple)
                    elif sorted_triple[0][1] == sorted_triple[2][1] and sorted_triple[1][0] == sorted_triple[2][0] and sorted_triple[0][0:2] != sorted_triple[1][0:2]:
                        M36.append(sorted_triple)
                    elif sorted_triple[0][1] == sorted_triple[2][0] and sorted_triple[1][1] == sorted_triple[2][1]:
                        M45.append(sorted_triple)
                    elif sorted_triple[0][1] == sorted_triple[2][1] and sorted_triple[1][1] == sorted_triple[2][0]:
                        M46.append(sorted_triple)
                    elif sorted_triple[0][0:2] == sorted_triple[1][0:2] and sorted_triple[1][0:2]==sorted_triple[2][0:2]:
                        M61.append(sorted_triple)
                    elif sorted_triple[0][0:2] == sorted_triple[1][0:2] and sorted_triple[1][0:2]==reversed_triplet[0:2]:
                        M62.append(sorted_triple)
                    
def TriLoop1Search(first_edge, second_edge, matrix, timestamp_start, timestap_stop, visited):
    for edges in matrix:
        motif = [first_edge,second_edge,edges]
        to_check = {frozenset(inner_list) for inner_list in motif}
        if (edges[2]>=timestamp_start and edges[2]<timestap_stop) and (edges!=first_edge and edges!=second_edge) and (to_check not in visited) and (first_edge[1]==edges[0] and second_edge[0]==edges[1]):      
            #print(motif)
            visited.append(to_check)
            M35.append(motif)

            
def TriLoop2Search(first_edge, second_edge, matrix, timestamp_start, timestap_stop, visited):
    for edges in matrix:
        motif = [first_edge,second_edge,edges]
        to_check = {frozenset(inner_list) for inner_list in motif}
        if (edges[2]>=timestamp_start and edges[2]<timestap_stop) and (edges!=first_edge and edges!=second_edge) and (to_check not in visited) and (first_edge[0]==edges[1] and second_edge[1]==edges[0]):      
            #print(motif)
            visited.append(to_check)
            M24.append(motif)
                   
        # print(first_edge, second_edge, edges)
        # if (edges[2]>=timestamp_start and edges[2]<timestap_stop):
        #     print("Prosao je prvi test")
        #     if (edges!=first_edge and edges!=second_edge):
        #         print("Prosao je drugi test")
        #         if (to_check not in visited) :
        #             print("Prosao je test ponavljanja")
        #             if (first_edge[1] == edges[0] and second_edge[1] == edges[1]):
        #                 print("Prosao je prvi podtest")
        #                 visited.append(to_check)
        #             elif (first_edge[1] == edges[1] and second_edge[1] == edges[0]):
        #                 print("Prosao je drugi podtest")
        #                 visited.append(to_check)
        #             elif (first_edge[0] == edges[1] and second_edge[1] == edges[0]):
        #                 print("Prosao je treći podtest za loop")
        #                 visited.append(to_check)
            
                

matx=[]
visited=[]
M13,M14,M23,M36,M45,M46,M35,M24,M61, M62 = [], [], [], [], [], [], [], [], [], []
file_path = "example2.txt"
with open(file_path, 'r') as file:
    lines = file.readlines()


net = nx.DiGraph()

for line in lines:
    row = [int(value) for value in line.strip().split()]
    matx.append(row)
    parts = line.split()
    if len(parts) == 3:
        net.add_edge(int(parts[0]), int(parts[1]), weight=float(parts[2]))

plt.figure(figsize=(10, 10))  

pos = nx.spring_layout(net, k=0.2)  

labels = {node: str(node) for node in net.nodes()}
edge_labels = {(i, j): f"{d['weight']:.2f}" for i, j, d in net.edges(data=True)} 

nx.draw_networkx(net, pos, with_labels=True, labels=labels, font_color="black", node_color="white", width=1.5, node_size=200, font_weight='bold')
nx.draw_networkx_edge_labels(net, pos, edge_labels=edge_labels, font_size=10)

plt.axis('off')  
plt.show()


sorted_matrix = sorted(matx, key=lambda x: x[0])
#print(sorted_matrix)

start = float(input("Timestamp starting time (seconds): "))
stop = float(input("Timestamp end time (seconds): "))

for i in matx:
    if i[2]>= start and i[2]<stop:
        for j in matx:
            if j[2]>= start and j[2]<stop and i!=j:
                #Same source
                if i[0] == j[0]:
                    TriSearch(i,j,matx,start,stop,visited)
                #Source of the first edge is the target of the second edge (M35)
                elif i[0]==j[1]:
                    TriLoop1Search(i,j,matx,start,stop,visited)
                #Target of the first edge is the source of the second edge (M24)
                elif i[1]==j[0]:
                    TriLoop2Search(i,j,matx,start,stop,visited)

print("M13: {}\nM14: {}\nM23: {}\nM24: {}\nM35: {}\nM36: {}\nM45: {}\nM46: {}\nM61: {}\nM62: {}".format(len(M13),len(M14),len(M23),len(M24),len(M35),len(M36),len(M45),len(M46),len(M61),len(M62)))

    