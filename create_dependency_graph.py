import json
import networkx as nx
import matplotlib.pyplot as plt

# Load the CycloneDX SBOM in JSON format
with open('sbom-npm.json') as f:
    sbom = json.load(f)

# Create a directed graph
G = nx.DiGraph()

# Add nodes and edges based on dependencies
for component in sbom.get('components', []):
    component_name = component.get('name')
    G.add_node(component_name)
    for dependency in component.get('dependencies', []):
        G.add_edge(component_name, dependency)

# Create a layout
pos = nx.spring_layout(G)  # or nx.circular_layout(G)

# Draw the graph with adjustments
plt.figure(figsize=(15, 10))
nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue', font_size=8, font_weight='bold', arrows=True)
plt.title('Dependency Graph from SBOM')
plt.show()
