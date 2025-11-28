# DFA Simulator - System Architecture

## System Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                     DFA SIMULATOR SYSTEM                        │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ├─────────────────────────────────┐
                              │                                 │
                    ┌─────────▼─────────┐          ┌───────────▼──────────┐
                    │   CORE LAYER      │          │   GUI LAYER          │
                    │   (dfa.py)        │          │   (PyQt5)            │
                    └─────────┬─────────┘          └───────────┬──────────┘
                              │                                 │
        ┌─────────────────────┼─────────────────────┐          │
        │                     │                     │          │
┌───────▼────────┐  ┌────────▼────────┐  ┌────────▼────────┐  │
│ DFA Class      │  │ Simulation      │  │ Import/Export   │  │
│ • States       │  │ • is_accepted() │  │ • JSON Schema   │  │
│ • Alphabet     │  │ • trace_exec()  │  │ • Validation    │  │
│ • Transitions  │  │ • Validation    │  │ • File I/O      │  │
│ • Start/Final  │  └─────────────────┘  └─────────────────┘  │
└────────────────┘                                             │
                                                               │
                              ┌────────────────────────────────┘
                              │
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
┌───────▼────────┐  ┌────────▼────────┐  ┌────────▼────────────┐
│ Basic          │  │ Interactive     │  │ Simple              │
│ Visualizer     │  │ Debugger        │  │ Visualizer          │
│ • Load DFA     │  │ • Step Forward  │  │ • Minimal           │
│ • Test String  │  │ • Step Back     │  │ • Example           │
│ • View Trace   │  │ • Auto-play     │  │ • Demo              │
│ • Graph View   │  │ • Highlighting  │  └─────────────────────┘
└────────────────┘  └─────────────────┘
```

## Core Layer Architecture

```
┌──────────────────────────────────────────────────────────┐
│                      DFA Class                           │
├──────────────────────────────────────────────────────────┤
│  Properties:                                             │
│  • states: Set[str]                                      │
│  • alphabet: Set[str]                                    │
│  • transitions: Dict[(str, str), str]                    │
│  • start_state: str                                      │
│  • final_states: Set[str]                                │
├──────────────────────────────────────────────────────────┤
│  Methods:                                                │
│  • __init__(...)           - Initialize and validate     │
│  • _validate()             - Check DFA correctness       │
│  • process(string)         - Test acceptance             │
│  • process_with_trace()    - Get state sequence          │
└──────────────────────────────────────────────────────────┘
                              │
                              │ uses
                              ▼
┌──────────────────────────────────────────────────────────┐
│              Simulation Functions                        │
├──────────────────────────────────────────────────────────┤
│  is_accepted(dfa, string) → bool                         │
│  • Processes string symbol by symbol                     │
│  • Returns True if accepted                              │
│  • Validates input symbols                               │
├──────────────────────────────────────────────────────────┤
│  trace_execution(dfa, string) → Generator[Dict]          │
│  • Yields step-by-step execution info                    │
│  • Each step contains:                                   │
│    - step_number                                         │
│    - symbol                                              │
│    - current_state                                       │
│    - next_state                                          │
│    - processed_input                                     │
│    - remaining_input                                     │
│    - is_final_step                                       │
│    - accepted (final step only)                          │
└──────────────────────────────────────────────────────────┘
                              │
                              │ uses
                              ▼
