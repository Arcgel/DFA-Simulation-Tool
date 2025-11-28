# DFA Visualization Guide

## Overview

The DFA Visualizer provides a graphical interface for visualizing and testing Deterministic Finite Automata using PyQt5 and NetworkX.

## Installation

### Install Required Packages

```bash
pip install PyQt5 matplotlib networkx
```

Or use the requirements file:

```bash
pip install -r requirements.txt
```

## Running the Visualizer

### Full-Featured Visualizer

```bash
python dfa_visualizer.py
```

Features:
- Load DFA from JSON files
- Interactive string testing
- Step-by-step execution trace
- Path highlighting
- Complete DFA information display

### Simple Visualizer

```bash
python simple_visualizer.py
```

A minimal example showing basic visualization structure.

## Visual Elements

### State Representations

1. **Regular State**
   - Single circle
   - Light blue color
   - Standard node

2. **Start State**
   - Single circle
   - Light green color
   - Green arrow pointing to it with "start" label

3. **Final State (Accept State)**
   - Double circle (two concentric circles)
   - Light coral/red color
   - Indicates accepting states

4. **Start + Final State**
   - Double circle
   - Light green color
   - Has start arrow and double circle

### Transitions

- **Arrows**: Directed edges showing state transitions
- **Labels**: Symbols that trigger the transition
- **Multiple Symbols**: Grouped as "a,b" if multiple symbols lead to same transition
- **Self-loops**: Curved arrows for transitions back to same state

### Highlighting

- **Yellow nodes**: States visited during execution trace
- Shows the path taken when processing a string

## Using the Full Visualizer

### 1. Load a DFA

Click "Load DFA from JSON" and select a JSON file (e.g., `even_a_dfa.json`)

The visualization will display:
- All states as nodes
- All transitions as labeled edges
- Start state with green arrow
- Final states with double circles

### 2. Test Strings

1. Enter a string in the "Test String" field
2. Click "Test String" or press Enter
3. Result shows:
   - ✓ ACCEPTED (green) if string is accepted
   - ✗ REJECTED (red) if string is rejected

### 3. View Execution Trace

1. Enter a string to test
2. Click "Show Step-by-Step Trace"
3. The trace shows:
   - Initial state
   - Each transition step
   - Final result
4. The graph highlights the path taken (yellow nodes)

### 4. Clear Visualization

Click "Clear Visualization" to reset the display

## Code Structure

### Main Components

#### `DFACanvas` Class

```python
class DFACanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=8, height=6, dpi=100)
    def set_dfa(self, dfa)
    def highlight_path(self, states)
    def draw_dfa(self)
```

**Purpose**: Handles all graph drawing using NetworkX and Matplotlib

**Key Methods**:
- `set_dfa()`: Load a new DFA to visualize
- `highlight_path()`: Highlight states in execution path
- `draw_dfa()`: Main drawing logic

#### `DFAVisualizerWindow` Class

```python
class DFAVisualizerWindow(QMainWindow):
    def __init__(self)
    def init_ui(self)
    def load_dfa(self)
    def test_string(self)
    def show_trace(self)
    def clear_visualization(self)
```

**Purpose**: Main application window with controls

**Key Methods**:
- `load_dfa()`: File dialog to load JSON
- `test_string()`: Test input against DFA
- `show_trace()`: Display step-by-step execution
- `clear_visualization()`: Reset display

## Customization

### Changing Colors

Edit the `draw_dfa()` method in `DFACanvas`:

```python
# Regular states
node_color='lightblue'  # Change to any color

# Start state
node_color='lightgreen'  # Change start state color

# Final states
node_color='lightcoral'  # Change final state color
```

### Adjusting Layout

Change the layout algorithm:

```python
# Current: Spring layout
pos = nx.spring_layout(G, k=2, iterations=50, seed=42)

# Alternative: Circular layout
pos = nx.circular_layout(G)

# Alternative: Shell layout
pos = nx.shell_layout(G)

# Alternative: Kamada-Kawai layout
pos = nx.kamada_kawai_layout(G)
```

