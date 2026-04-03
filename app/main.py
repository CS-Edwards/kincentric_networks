import streamlit as st
import sys
import os

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


from network.build import build_graph
from app.graph_view import render_graph

st.title("Ore-Graph: Sample Nuclear Kinship Network")

G = build_graph()

render_graph(G)