┌──────────────────────────────────────────────────────────┐
│            Import/Export Functions                       │
├──────────────────────────────────────────────────────────┤
│  export_dfa_to_json(dfa, filename)                       │
│  • Converts DFA to JSON dict                             │
│  • Writes to file with formatting                        │
│  • Handles I/O errors                                    │
├──────────────────────────────────────────────────────────┤
│  import_dfa_from_json(filename) → DFA                    │
│  • Reads JSON file                                       │
│  • Validates structure                                   │
│  • Creates DFA object                                    │
│  • Returns validated DFA                                 │
└──────────────────────────────────────────────────────────┘
```

## Interactive Debugger Architecture

```
┌─────────────────────────────────────────────────────────────┐
│           InteractiveDebuggerWindow (QMainWindow)           │
├─────────────────────────────────────────────────────────────┤
│  State:                                                     │
│  • dfa: DFA                    - Loaded DFA                 │
│  • trace_steps: List[Dict]     - All execution steps        │
│  • current_step_index: int     - Current position           │
├─────────────────────────────────────────────────────────────┤
│  UI Components:                                             │
│  • input_field: QLineEdit      - Test string input          │
│  • step_btn: QPushButton       - Next step button           │
│  • prev_btn: QPushButton       - Previous step button       │
│  • auto_btn: QPushButton       - Auto-play button           │
│  • canvas: InteractiveDFACanvas - Graph visualization       │
│  • info_labels: QLabel[]       - Step information           │
│  • log_output: QTextEdit       - Execution log              │
├─────────────────────────────────────────────────────────────┤
│  Methods:                                                   │
│  • load_dfa()                  - Load from JSON             │
│  • run_debug()                 - Initialize session         │
│  • next_step()                 - Advance forward            │
│  • prev_step()                 - Go backward                │
│  • display_step()              - Update UI                  │
│  • auto_play()                 - Automatic stepping         │
└─────────────────────────────────────────────────────────────┘
                              │
                              │ contains
                              ▼
┌─────────────────────────────────────────────────────────────┐
│        InteractiveDFACanvas (FigureCanvasQTAgg)             │
├─────────────────────────────────────────────────────────────┤
│  State:                                                     │
│  • dfa: DFA                    - DFA to visualize           │
│  • graph: nx.DiGraph           - NetworkX graph             │
│  • pos: Dict                   - Node positions (cached)    │
│  • current_state: str          - Gold highlighted           │
│  • current_edge: Tuple         - Red highlighted            │
│  • all_visited_states: List    - Faded blue                 │
├─────────────────────────────────────────────────────────────┤
│  Methods:                                                   │
│  • set_dfa(dfa)                - Load DFA                   │
│  • highlight_step(...)         - Update highlighting        │
│  • draw_dfa()                  - Render graph               │
│  • _prepare_graph()            - Build NetworkX graph       │
└─────────────────────────────────────────────────────────────┘
```

## Data Flow - Step-by-Step Execution

```
┌─────────────┐
│ User Action │
└──────┬──────┘
       │
       ▼
┌─────────────────────────────────────┐
│ 1. Load DFA from JSON               │
│    import_dfa_from_json(filename)   │
└──────┬──────────────────────────────┘
       │
       ▼
┌─────────────────────────────────────┐
│ 2. Enter Test String                │
│    input_field.text()               │
└──────┬──────────────────────────────┘
       │
       ▼
┌─────────────────────────────────────┐
│ 3. Click "Run"                      │
│    run_debug()                      │
└──────┬──────────────────────────────┘
       │
       ▼
┌─────────────────────────────────────┐
│ 4. Generate All Steps               │
│    trace_steps = list(              │
│      trace_execution(dfa, string)   │
│    )                                │
└──────┬──────────────────────────────┘
       │
       ▼
┌─────────────────────────────────────┐
│ 5. Click "Next Step"                │
│    next_step()                      │
└──────┬──────────────────────────────┘
       │
       ▼
┌─────────────────────────────────────┐
│ 6. Get Current Step                 │
│    step = trace_steps[index]        │
└──────┬──────────────────────────────┘
       │
       ├──────────────────────────────┐
       │                              │
       ▼                              ▼
┌──────────────────┐      ┌──────────────────────┐
│ 7a. Update Graph │      │ 7b. Update Info      │
│ highlight_step() │      │ • Symbol label       │
│ • Gold state     │      │ • State label        │
│ • Red edge       │      │ • Transition label   │
│ • Redraw         │      │ • Processed/remain   │
└──────────────────┘      └──────────────────────┘
       │                              │
       └──────────────┬───────────────┘
                      │
                      ▼
            ┌─────────────────┐
            │ 8. Update Log   │
            │ Append step info│
            └─────────────────┘
                      │
                      ▼
            ┌─────────────────┐
            │ 9. User Sees:   │
            │ • Gold state    │
            │ • Red edge      │
            │ • Symbol info   │
            │ • Log entry     │
            └─────────────────┘
