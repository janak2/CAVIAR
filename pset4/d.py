import csv
import networkx as nx
import matplotlib.pyplot as plt

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
	plt.subplot(121)
	nx.draw_shell(g,with_labels=True,font_weight='bold',node_size=500,width = 0.5)
	plt.savefig("CAVIAR_Phases/phase"+str(k)+"d.png")