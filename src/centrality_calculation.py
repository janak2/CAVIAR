import csv
import networkx as nx

n = [1,3,5,6,8,11,12,16,17,33,76,77,80,82,83,84,85,86,87,88,89,96,106]

for k in range(1,12):
	g = nx.DiGraph()
	phase = []
	with open("CAVIAR_Phases/phase"+str(k)+".csv","rb") as myfile:
		data = csv.reader(myfile,delimiter=	' ',quotechar='|')
		for row in data:
			phase.append(row[0].split(","))
		g.add_nodes_from(phase[0][1:])
		for i in range(1,len(phase)):
			for j in range(1,len(phase[0])):
				if int(phase[i][j]) !=0:
					g.add_edge(phase[0][i],phase[0][j],weight=int(phase[i][j]))
	print g.edges()
	with open("CAVIAR_Phases/phase"+str(k)+"a.txt",'w') as myfile:
		myfile.write("degree\n")
		for i in phase[0][1:]:
			myfile.write(i + " "+ str(g.degree(i))+"\n")
		myfile.write("eigen\n")
		h = nx.eigenvector_centrality(g)
		for i in h:
			myfile.write(i+" "+str(h[i])+"\n")
		myfile.write("between\n")
		b = nx.betweenness_centrality(g)
		for i in b:
			myfile.write(i+" " +str(b[i])+"\n")	
		myfile.write("closeness\n")
		c  = nx.closeness_centrality(g)
		for i in c:
			myfile.write(i+" "+str(c[i])+"\n")