import networkx as nx
import matplotlib.pyplot as plt

def TriSearch(first_edge, second_edge, matrix, timestamp_start, timestap_stop, visited):
    for edges in matrix:
        motif = [first_edge,second_edge,edges]
        to_check = {frozenset(inner_list) for inner_list in motif}
        #print("tu")
        if (edges[2]>=timestamp_start and edges[2]<timestap_stop) and (edges!=first_edge and edges!=second_edge) and ((first_edge[1] == edges[0] and second_edge[1] == edges[1])) and (to_check not in visited) :
                    print("Motif koji zadovoljava uvjet: ", first_edge, second_edge, edges)
                    visited.append(to_check)
                    triple = [first_edge, second_edge, edges]
                    sorted_triple = sorted(triple, key = lambda x: x[-1])
                    print("Veze sortirane prema redosljedu događanja: ", sorted_triple)
                    if sorted_triple[0][0] == sorted_triple[2][0] and sorted_triple[1][0] == sorted_triple[2][1]:
                        M13.append(sorted_triple)
                    elif sorted_triple[0][0] == sorted_triple[2][1] and sorted_triple[1][0] == sorted_triple[2][0]:
                        M14.append(sorted_triple)
                    elif sorted_triple[0][0] == sorted_triple[2][0] and sorted_triple[1][1] == sorted_triple[2][1]:
                        M23.append(sorted_triple)
                    elif sorted_triple[0][1] == sorted_triple[2][1] and sorted_triple[1][0] == sorted_triple[2][0]:
                        M36.append(sorted_triple)
                    elif sorted_triple[0][1] == sorted_triple[2][0] and sorted_triple[1][1] == sorted_triple[2][1]:
                        M45.append(sorted_triple)
                    elif sorted_triple[0][1] == sorted_triple[2][1] and sorted_triple[1][1] == sorted_triple[2][0]:
                        M46.append(sorted_triple)
                    
                   
                   
                   
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
M13,M14,M23,M36,M45,M46 = [], [], [], [], [], []
file_path = "example.txt"
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

start = float(input("Unesi pocetak odvijanja pretrazivanja (u sekundama): "))
stop = float(input("Unesi kraj odvijanja pretrazivanja (u sekundama): "))

for i in matx:
    if i[2]>= start and i[2]<stop:
        for j in matx:
            if j[2]>= start and j[2]<stop and i!=j:
                if i[0] == j[0]:
                    #print("Prije")
                    TriSearch(i,j,matx,start,stop,visited)

print("M13: {}\nM14: {}\nM23: {}\nM36: {}\nM45: {}\nM46: {}".format(len(M13),len(M14),len(M23),len(M36),len(M45),len(M46)))

    
# (first_edge[1] == edges[1] and second_edge[1] == edges[0]) or (first_edge[0] == edges[1] and second_edge[1] == edges[0])