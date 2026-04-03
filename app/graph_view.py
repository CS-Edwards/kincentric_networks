import streamlit as st
import json
from streamlit.components.v1 import html

def render_graph(G):
    nodes = [
        {
            "id": str(n),
            "label": G.nodes[n].get("label", str(n)),
            "size":10,
            "color":"#A020F0"  #TODO: expand sample to include generation levels, color map based on {"generation"}
        }
        for n in G.nodes()
    ]

    edges = [
        {"id":f"{u}-{v}", "source": str(u), "target": str(v)}
        for u,v in G.edges()
    ]

    graph_data = {"nodes":nodes, "edges": edges}

    print(f'generated graph: {graph_data}')

    # sigma.js
    html_code = f""" <!DOCTYPE html>
        <html>
        <head>
        <script src="https://unpkg.com/sigma@2/build/sigma.min.js"></script>
        <script src="https://unpkg.com/graphology"></script>
        <script src="https://unpkg.com/graphology-layout-forceatlas2"></script>
        <style>
            body {{ margin: 0; }}
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

        // Build graph
        const graph = new graphology.Graph();

        graphData.nodes.forEach(n => graph.addNode(n.id, n));
        graphData.edges.forEach(e => graph.addEdge(e.source, e.target, e));

        // Run layout
        const positions = graphologyLayoutForceatlas2.assign(graph, {{
        iterations: 100
        }});

        // Render
        const renderer = new sigma.Sigma(graph, document.getElementById("container"), {{
        renderLabels: true,
        }});

        </script>
        </body>
        </html>
"""

    html(html_code, height = 620)