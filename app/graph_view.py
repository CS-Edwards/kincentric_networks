import streamlit as st
import json
from streamlit.components.v1 import html

def render_graph(G):
    nodes = [
        {
            "id": str(n),
            "label": G.nodes[n].get("label", str(n)),
            "size": 10,
            "color": "#A020F0"
        }
        for n in G.nodes()
    ]
    edges = [
        {"id": f"{u}-{v}", "source": str(u), "target": str(v)}
        for u, v in G.edges()
    ]
    graph_data = {"nodes": nodes, "edges": edges}

    html_code = f"""
    <html>
    <head>
      <script src="https://unpkg.com/graphology@0.25.4/dist/graphology.umd.min.js"></script>
      <script src="https://unpkg.com/sigma@2.4.0/build/sigma.min.js"></script>
      <style>
        body {{ margin: 0; padding: 0; }}
        #container {{
          width: 100%;
          height: 600px;
          background: #0f172a;
        }}
      </style>
    </head>
    <body>
      <div id="container"></div>
      <script>
        const graphData = {json.dumps(graph_data)};

        const graph = new graphology.Graph();

        graphData.nodes.forEach(n => {{
          graph.addNode(n.id, {{
            label: n.label,
            size: n.size,
            color: n.color,
            // Simple random layout — replace with FA2 if you add the layout CDN
            x: Math.random(),
            y: Math.random()
          }});
        }});

        graphData.edges.forEach(e => {{
          if (!graph.hasEdge(e.source, e.target)) {{
            graph.addEdge(e.source, e.target);
          }}
        }});

        const renderer = new Sigma(graph, document.getElementById("container"), {{
          renderLabels: true,
          defaultEdgeColor: "#888",
          defaultNodeColor: "#A020F0"
        }});
      </script>
    </body>
    </html>
    """
    html(html_code, height=620)