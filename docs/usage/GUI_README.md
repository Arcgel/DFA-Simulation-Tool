# DFA Visualizer - GUI Application

## Overview

A complete graphical user interface for visualizing and testing Deterministic Finite Automata (DFAs) built with PyQt5 and NetworkX.

## Features

### Visual Representation
- **Nodes (States)**: Clearly distinguished visual styles
  - Regular states: Blue single circles
  - Start state: Green circle with incoming arrow labeled "start"
  - Final states: Red/coral double circles (concentric circles)
  - Start+Final: Green double circles with start arrow

- **Edges (Transitions)**: Directed arrows with labels
  - Arrow direction shows transition flow
  - Labels show input symbols
  - Multiple symbols grouped (e.g., "a, b")
  - Curved edges for better visibility

- **Path Highlighting**: Yellow highlighting for execution traces

### Interactive Features
- Load DFA from JSON files
- Test strings interactively
- View step-by-step execution traces
- Real-time visualization updates
- Clear accept/reject feedback

## Installation

### Prerequisites

Python 3.7 or higher

### Install Dependencies

```bash
pip install PyQt5 matplotlib networkx
```

Or use the requirements file:

```bash
pip install -r requirements.txt
```

### Verify Installation

```bash
python -c "import PyQt5, matplotlib, networkx; print('All packages installed!')"
```

## Usage

### Running the Full Visualizer

```bash
python dfa_visualizer.py
```

### Running the Simple Example

```bash
python simple_visualizer.py
```

This shows a minimal working example with the even-a DFA.

## Application Structure

### Main Window Layout

```
┌─────────────────────────────────────────────────────────┐
│  DFA Visualizer                                         │
├──────────────┬──────────────────────────────────────────┤
│              │                                          │
│  Controls    │         Graph Visualization             │
│  Panel       │                                          │
│              │         (NetworkX + Matplotlib)          │
│  - Load DFA  │                                          │
│  - Test      │         Shows:                           │
│  - Trace     │         • States as nodes                │
│  - Info      │         • Transitions as edges           │
│              │         • Start arrow                    │
│              │         • Double circles for finals      │
│              │                                          │
└──────────────┴──────────────────────────────────────────┘
```

### Code Architecture

#### 1. DFACanvas Class
```python
class DFACanvas(FigureCanvasQTAgg):
    """Matplotlib canvas embedded in PyQt"""
    
    def set_dfa(self, dfa)
        # Load new DFA
    
    def highlight_path(self, states)
        # Highlight execution path
    
    def draw_dfa(self)
        # Main drawing logic
        # - Create NetworkX graph
        # - Apply layout algorithm
        # - Draw nodes with distinctions
        # - Draw edges with labels
        # - Add start arrow
```

#### 2. DFAVisualizerWindow Class
```python
class DFAVisualizerWindow(QMainWindow):
    """Main application window"""
    
    def init_ui(self)
        # Setup UI components
    
    def load_dfa(self)
        # File dialog + import
    
    def test_string(self)
        # Test input string
    
    def show_trace(self)
        # Display execution trace
```

## Visual Distinctions

### State Types

| State Type | Visual Style | Description |
|------------|--------------|-------------|
| Regular | Blue single circle | Standard state |
| Start | Green circle + arrow | Initial state with "start" arrow |
| Final | Red double circle | Accepting state (two circles) |
| Start+Final | Green double circle | Both start and accepting |

### Example Visual Representation

```
    start
      ↓
    (q0)  ──a──→  ((q1))
     ↑ ↓           ↑ ↓
     b  b          a  a
       ↓           ↓
      (q0)  ←──b── ((q1))

Legend:
(q0)   = Regular or start state (single circle)
((q1)) = Final state (double circle)
start↓ = Start arrow
──a──→ = Transition on symbol 'a'
```

## Key Implementation Details

### 1. Drawing States with Visual Distinctions

```python
# Regular states - single circle
nx.draw_networkx_nodes(G, pos, nodelist=regular_nodes,
                      node_color='lightblue', 
                      node_size=800)

# Final states - double circle (draw twice)
nx.draw_networkx_nodes(G, pos, nodelist=final_nodes,
                      node_color='lightcoral', 
                      node_size=1000)  # Outer circle
nx.draw_networkx_nodes(G, pos, nodelist=final_nodes,
                      node_color='lightcoral', 
                      node_size=800)   # Inner circle
```

### 2. Start State Arrow

```python
# Calculate arrow position
start_pos = pos[start_state]
arrow_start = (start_pos[0] - 0.15, start_pos[1] + 0.15)
arrow_end = (start_pos[0] - 0.05, start_pos[1] + 0.05)

# Draw arrow
axes.annotate('', xy=arrow_end, xytext=arrow_start,
             arrowprops=dict(arrowstyle='->', lw=2, color='green'))

# Add "start" label
axes.text(arrow_start[0] - 0.05, arrow_start[1] + 0.05,
         'start', fontsize=10, color='green', weight='bold')
```

### 3. Transition Edges

```python
# Draw directed edges
nx.draw_networkx_edges(G, pos,
                      edge_color='gray',
                      arrows=True,
                      arrowsize=20,
                      arrowstyle='->',
                      connectionstyle='arc3,rad=0.1')  # Curved edges

# Add edge labels (symbols)
nx.draw_networkx_edge_labels(G, pos, edge_labels, font_size=10)
```

### 4. Graph Layout

```python
# Spring layout - force-directed
pos = nx.spring_layout(G, k=2, iterations=50, seed=42)

# Parameters:
# k: optimal distance between nodes
# iterations: number of iterations
# seed: for reproducible layouts
```

