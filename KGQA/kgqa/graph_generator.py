import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd

from kgqa.gep import GetEntity


class GraphEnt:
    """
    This class is used to create a graph of the entities
    """

    def __init__(self):
        super(GraphEnt, self).__init__()
        self.x = GetEntity()

    def createGraph(self, dataEntities):
        entity_list = dataEntities.values.tolist()
        source, relations, target = [],[],[]

        for i in entity_list:
            source.append(i[0])
            relations.append(i[1])
            target.append(i[3])


        kg_df = pd.DataFrame({'source':source, 'target':target, 'edge':relations})
        G=nx.from_pandas_edgelist(kg_df, "source", "target", edge_attr=True, create_using=nx.MultiDiGraph())

        plt.figure(figsize=(12,12))
        pos = nx.spring_layout(G, k = 2) 
        nx.draw(G, with_labels=True, node_color='yellow', node_size=1000, edge_cmap=plt.cm.Blues, pos = pos)

        plt.show()

