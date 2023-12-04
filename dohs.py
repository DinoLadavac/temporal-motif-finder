import networkx as nx
import matplotlib.pyplot as plt

def ReverseListElement(edge):
    return [edge[1], edge[0], edge[2]]

def SameSourceSearch(first_edge, second_edge, matrix, delta, visited):
    for edges in matrix:
        motif = [first_edge,second_edge,edges]
        motif_sorted = sorted(motif, key=lambda x: x[-1])
        to_check = tuple(motif_sorted)
        triple = [first_edge, second_edge, edges]
        sorted_triple = sorted(triple, key = lambda x: x[-1])
        reversed_triplet=ReverseListElement(sorted_triple[2])
        #to_check = {frozenset(inner_list) for inner_list in motif}
        reversed_edge = ReverseListElement(edges)
        if (sorted_triple[2][2] - sorted_triple[0][2] <= delta) and (to_check not in visited) and (edges!=first_edge and edges!=second_edge):
            #print("Motifs: ", first_edge, second_edge, edges, visited)
            #print("to_check: ", to_check, "visited:", visited)
            visited.append(to_check)
            #print("Sorted Edges in Motif: ", sorted_triple)
            if sorted_triple[0][0] == sorted_triple[2][0] and sorted_triple[1][0] == sorted_triple[2][1] and sorted_triple[1][1] == sorted_triple[0][1]:
                #print("M13:", sorted_triple)
                M13.append(sorted_triple)
            elif sorted_triple[0][0] == sorted_triple[2][1] and sorted_triple[1][0] == sorted_triple[2][0] and sorted_triple[0][1] == sorted_triple[1][1]:
                #print("M14:", sorted_triple)
                M14.append(sorted_triple)
            elif sorted_triple[0][0] == sorted_triple[2][0] and sorted_triple[1][1] == sorted_triple[2][1] and sorted_triple[1][0] == sorted_triple[0][1] :
                #print("M23:", sorted_triple)
                M23.append(sorted_triple)  
            elif sorted_triple[0][1] == sorted_triple[2][1] and sorted_triple[1][0] == sorted_triple[2][0] and sorted_triple[1][1] == sorted_triple[0][0]:
                #print("M36:" ,sorted_triple)
                M36.append(sorted_triple)
            elif sorted_triple[0][1] == sorted_triple[2][0] and sorted_triple[1][1] == sorted_triple[2][1] and sorted_triple[0][0] == sorted_triple[1][0]:
                #print("M45:", sorted_triple)
                M45.append(sorted_triple)
            elif sorted_triple[0][1] == sorted_triple[2][1] and sorted_triple[1][1] == sorted_triple[2][0] and sorted_triple[0][0] == sorted_triple[1][0]:
                #print("M46: ", sorted_triple)
                M46.append(sorted_triple)
            elif sorted_triple[0][0:2] == sorted_triple[1][0:2] and sorted_triple[1][0:2]==sorted_triple[2][0:2]:
                #print("M61: ",sorted_triple)
                M61.append(sorted_triple)
            elif sorted_triple[0][0:2] == sorted_triple[1][0:2] and sorted_triple[1][0:2]==reversed_triplet[0:2]:
                #print("M62:",sorted_triple)
                M62.append(sorted_triple)

                    
