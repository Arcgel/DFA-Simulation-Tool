# Interactive Step-by-Step DFA Debugger Guide

## Overview

The Interactive Debugger provides a visual, step-by-step execution environment for DFAs with real-time highlighting of states, transitions, and execution flow.

## Features

### Visual Highlighting

1. **Current State** (Gold with orange border)
   - The state currently being processed
   - Pulsing gold color for high visibility
   - Double circle if it's a final state

2. **Current Transition** (Red thick arrow)
   - The edge being traversed in current step
   - Highlighted in red with increased width
   - Shows the active transition

3. **Visited States** (Lighter blue)
   - States already visited in execution
   - Slightly faded to show history
   - Helps track execution path

4. **Symbol Display**
   - Shows current symbol being processed
   - Displayed in dedicated info panel
   - Updates with each step

### Interactive Controls

#### 1. Load DFA
- Click "📁 Load DFA from JSON"
- Select any DFA JSON file
- DFA information displayed immediately

#### 2. Enter Test String
- Type string in input field
- Click "▶ Run / Reset" to initialize
- Generates all execution steps

#### 3. Step Through Execution
- **⏭ Next Step**: Advance one step forward
- **⏮ Previous**: Go back one step
- **⏯ Auto Play**: Automatically step through (800ms intervals)

### Information Display

#### Current Step Panel
- **Step Counter**: Shows current step / total steps
- **Symbol**: Current symbol being read
- **Current State**: Active state in execution
- **Transition**: Shows state transition (from → to)
- **Processed**: Portion of string already processed
- **Remaining**: Portion of string yet to process

#### Execution Log
- Real-time log of all steps
- Shows transitions in format: "q0 → q1"
- Final result with accept/reject status

#### Result Display
- Green background: ACCEPTED ✓
- Red background: REJECTED ✗
- Shows final state information

## Usage Workflow

### Basic Workflow

```
1. Load DFA
   ↓
2. Enter test string
   ↓
3. Click "Run / Reset"
   ↓
4. Click "Next Step" repeatedly
   ↓
5. Observe:
   - Current state highlighted in gold
   - Transition edge highlighted in red
   - Symbol being processed
   - State changes
   ↓
6. Final result displayed
```

### Example Session

```
1. Load: even_a_dfa.json
2. Enter: "aba"
3. Click Run

Step 1: Initial
  - Current State: q0 (gold)
  - Symbol: [Initial]
  - Graph shows q0 highlighted

Step 2: Read 'a'
  - Current State: q0 (gold)
  - Transition: q0 → q1 (red arrow)
  - Symbol: 'a'
  - Processed: "a"
  - Remaining: "ba"

Step 3: Read 'b'
  - Current State: q1 (gold)
  - Transition: q1 → q1 (red arrow)
  - Symbol: 'b'
  - Processed: "ab"
  - Remaining: "a"

Step 4: Read 'a'
  - Current State: q1 (gold)
  - Transition: q1 → q0 (red arrow)
  - Symbol: 'a'
  - Processed: "aba"
  - Remaining: ""

Step 5: Final
  - Final State: q0 (gold)
  - Result: ACCEPTED ✓ (green)
```

## Visual Elements

### State Colors

| State Type | Color | Border | Description |
|------------|-------|--------|-------------|
| Regular | Light Blue | None | Standard state |
| Visited | Faded Blue | None | Already visited |
| Current | Gold | Orange (thick) | Active state |
| Start | Light Green | None | Initial state |
| Final | Light Coral | None | Accept state |

### Edge Colors

| Edge Type | Color | Width | Description |
|-----------|-------|-------|-------------|
| Regular | Gray | 1.5 | Standard transition |
| Current | Red | 4.0 | Active transition |

### Special Indicators

- **Start Arrow**: Green arrow pointing to start state
- **Double Circle**: Final/accept states
- **Edge Labels**: Transition symbols

## Code Structure

