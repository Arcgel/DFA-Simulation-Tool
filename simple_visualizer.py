"""
Simple DFA Visualizer - Minimal example showing basic structure
"""
import sys
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton

from dfa import create_even_a_dfa


class SimpleDFACanvas(FigureCanvasQTAgg):
    """Simple canvas for DFA visualization."""
    
    def __init__(self, parent=None):
        fig = Figure(figsize=(8, 6))
        self.axes = fig.add_subplot(111)
        super().__init__(fig)
        self.setParent(parent)
    
    def draw_dfa(self, dfa):
        """Draw DFA with visual distinctions for start and final states."""
        self.axes.clear()
        
        # Create directed graph
        G = nx.DiGraph()
        
        # Add nodes and edges
        for state in dfa.states:
            G.add_node(state)
        
        # Add edges with labels
        edge_labels = {}
        for (state, symbol), next_state in dfa.transitions.items():
            edge_key = (state, next_state)
            if edge_key in edge_labels:
                edge_labels[edge_key] += f",{symbol}"
            else:
                edge_labels[edge_key] = symbol
                G.add_edge(state, next_state)
        
        # Layout
        pos = nx.spring_layout(G, k=2, seed=42)
        
        # Separate node types
        regular = [n for n in G.nodes() 
                  if n != dfa.start_state and n not in dfa.final_states]
        start = [dfa.start_state] if dfa.start_state not in dfa.final_states else []
        final = [n for n in dfa.final_states if n != dfa.start_state]
        both = [n for n in dfa.final_states if n == dfa.start_state]
        
        # Draw nodes
        # Regular states - blue single circle
        if regular:
            nx.draw_networkx_nodes(G, pos, nodelist=regular,
                                  node_color='lightblue', node_size=800,
                                  ax=self.axes)
        
        # Start state - green single circle
        if start:
            nx.draw_networkx_nodes(G, pos, nodelist=start,
                                  node_color='lightgreen', node_size=800,
                                  ax=self.axes)
        
        # Final states - red double circle
        if final:
            nx.draw_networkx_nodes(G, pos, nodelist=final,
                                  node_color='lightcoral', node_size=1000,
                                  ax=self.axes)
            nx.draw_networkx_nodes(G, pos, nodelist=final,
                                  node_color='lightcoral', node_size=800,
                                  ax=self.axes)
        
        # Start + Final - green double circle
        if both:
            nx.draw_networkx_nodes(G, pos, nodelist=both,
                                  node_color='lightgreen', node_size=1000,
                                  ax=self.axes)
            nx.draw_networkx_nodes(G, pos, nodelist=both,
                                  node_color='lightgreen', node_size=800,
                                  ax=self.axes)
        
        # Draw edges
        nx.draw_networkx_edges(G, pos, edge_color='gray',
                              arrows=True, arrowsize=20,
                              arrowstyle='-|>',
                              connectionstyle='arc3,rad=0.15',
                              width=2, ax=self.axes,
                              min_source_margin=15, min_target_margin=15)
        
        # Draw labels
        nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold',
                               ax=self.axes)
        nx.draw_networkx_edge_labels(G, pos, edge_labels, font_size=10,
                                     ax=self.axes)
        
        # Arrow pointing to start state
        if dfa.start_state in pos:
            start_pos = pos[dfa.start_state]
            arrow_start = (start_pos[0] - 0.15, start_pos[1] + 0.15)
            arrow_end = (start_pos[0] - 0.05, start_pos[1] + 0.05)
            self.axes.annotate('', xy=arrow_end, xytext=arrow_start,
                             arrowprops=dict(arrowstyle='->', lw=2, color='green'))
            self.axes.text(arrow_start[0] - 0.05, arrow_start[1] + 0.05,
                          'start', fontsize=10, color='green', weight='bold')
        
        self.axes.set_title('DFA Visualization', fontsize=14, weight='bold')
        self.axes.axis('off')
        self.draw()


class SimpleWindow(QMainWindow):
    """Simple main window."""
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Simple DFA Visualizer')
        self.setGeometry(100, 100, 900, 700)
        
        # Central widget
        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout()
        central.setLayout(layout)
        
        # Canvas
        self.canvas = SimpleDFACanvas(self)
        layout.addWidget(self.canvas)
        
        # Button
        btn = QPushButton('Visualize DFA (Even number of a\'s)')
        btn.clicked.connect(self.visualize)
        layout.addWidget(btn)
        
        # Auto-visualize on start
        self.visualize()
    
    def visualize(self):
        """Visualize the example DFA."""
        dfa = create_even_a_dfa()
        self.canvas.draw_dfa(dfa)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SimpleWindow()
    window.show()
    sys.exit(app.exec_())
