import pandas as pd
import networkx as nx

edges = pd.read_csv('network-test.csv')

G = nx.from_pandas_edgelist(edges,'source','target',create_using=nx.MultiDiGraph())

from pyvis.network import Network
pyvis_G = Network()
pyvis_G.from_nx(G)
#pyvis_G.enable_physics(True)  #html上でレイアウト動かしたくない場合false

#pyvis_G.show_buttons()   # 描画設定をGUIで変更する場合はコメントを外して、set_optionsをコメントアウトする

pyvis_G.set_options(
"""
var options = {
  "edges": {
    "arrows": {
      "to": {
        "enabled": true
      }
    },
    "color": {
      "inherit": true
    },
    "smooth": false
  },
  "physics": {
    "minVelocity": 0.75
  }
}
"""
)

pyvis_G.show("mygraph.html")