### InteractiveDFACanvas Class

```python
class InteractiveDFACanvas(FigureCanvasQTAgg):
    """Canvas with step highlighting capabilities."""
    
    def set_dfa(self, dfa)
        # Load DFA and prepare graph
    
    def highlight_step(self, current_state, previous_state, edge)
        # Highlight current execution step
        # - current_state: Gold highlighting
        # - edge: Red arrow highlighting
    
    def draw_dfa(self)
        # Redraw with current highlighting
```

### InteractiveDebuggerWindow Class

```python
class InteractiveDebuggerWindow(QMainWindow):
    """Main debugger window."""
    
    def run_debug(self)
        # Initialize debugging session
        # Generate all steps using trace_execution()
    
    def next_step(self)
        # Advance to next step
        # Update visualization and info
    
    def prev_step(self)
        # Go back to previous step
    
    def display_step(self)
        # Update all UI elements for current step
        # - Highlight state and edge
        # - Update info labels
        # - Append to log
```

## Key Implementation Details

### Step Highlighting

```python
def highlight_step(self, current_state, previous_state=None, edge=None):
    """Highlight current execution step."""
    self.current_state = current_state
    self.current_edge = edge
    
    # Track visited states
    if current_state not in self.all_visited_states:
        self.all_visited_states.append(current_state)
    
    # Redraw with highlighting
    self.draw_dfa()
```

### Current State Drawing

```python
# Draw current state with gold color and thick border
if self.current_state:
    nx.draw_networkx_nodes(G, pos, 
                          nodelist=[self.current_state],
                          node_color='gold',
                          node_size=1200,
                          linewidths=4,
                          edgecolors='orange')
```

### Current Edge Drawing

```python
# Draw current transition in red
if self.current_edge:
    nx.draw_networkx_edges(G, pos,
                          edgelist=[self.current_edge],
                          edge_color='red',
                          width=4,
                          arrows=True,
                          arrowsize=25)
```

### Step Information Update

```python
def display_step(self):
    """Update all UI for current step."""
    step = self.trace_steps[self.current_step_index]
    
    # Determine edge to highlight
    edge = None
    if step['symbol'] and step['next_state']:
        edge = (step['current_state'], step['next_state'])
    
    # Update visualization
    self.canvas.highlight_step(
        current_state=step['current_state'],
        edge=edge
    )
    
    # Update info labels
    self.symbol_label.setText(f"Symbol: '{step['symbol']}'")
    self.state_label.setText(f"Current State: {step['current_state']}")
    # ... more updates
```

## Advanced Features

### Auto-Play Mode

Automatically steps through execution with delays:

```python
def auto_play(self):
    """Auto-play through all steps."""
    def play_next():
        if self.current_step_index < len(self.trace_steps) - 1:
            self.next_step()
            QTimer.singleShot(800, play_next)  # 800ms delay
    
    play_next()
```

### Previous Step Navigation

Go backwards through execution:

```python
def prev_step(self):
    """Move to previous step."""
    if self.current_step_index > 0:
        self.current_step_index -= 1
        self.display_step()
```

### Execution Log

Real-time logging of all steps:

```python
# Log transition
self.log_output.append(
    f"Step {step['step_number']}: Read '{step['symbol']}' | "
    f"{step['current_state']} → {step['next_state']}"
)
```

## Customization

### Change Highlighting Colors

Edit `draw_dfa()` method:

```python
# Current state color
current_color = 'gold'
current_border = 'orange'

# Current edge color
edge_color = 'red'

# Visited state color
visited_color = '#b3d9ff'
```

### Adjust Auto-Play Speed

Edit `auto_play()` method:

```python
QTimer.singleShot(800, play_next)  # Change 800 to desired milliseconds
```

### Modify Step Display

Edit `display_step()` method to customize info panel content.

## Keyboard Shortcuts (Future Enhancement)