## Workflow Example

### 1. Load DFA
```
User clicks "Load DFA from JSON"
  ↓
File dialog opens
  ↓
Select even_a_dfa.json
  ↓
DFA imported and validated
  ↓
Graph visualization updates
  ↓
Info panel shows DFA details
```

### 2. Test String
```
User enters "aba" in test field
  ↓
Clicks "Test String"
  ↓
is_accepted(dfa, "aba") called
  ↓
Result: ACCEPTED (green) or REJECTED (red)
  ↓
Display updates with result
```

### 3. Show Trace
```
User clicks "Show Step-by-Step Trace"
  ↓
trace_execution(dfa, "aba") called
  ↓
Each step displayed in trace panel
  ↓
Path highlighted in yellow on graph
  ↓
User sees state transitions visually
```

## Customization Guide

### Change Colors

Edit `draw_dfa()` method:

```python
# State colors
regular_color = 'lightblue'
start_color = 'lightgreen'
final_color = 'lightcoral'
highlight_color = 'yellow'

# Edge colors
edge_color = 'gray'
start_arrow_color = 'green'
```

### Change Layout Algorithm

```python
# Current: Spring layout
pos = nx.spring_layout(G, k=2, iterations=50, seed=42)

# Circular layout
pos = nx.circular_layout(G)

# Shell layout
pos = nx.shell_layout(G)

# Random layout
pos = nx.random_layout(G)

# Kamada-Kawai layout (force-directed)
pos = nx.kamada_kawai_layout(G)
```

### Adjust Node Sizes

```python
# Regular nodes
node_size = 800

# Final states outer circle
outer_size = 1000

# Final states inner circle
inner_size = 800

# Ratio for double circle: outer/inner ≈ 1.25
```

### Modify Arrow Styles

```python
# Arrow parameters
arrowsize = 20          # Size of arrow head
arrowstyle = '->'       # Style: '->', '-|>', '->>', etc.
connectionstyle = 'arc3,rad=0.1'  # Curve: rad=0 (straight) to rad=0.3 (curved)
width = 2               # Edge line width
```

## Troubleshooting

### Issue: Graph looks cluttered

**Solutions:**
1. Increase `k` parameter in spring_layout (more spacing)
2. Increase figure size in DFACanvas init
3. Try different layout algorithm
4. Reduce node sizes

### Issue: Self-loops not visible

**Solution:**
Increase `rad` in connectionstyle:
```python
connectionstyle='arc3,rad=0.3'  # More curved
```

### Issue: Edge labels overlap

**Solutions:**
1. Adjust layout parameters
2. Reduce font size
3. Use shorter symbol names
4. Manually adjust positions

### Issue: Start arrow not visible

**Solution:**
Adjust arrow position calculation:
```python
arrow_start = (start_pos[0] - 0.2, start_pos[1] + 0.2)  # Further away
```

## Advanced Features

### Export Visualization

Add to DFAVisualizerWindow:

```python
def export_image(self):
    filename, _ = QFileDialog.getSaveFileName(
        self, 'Export Image', '', 'PNG (*.png);;PDF (*.pdf)'
    )
    if filename:
        self.canvas.fig.savefig(filename, dpi=300, bbox_inches='tight')
```

### Zoom and Pan

Matplotlib canvas includes built-in zoom/pan:
- Zoom: Use mouse wheel or zoom button
- Pan: Click and drag with pan button

### Animation

Animate state transitions:

```python
from matplotlib.animation import FuncAnimation

def animate_trace(self, states):
    def update(frame):
        self.highlight_path(states[:frame+1])
    
    anim = FuncAnimation(self.canvas.fig, update, 
                        frames=len(states), interval=500)
    return anim
```

## Performance Tips

1. **Large DFAs**: Use simpler layouts (circular, shell)
2. **Many transitions**: Reduce iterations in spring_layout
3. **Frequent updates**: Cache layout positions
4. **High DPI displays**: Adjust dpi parameter

## Testing the Visualizer

### Manual Testing

1. Load `even_a_dfa.json`
2. Test strings: "", "a", "aa", "aaa"
3. Verify visual distinctions
4. Check trace functionality

### Automated Testing

```python
def test_visualization():
    from dfa import create_even_a_dfa
    
    app = QApplication([])
    window = DFAVisualizerWindow()
    
    # Load DFA
    window.dfa = create_even_a_dfa()
    window.canvas.set_dfa(window.dfa)
    
    # Test string
    window.test_input.setText("aa")
    window.test_string()
    
    # Verify result
    assert "ACCEPTED" in window.result_label.text()
    
    print("✓ Visualization test passed")
```

## Future Enhancements

Possible additions:
- [ ] DFA creation/editing in GUI
- [ ] Animation of string processing
- [ ] Multiple DFA comparison
- [ ] Export to various formats (SVG, PDF)
- [ ] Undo/redo for DFA modifications
- [ ] Zoom and pan controls
- [ ] State/transition tooltips
- [ ] Batch string testing
- [ ] DFA minimization visualization

## Resources

- **NetworkX Docs**: https://networkx.org/documentation/stable/
- **PyQt5 Tutorial**: https://www.riverbankcomputing.com/static/Docs/PyQt5/
- **Matplotlib Gallery**: https://matplotlib.org/stable/gallery/index.html

## Support

For issues or questions:
1. Check VISUALIZATION_GUIDE.md
2. Review example files
3. Check NetworkX/PyQt5 documentation
4. Verify all dependencies installed

## License

Same as main DFA Simulator project.