### Node Sizes

Adjust node sizes in `draw_dfa()`:

```python
# Regular nodes
node_size=800  # Increase for larger nodes

# Final states (outer circle)
node_size=1000  # Outer circle size

# Final states (inner circle)
node_size=800  # Inner circle size
```

### Arrow Styles

Modify arrow appearance:

```python
nx.draw_networkx_edges(G, pos,
    arrows=True,
    arrowsize=20,        # Arrow head size
    arrowstyle='->',     # Arrow style: '->', '-|>', '<->', etc.
    connectionstyle='arc3,rad=0.1',  # Curve amount
    edge_color='gray',   # Edge color
    width=2,             # Edge width
    ax=self.axes)
```

## Example Usage

### Visualizing Custom DFA

```python
from dfa import DFA
from dfa_visualizer import DFACanvas
import matplotlib.pyplot as plt

# Create custom DFA
states = {'q0', 'q1', 'q2'}
alphabet = {'a', 'b'}
transitions = {
    ('q0', 'a'): 'q1',
    ('q0', 'b'): 'q0',
    ('q1', 'a'): 'q2',
    ('q1', 'b'): 'q0',
    ('q2', 'a'): 'q2',
    ('q2', 'b'): 'q2',
}
start_state = 'q0'
final_states = {'q2'}

dfa = DFA(states, alphabet, transitions, start_state, final_states)

# Visualize
canvas = DFACanvas()
canvas.set_dfa(dfa)
plt.show()
```

### Programmatic Testing

```python
from dfa_visualizer import DFAVisualizerWindow
from PyQt5.QtWidgets import QApplication
import sys

app = QApplication(sys.argv)
window = DFAVisualizerWindow()

# Load DFA programmatically
from dfa import create_even_a_dfa
window.dfa = create_even_a_dfa()
window.canvas.set_dfa(window.dfa)

window.show()
sys.exit(app.exec_())
```

## Troubleshooting

### "No module named 'PyQt5'"

Install PyQt5:
```bash
pip install PyQt5
```

### "No module named 'networkx'"

Install NetworkX:
```bash
pip install networkx
```

### Graph Layout Issues

If the graph looks cluttered:
1. Try different layout algorithms (see Customization section)
2. Adjust the `k` parameter in spring_layout (higher = more spread out)
3. Increase figure size in `DFACanvas.__init__()`

### Slow Rendering

For large DFAs:
1. Reduce `iterations` in spring_layout
2. Use simpler layout like circular_layout
3. Reduce node sizes

## Advanced Features

### Custom Node Shapes

NetworkX supports different node shapes:

```python
nx.draw_networkx_nodes(G, pos,
    node_shape='o',  # 'o' circle, 's' square, '^' triangle, etc.
    node_color='lightblue',
    node_size=800,
    ax=self.axes)
```

### Edge Weights

Add visual weight to frequently used transitions:

```python
# Calculate edge weights based on usage
edge_weights = {edge: 1.0 for edge in G.edges()}

nx.draw_networkx_edges(G, pos,
    width=[edge_weights[e] * 2 for e in G.edges()],
    ax=self.axes)
```

### Interactive Features

Add click handlers:

```python
def on_click(event):
    # Handle node clicks
    pass

self.fig.canvas.mpl_connect('button_press_event', on_click)
```

## Tips

1. **Use descriptive state names** for better readability
2. **Keep DFAs small** (< 10 states) for best visualization
3. **Test with various strings** to understand DFA behavior
4. **Use trace feature** to debug unexpected results
5. **Export visualizations** using matplotlib's save feature

## Further Reading

- NetworkX Documentation: https://networkx.org/
- PyQt5 Documentation: https://www.riverbankcomputing.com/static/Docs/PyQt5/
- Matplotlib Documentation: https://matplotlib.org/