```

## Visual Highlighting System

```
┌────────────────────────────────────────────────────────┐
│              Highlighting State Machine                │
└────────────────────────────────────────────────────────┘

State Types:
┌──────────────┬─────────────┬──────────┬─────────────┐
│ State Type   │ Color       │ Border   │ Size        │
├──────────────┼─────────────┼──────────┼─────────────┤
│ Regular      │ Light Blue  │ None     │ 1000        │
│ Visited      │ Faded Blue  │ None     │ 1000        │
│ Current      │ Gold        │ Orange 4 │ 1200        │
│ Start        │ Light Green │ None     │ 1000        │
│ Final        │ Light Coral │ None     │ 1200/1000   │
└──────────────┴─────────────┴──────────┴─────────────┘

Edge Types:
┌──────────────┬─────────────┬──────────┬─────────────┐
│ Edge Type    │ Color       │ Width    │ Arrow Size  │
├──────────────┼─────────────┼──────────┼─────────────┤
│ Regular      │ Gray        │ 1.5      │ 20          │
│ Current      │ Red         │ 4.0      │ 25          │
└──────────────┴─────────────┴──────────┴─────────────┘

Highlighting Logic:
┌─────────────────────────────────────────────────────┐
│ For each step:                                      │
│                                                     │
│ 1. Determine current_state                         │
│    → Draw with gold + orange border                │
│                                                     │
│ 2. Determine current_edge (from, to)               │
│    → Draw with red + thick width                   │
│                                                     │
│ 3. Track visited_states                            │
│    → Draw with faded blue                          │
│                                                     │
│ 4. Redraw entire graph                             │
│    → All elements updated                          │
└─────────────────────────────────────────────────────┘
```

## JSON Schema Structure

```
┌─────────────────────────────────────────────────────┐
│                  JSON DFA Format                    │
├─────────────────────────────────────────────────────┤
│ {                                                   │
│   "states": ["q0", "q1", ...],                      │
│   "alphabet": ["a", "b", ...],                      │
│   "transitions": {                                  │
│     "q0,a": "q1",      ← Format: "state,symbol"     │
│     "q0,b": "q0",                                   │
│     ...                                             │
│   },                                                │
│   "start_state": "q0",                              │
│   "final_states": ["q0", ...]                       │
│ }                                                   │
└─────────────────────────────────────────────────────┘
                      │
                      │ Validation
                      ▼
┌─────────────────────────────────────────────────────┐
│              Validation Checks                      │
├─────────────────────────────────────────────────────┤
│ ✓ All required fields present                       │
│ ✓ Correct data types                                │
│ ✓ start_state in states                             │
│ ✓ final_states ⊆ states                             │
│ ✓ Transition function complete                      │
│ ✓ All transition states valid                       │
│ ✓ All transition symbols in alphabet                │
└─────────────────────────────────────────────────────┘
```

## Component Dependencies

```
┌─────────────────────────────────────────────────────┐
│                 Dependency Graph                    │
└─────────────────────────────────────────────────────┘

Python Standard Library
    │
    ├─→ json (import/export)
    ├─→ sys (application)
    └─→ typing (type hints)

External Libraries
    │
    ├─→ PyQt5
    │   ├─→ QtWidgets (UI components)
    │   └─→ QtCore (signals, timers)
    │
    ├─→ matplotlib
    │   ├─→ pyplot (plotting)
    │   ├─→ Figure (canvas)
    │   └─→ FigureCanvasQTAgg (Qt integration)
    │
    └─→ networkx
        ├─→ DiGraph (directed graph)
        ├─→ draw_networkx_* (rendering)
        └─→ spring_layout (positioning)

Project Modules
    │
    ├─→ dfa.py (core)
    │   ├─→ DFA class
    │   ├─→ is_accepted()
    │   ├─→ trace_execution()
    │   ├─→ export_dfa_to_json()
    │   └─→ import_dfa_from_json()
    │
    ├─→ dfa_visualizer.py (basic GUI)
    │   ├─→ DFACanvas
    │   └─→ DFAVisualizerWindow
    │
    └─→ interactive_debugger.py (advanced GUI)
        ├─→ InteractiveDFACanvas
        └─→ InteractiveDebuggerWindow