def SourceFirstSearch(first_edge, second_edge, matrix, delta, visited):
    for edges in matrix:
        motif = [first_edge,second_edge,edges]
        motif_sorted = sorted(motif, key=lambda x: x[-1])
        sorted_triple = sorted(motif, key = lambda x: x[-1])
        to_check = tuple(motif_sorted)
        #to_check = {frozenset(inner_list) for inner_list in motif}
        if (sorted_triple[2][2] - sorted_triple[0][2] <= delta) and (edges!=first_edge and edges!=second_edge) and (to_check not in visited) and (sorted_triple[0][1]==sorted_triple[2][0] and sorted_triple[1][0]==sorted_triple[2][1]) and sorted_triple[1][1] == sorted_triple[0][0]:      
            #print(motif)
            visited.append(to_check)
            #print("M35:", motif)
            M35.append(motif)
        elif (sorted_triple[2][2] - sorted_triple[0][2] <= delta) and (edges!=first_edge and edges!=second_edge) and (to_check not in visited) and (sorted_triple[0][1]==sorted_triple[1][0] and sorted_triple[1][1]==sorted_triple[2][0]) and sorted_triple[2][0:2] == sorted_triple[0][0:2]:      
            #print(motif)
            visited.append(to_check)
            #print("M51:", motif)
            M51.append(motif)
        elif (sorted_triple[2][2] - sorted_triple[0][2] <= delta) and (edges!=first_edge and edges!=second_edge) and (to_check not in visited) and (sorted_triple[0][1]==sorted_triple[1][0] and sorted_triple[1][1]==sorted_triple[0][0]) and sorted_triple[2][0:2] == sorted_triple[1][0:2]:      
            #print(motif)
            visited.append(to_check)
            #print("M52:", motif)
            M52.append(motif)

            
def TargetFirstSearch(first_edge, second_edge, matrix, delta, visited):
    for edges in matrix:
        motif = [first_edge,second_edge,edges]
        motif_sorted = sorted(motif, key=lambda x: x[-1])
        sorted_triple = sorted(motif, key = lambda x: x[-1])
        to_check = tuple(motif_sorted)
        #to_check = {frozenset(inner_list) for inner_list in motif
        #print(motif,to_check)
        if (sorted_triple[2][2] - sorted_triple[0][2] <= delta) and (edges!=first_edge and edges!=second_edge) and (to_check not in visited) and (sorted_triple[0][0]==sorted_triple[2][1] and sorted_triple[1][1]==sorted_triple[2][0] and sorted_triple[0][1] == sorted_triple[1][0]):      
            #print(motif)
            visited.append(to_check)
            #print("M24:", motif)
            M24.append(motif)
                   
            
                

matx=[]
visited=[]
M13,M14,M23,M25,M36,M45,M46,M35,M24,M51,M52,M61,M62 = [], [], [], [], [], [], [], [], [], [], [], [], []
file_path = "example2.txt"
with open(file_path, 'r') as file:
    lines = file.readlines()


# net = nx.DiGraph()

for line in lines:
    row = [int(value) for value in line.strip().split()]
    matx.append(row)
    parts = line.split()
    if len(parts) == 3:
        net.add_edge(int(parts[0]), int(parts[1]), weight=float(parts[2]))

# plt.figure(figsize=(10, 10))  

# pos = nx.spring_layout(net, k=0.2)  

# labels = {node: str(node) for node in net.nodes()}
# edge_labels = {(i, j): f"{d['weight']:.2f}" for i, j, d in net.edges(data=True)} 

# nx.draw_networkx(net, pos, with_labels=True, labels=labels, font_color="black", node_color="white", width=1.5, node_size=200, font_weight='bold')
# nx.draw_networkx_edge_labels(net, pos, edge_labels=edge_labels, font_size=10)

# plt.axis('off')  
# #plt.show()


sorted_matrix = sorted(matx, key=lambda x: x[0])
#print(sorted_matrix)

# start = float(input("Timestamp starting time (seconds): "))
# stop = float(input("Timestamp end time (seconds): "))

delta = float(input("Delta (seconds): "))
for i in matx:
    for j in matx:
        if i!=j:
            #Same source
            if i[0] == j[0]:
                SameSourceSearch(i,j,matx,delta,visited)
            #Source of the first edge is the target of the second edge (M35)
            elif i[0]==j[1]:
                SourceFirstSearch(i,j,matx,delta,visited)
            #Target of the first edge is the source of the second edge (M24)
            elif i[1]==j[0]:
                TargetFirstSearch(i,j,matx,delta,visited)

print("M13: {}\nM14: {}\nM23: {}\nM24: {}\nM35: {}\nM36: {}\nM45: {}\nM46: {}\nM51: {}\nM52: {}\nM61: {}\nM62: {}".format(len(M13),len(M14),len(M23),len(M24),len(M35),len(M36),len(M45),len(M46),len(M51),len(M52),len(M61),len(M62)))

    
