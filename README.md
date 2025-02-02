# Classmate Relationship Graph with NetworkX  

## Overview  
This project visualizes relationships between classmates based on shared features using **NetworkX** and **Matplotlib**. The graph places me `"Adea"` at the center, connecting to classmates who share common features (`A`, `B`, or `C`). The strength of each connection is represented by edge thickness, based on the number of shared features.  

## Features  
- **Constructs an undirected graph** where nodes represent classmates.  
- **Uses shared features** (`A`, `B`, `C`) to determine connection strength.  
- **Customizes node sizes and colors**, with `"Adea"` highlighted in gold.  
- **Applies circular layout** for clear visualization.  

## Technologies Used  
- **Python**  
- **NetworkX** (for graph representation)  
- **Matplotlib** (for visualization)  

## How to Run  
1. Install the required libraries:  
   ```bash
   pip install matplotlib networkx
2. Run the script:
   ```bash
   python classmate_graph.py
3.  graph will be displayed showing "Adea" and the connections based on shared features.

## Visualization
The generated graph visually represents relationships among classmates, with:

- **Thicker edges** indicating stronger connections.
- **Larger nodes** for students with more shared features.
- **Adea highlighted in gold** to emphasize their central role.

## Future Improvements
- Include an interactive UI for exploring connections dynamically.
- Add support for additional relationship types beyond A, B, C.
- Implement real-world applications, such as networking analysis.