```

## Execution Flow - Interactive Debugging

```
┌──────────────────────────────────────────────────────┐
│              Execution Timeline                      │
└──────────────────────────────────────────────────────┘

Time  │ Action                │ State
──────┼───────────────────────┼─────────────────────────
t0    │ Load DFA              │ DFA loaded, graph ready
      │                       │
t1    │ Enter "aba"           │ String in input field
      │                       │
t2    │ Click "Run"           │ Generate all steps:
      │                       │ [initial, step1, step2,
      │                       │  step3, final]
      │                       │
t3    │ Click "Next"          │ Step 0: Initial
      │                       │ • q0 highlighted (gold)
      │                       │ • No edge highlighted
      │                       │
t4    │ Click "Next"          │ Step 1: Read 'a'
      │                       │ • q1 highlighted (gold)
      │                       │ • q0→q1 edge (red)
      │                       │ • Symbol: 'a'
      │                       │
t5    │ Click "Next"          │ Step 2: Read 'b'
      │                       │ • q1 highlighted (gold)
      │                       │ • q1→q1 edge (red)
      │                       │ • Symbol: 'b'
      │                       │
t6    │ Click "Next"          │ Step 3: Read 'a'
      │                       │ • q0 highlighted (gold)
      │                       │ • q1→q0 edge (red)
      │                       │ • Symbol: 'a'
      │                       │
t7    │ Click "Next"          │ Step 4: Final
      │                       │ • q0 highlighted (gold)
      │                       │ • Result: ACCEPTED ✓
      │                       │
t8    │ Click "Previous"      │ Back to Step 3
      │                       │ • Visualization restored
```

## Performance Profile

```
┌──────────────────────────────────────────────────────┐
│            Performance Characteristics               │
└──────────────────────────────────────────────────────┘

Operation              │ Time Complexity │ Space
───────────────────────┼─────────────────┼──────────────
DFA Creation           │ O(|Q| × |Σ|)    │ O(|Q| + |δ|)
String Processing      │ O(n)            │ O(1)
Trace Generation       │ O(n)            │ O(n)
Step Navigation        │ O(1)            │ O(1)
Graph Layout           │ O(|Q|² + |δ|)   │ O(|Q|)
Graph Rendering        │ O(|Q| + |δ|)    │ O(|Q| + |δ|)
JSON Export            │ O(|Q| + |δ|)    │ O(|Q| + |δ|)
JSON Import            │ O(|Q| + |δ|)    │ O(|Q| + |δ|)

Where:
  n = string length
  |Q| = number of states
  |Σ| = alphabet size
  |δ| = number of transitions
```

## System Requirements

```
┌──────────────────────────────────────────────────────┐
│              System Requirements                     │
├──────────────────────────────────────────────────────┤
│ Software:                                            │
│ • Python 3.7+                                        │
│ • PyQt5 >= 5.15.0 (GUI only)                         │
│ • matplotlib >= 3.5.0 (GUI only)                     │
│ • networkx >= 2.6.0 (GUI only)                       │
├──────────────────────────────────────────────────────┤
│ Hardware:                                            │
│ • CPU: Any modern processor                          │
│ • RAM: 512MB minimum, 1GB recommended                │
│ • Display: 1024x768 minimum, 1920x1080 recommended   │
├──────────────────────────────────────────────────────┤
│ Operating System:                                    │
│ • Windows 7+                                         │
│ • macOS 10.12+                                       │
│ • Linux (any modern distribution)                    │
└──────────────────────────────────────────────────────┘
```

## Summary

This architecture provides:

✅ **Modular Design**: Clear separation of concerns
✅ **Extensibility**: Easy to add new features
✅ **Performance**: Efficient algorithms and caching
✅ **Maintainability**: Well-documented and structured
✅ **Usability**: Intuitive interface and controls
✅ **Reliability**: Comprehensive validation and error handling

The system successfully implements all requirements with a clean, professional architecture suitable for education, development, and research.