Potential additions:
- **Space**: Next step
- **Backspace**: Previous step
- **Enter**: Run/Reset
- **Escape**: Stop auto-play

## Troubleshooting

### Issue: Highlighting not visible

**Solution**: Check that colors have sufficient contrast:
```python
node_color='gold'  # High contrast
edgecolors='orange'  # Visible border
```

### Issue: Steps advance too fast in auto-play

**Solution**: Increase delay in `auto_play()`:
```python
QTimer.singleShot(1200, play_next)  # Slower
```

### Issue: Graph layout changes between steps

**Solution**: Layout is calculated once in `_prepare_graph()` and reused, ensuring consistency.

### Issue: Edge labels overlap

**Solution**: Adjust `connectionstyle` radius:
```python
connectionstyle='arc3,rad=0.15'  # More curved
```

## Comparison with Basic Visualizer

| Feature | Basic Visualizer | Interactive Debugger |
|---------|-----------------|---------------------|
| Load DFA | ✓ | ✓ |
| Test strings | ✓ | ✓ |
| View trace | ✓ (all at once) | ✓ (step-by-step) |
| Highlight current state | ✗ | ✓ (gold) |
| Highlight transition | ✗ | ✓ (red arrow) |
| Step forward | ✗ | ✓ |
| Step backward | ✗ | ✓ |
| Auto-play | ✗ | ✓ |
| Symbol display | ✗ | ✓ |
| Execution log | ✗ | ✓ |

## Best Practices

1. **Start Simple**: Begin with small DFAs (2-3 states)
2. **Use Short Strings**: Easier to follow step-by-step
3. **Watch Transitions**: Focus on red arrows showing transitions
4. **Check State Colors**: Gold = current, Blue = visited
5. **Read Log**: Execution log provides text summary
6. **Use Auto-Play**: Good for demonstrations
7. **Step Backward**: Review confusing transitions

## Example Use Cases

### 1. Learning DFA Execution
- Load simple DFA
- Enter short string
- Step through slowly
- Observe state changes

### 2. Debugging DFA Design
- Load your DFA
- Test edge cases
- Step through to find issues
- Identify incorrect transitions

### 3. Teaching Automata Theory
- Use auto-play for demonstrations
- Show students state transitions
- Highlight accept/reject behavior
- Visual learning aid

### 4. Verifying DFA Correctness
- Test multiple strings
- Step through each
- Verify expected behavior
- Confirm all transitions work

## Performance Notes

- **Step Generation**: All steps generated upfront using `trace_execution()`
- **Navigation**: O(1) for next/previous (array indexing)
- **Rendering**: Only redraws on step change
- **Memory**: Stores all steps in memory (O(n) where n = string length)

## Future Enhancements

Potential additions:
- [ ] Breakpoints on specific states
- [ ] Speed control for auto-play
- [ ] Export execution as video/GIF
- [ ] Keyboard shortcuts
- [ ] Step-over (skip to next state change)
- [ ] Execution history tree
- [ ] Compare two executions side-by-side
- [ ] Highlight multiple paths simultaneously

## Running the Debugger

### Command Line
```bash
python interactive_debugger.py
```

### From Python
```python
from interactive_debugger import InteractiveDebuggerWindow
from PyQt5.QtWidgets import QApplication
import sys

app = QApplication(sys.argv)
window = InteractiveDebuggerWindow()
window.show()
sys.exit(app.exec_())
```

## Summary

The Interactive Step-by-Step Debugger provides:

✅ **Visual State Highlighting**: Gold current state with orange border
✅ **Transition Highlighting**: Red arrows for active transitions
✅ **Symbol Display**: Shows current symbol being processed
✅ **Step Controls**: Next, Previous, Auto-play buttons
✅ **Information Panel**: Detailed step information
✅ **Execution Log**: Real-time logging
✅ **Result Display**: Clear accept/reject indication

Perfect for learning, teaching, debugging, and understanding DFA execution!
