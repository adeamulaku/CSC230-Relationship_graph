import matplotlib.pyplot as plt
import networkx as nx


G = nx.Graph()


G.add_nodes_from(
    ["Moe", "AJ", "Dias",
    "Joseph", "Ryan", "Adrian", "Ronak", "Conner", "Haibin",
    "Rumeysa", "Sharanam", "Jermon", "Carlos", "Jaden",
    "Marcelo", "Arvind", "Francine", "Sean", "Antonio",
    "Simran", "Daejuan", "Singh", "Ananya", "Charlie",
    "Ricki", "Hashmat", "Enoch", "Ezeren", "Said",
    "Nate", "Adea","Shreya","Benji","Alessandro",
    "Ryan", "Kunj","Rahul","Sonam","John",
    "Charley","Janelle","Elijah","Jordan",
    "Jayden", "Tom", "Damon", "Kuanysh", "Jason",
    "Angel", "Homayoun"])


features = {
    "Moe": {"A"}, "AJ": {"A", "B"}, "Dias": set(),
    "Joseph": set(), "Ryan": set(), "Adrian": set(), "Ronak": set(),
    "Conner": set(), "Haibin": set(), "Rumeysa": set(), "Sharanam": set(),
    "Jermon": set(), "Carlos": set(), "Jaden": {"A", "B", "C"},
    "Marcelo": set(), "Arvind": set(), "Francine": set(), "Sean": set(),
    "Antonio": set(), "Simran": set(), "Daejuan": set(), "Singh": set(),
    "Ananya": set(), "Charlie": set(), "Ricki": set(), "Hashmat": set(),
    "Enoch": set(), "Ezeren": set(), "Said": set(), "Nate": set(),
    "Adea": {"A", "B", "C"}, "Shreya": set(), "Benji": set(),
    "Alessandro": set(), "Kunj": set(), "Rahul": set(), "Sonam": set(),
    "John": set(), "Charley": set(), "Janelle": set(), "Elijah": set(),
    "Jordan": set(), "Jayden": set(), "Tom": set(), "Damon": set(),
    "Kuanysh": set(), "Jason": set(), "Angel": set(), "Homayoun": set()
}

# Adding edges between me and other classmates based on shared features
for person in features:
    if person != "Adea":
        shared_features = features.get("Adea", set()) & features.get(person, set())
        weight = len(shared_features)
        G.add_edge("Adea", person, weight=weight)


pos = nx.circular_layout(G)


node_sizes = [
    3000 if node == "Adea" else 800 + 400 * len(features["Adea"] & features.get(node, set()))
    for node in G.nodes()
]

node_colors = ["gold" if node == "Adea" else "skyblue" for node in G.nodes()]


edge_weights = [G["Adea"][neighbor]["weight"] * 2 for neighbor in G.neighbors("Adea")]


plt.figure(figsize=(12, 12))
nx.draw(
    G, pos, with_labels=True, labels={node: node for node in G.nodes()},
    node_color=node_colors, node_size=node_sizes,
    font_color="black", font_family="Times New Roman",
    font_size=10, font_weight="bold", edge_color="gray",
    alpha=0.8, width=edge_weights
)

plt.title("Adea's Relationships w/ classmates Based on Shared Features")
plt.margins(0.2)
plt.show()
