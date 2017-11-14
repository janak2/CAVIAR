import csv
import networkx as nx

n = ['"1"','"3"','"5"','"6"','"8"','"11"','"12"','"16"','"17"','"33"','"76"','"77"','"80"','"82"','"83"','"84"','"85"','"86"','"87"','"88"','"89"','"96"','"106"']

with open("CAVIAR_Phases/a.txt",'w') as myfile:
	for k in range(1,12):
		g = nx.DiGraph()
		phase = []
		with open("CAVIAR_Phases/phase"+str(k)+".csv","rb") as csvfile:
			data = csv.reader(csvfile,delimiter=	' ',quotechar='|')
			for row in data:
				phase.append(row[0].split(","))
			g.add_nodes_from(phase[0][1:])
			for i in range(1,len(phase)):
				for j in range(1,len(phase[0])):
					if int(phase[i][j]) !=0:
						g.add_edge(phase[0][i],phase[0][j],weight=int(phase[i][j]))
		myfile.write("phase"+str(k)+"\n")
		h = nx.eigenvector_centrality(g)
		b = nx.betweenness_centrality(g)
		for i in n:
			if i in g.nodes():
				myfile.write("n"+i+"&"+str(g.degree(i))+"&"+str(round(h[i],3))+"&"+str(round(b[i],3))+"\\\\"+"\n")
		myfile.write("\n")