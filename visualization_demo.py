"""
Demonstration of DFA visualization without GUI
Creates static images showing different DFA visualizations
"""
import matplotlib.pyplot as plt
import networkx as nx
from dfa import create_even_a_dfa, DFA


def visualize_dfa_static(dfa, title="DFA Visualization", filename=None, highlight_path=None):
    """
    Create a static visualization of a DFA.
    
    Args:
        dfa: DFA object to visualize
        title: Title for the plot
        filename: If provided, save to this file
        highlight_path: List of states to highlight
    """
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Create graph
    G = nx.DiGraph()
    
    for state in dfa.states:
        G.add_node(state)
    
    # Add edges with labels
    edge_labels = {}
    for (state, symbol), next_state in dfa.transitions.items():
        edge_key = (state, next_state)
        if edge_key in edge_labels:
            edge_labels[edge_key] += f", {symbol}"
        else:
            edge_labels[edge_key] = symbol
            G.add_edge(state, next_state)
    
    # Layout
    pos = nx.spring_layout(G, k=2, iterations=50, seed=42)
    
    # Categorize nodes
    regular = [n for n in G.nodes() 
              if n != dfa.start_state and n not in dfa.final_states]
    start_only = [dfa.start_state] if dfa.start_state not in dfa.final_states else []
    final_only = [n for n in dfa.final_states if n != dfa.start_state]
    both = [n for n in dfa.final_states if n == dfa.start_state]
    
    # Apply highlighting
    if highlight_path:
        highlighted = [n for n in highlight_path if n in G.nodes()]
        regular = [n for n in regular if n not in highlighted]
        highlighted_regular = [n for n in highlighted if n in regular or n == dfa.start_state]
    else:
        highlighted_regular = []
    
    # Draw nodes
    if regular:
        nx.draw_networkx_nodes(G, pos, nodelist=regular,
                              node_color='lightblue', node_size=1200, ax=ax)
    
    if highlighted_regular:
        nx.draw_networkx_nodes(G, pos, nodelist=highlighted_regular,
                              node_color='yellow', node_size=1200, ax=ax)
    
    if start_only:
        nx.draw_networkx_nodes(G, pos, nodelist=start_only,
                              node_color='lightgreen', node_size=1200, ax=ax)
    
    if final_only:
        nx.draw_networkx_nodes(G, pos, nodelist=final_only,
                              node_color='lightcoral', node_size=1400, ax=ax)
        nx.draw_networkx_nodes(G, pos, nodelist=final_only,
                              node_color='lightcoral', node_size=1200, ax=ax)
    
    if both:
        nx.draw_networkx_nodes(G, pos, nodelist=both,
                              node_color='lightgreen', node_size=1400, ax=ax)
        nx.draw_networkx_nodes(G, pos, nodelist=both,
                              node_color='lightgreen', node_size=1200, ax=ax)
    
    # Draw edges
    nx.draw_networkx_edges(G, pos, edge_color='gray',
                          arrows=True, arrowsize=25,
                          arrowstyle='-|>', connectionstyle='arc3,rad=0.15',
                          width=2.5, ax=ax,
                          min_source_margin=15, min_target_margin=15)
    
    # Draw labels
    nx.draw_networkx_labels(G, pos, font_size=14, font_weight='bold', ax=ax)
    nx.draw_networkx_edge_labels(G, pos, edge_labels, font_size=12, ax=ax)
    
    # Start arrow
    if dfa.start_state in pos:
        start_pos = pos[dfa.start_state]
        arrow_start = (start_pos[0] - 0.15, start_pos[1] + 0.15)
        arrow_end = (start_pos[0] - 0.05, start_pos[1] + 0.05)
        ax.annotate('', xy=arrow_end, xytext=arrow_start,
                   arrowprops=dict(arrowstyle='->', lw=3, color='green'))
        ax.text(arrow_start[0] - 0.05, arrow_start[1] + 0.05,
               'start', fontsize=12, color='green', weight='bold')
    
    # Legend placed outside plot area to avoid overlap
    legend_elements = [
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='lightblue',
                  markersize=15, label='Regular State'),
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='lightgreen',
                  markersize=15, label='Start State'),
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='lightcoral',
                  markersize=18, label='Final State (double circle)'),
    ]
    ax.legend(handles=legend_elements, loc='upper left', bbox_to_anchor=(0, -0.05), 
             fontsize=10, framealpha=0.9, ncol=3)
    
    ax.set_title(title, fontsize=16, weight='bold', pad=20)
    ax.axis('off')
    
    plt.tight_layout()
    
    if filename:
        plt.savefig(filename, dpi=150, bbox_inches='tight')
        print(f"Saved visualization to {filename}")
    else:
        plt.show()
    
    plt.close()


def demo_visualizations():
    """Create demonstration visualizations."""
    print("Creating DFA visualizations...")
    print("=" * 60)
    
    # Example 1: Even number of a's
    print("\n1. DFA: Even number of 'a's")
    dfa1 = create_even_a_dfa()
    visualize_dfa_static(dfa1, 
                        "DFA: Accepts strings with even number of 'a's",
                        "viz_even_a.png")
    
    # Example 2: Strings ending with 'ab'
    print("\n2. DFA: Strings ending with 'ab'")
    states = {'q0', 'q1', 'q2'}
    alphabet = {'a', 'b'}
    transitions = {
        ('q0', 'a'): 'q1',
        ('q0', 'b'): 'q0',
        ('q1', 'a'): 'q1',
        ('q1', 'b'): 'q2',
        ('q2', 'a'): 'q1',
        ('q2', 'b'): 'q0',
    }
    dfa2 = DFA(states, alphabet, transitions, 'q0', {'q2'})
    visualize_dfa_static(dfa2,
                        "DFA: Accepts strings ending with 'ab'",
                        "viz_ends_ab.png")
    
    # Example 3: With highlighted path
    print("\n3. DFA with execution path highlighted")
    visualize_dfa_static(dfa1,
                        "DFA: Processing 'aba' (path highlighted)",
                        "viz_with_path.png",
                        highlight_path=['q0', 'q1', 'q1', 'q0'])
    
    # Example 4: Binary divisible by 3
    print("\n4. DFA: Binary numbers divisible by 3")
    states = {'q0', 'q1', 'q2'}
    alphabet = {'0', '1'}
    transitions = {
        ('q0', '0'): 'q0',
        ('q0', '1'): 'q1',
        ('q1', '0'): 'q2',
        ('q1', '1'): 'q0',
        ('q2', '0'): 'q1',
        ('q2', '1'): 'q2',
    }
    dfa3 = DFA(states, alphabet, transitions, 'q0', {'q0'})
    visualize_dfa_static(dfa3,
                        "DFA: Binary numbers divisible by 3",
                        "viz_div3.png")
    
    print("\n" + "=" * 60)
    print("All visualizations created successfully!")
    print("\nGenerated files:")
    print("  - viz_even_a.png")
    print("  - viz_ends_ab.png")
    print("  - viz_with_path.png")
    print("  - viz_div3.png")


if __name__ == '__main__':
    demo_visualizations()
