# DFA Simulator with Step-by-Step Debugger

A Python implementation of a Deterministic Finite Automaton (DFA) simulator with comprehensive debugging capabilities.

## Features

### 1. DFA Data Structure (`dfa.py`)
Complete implementation of the 5-tuple (Q, Σ, δ, q₀, F):
- **Q**: Set of states
- **Σ**: Alphabet (input symbols)
- **δ**: Transition function (state × symbol → state)
- **q₀**: Start state
- **F**: Set of final/accept states

### 2. Core Functions

#### `is_accepted(dfa, input_string)`
Core simulation logic that processes a string and returns acceptance status.
- Starts at the start state
- Processes symbols one at a time using the transition function
- Returns `True` if final state is an accept state
- Includes error handling for invalid symbols

#### `trace_execution(dfa, input_string)`
Step-by-step debugger that yields detailed execution information:
- **Initial step**: Shows starting configuration
- **Transition steps**: For each symbol, shows:
  - Symbol being processed
  - Current state before transition
  - Next state after transition
  - Processed portion of input
  - Remaining portion of input
  - Transition function notation: δ(state, symbol) → next_state
- **Final step**: Shows whether string was accepted or rejected

### 3. Import/Export Functions

#### `export_dfa_to_json(dfa, filename)`
Exports a DFA object to a JSON file with a well-defined schema.
- Converts DFA structure to JSON format
- Pretty-prints with indentation for readability
- Validates file write operations

#### `import_dfa_from_json(filename)`
Imports a DFA object from a JSON file.
- Validates JSON structure and required fields
- Checks data types and formats
- Constructs and validates DFA object
- Provides detailed error messages

#### JSON Schema
```json
{
  "states": ["q0", "q1", ...],
  "alphabet": ["a", "b", ...],
  "transitions": {
    "state,symbol": "next_state",
    ...
  },
  "start_state": "q0",
  "final_states": ["q0", ...]
}
```

**Transition Format**: The key `"q0,a"` represents δ(q0, a) → next_state

### 4. Example DFA

Included example: DFA that accepts strings with an **even number of 'a's** over Σ = {a, b}

**States:**
- q0: Even number of 'a's (accept state)
- q1: Odd number of 'a's (reject state)

**Transitions:**
- δ(q0, 'a') → q1 (even → odd)
- δ(q0, 'b') → q0 (even → even)
- δ(q1, 'a') → q0 (odd → even)
- δ(q1, 'b') → q1 (odd → odd)

## 📚 Documentation

**All documentation is now organized in the `docs/` folder!**

See **[DOCUMENTATION.md](DOCUMENTATION.md)** for the complete guide, or jump directly to:
- **[Installation Guide](docs/setup/INSTALLATION.md)** - Get started
- **[Quick Start](docs/QUICKSTART.md)** - 5-minute tutorial
- **[User Guide](docs/usage/USER_GUIDE.md)** - Complete instructions
- **[Examples](docs/usage/EXAMPLES.md)** - Usage examples
- **[FAQ](docs/usage/FAQ.md)** - Common questions

---

## Usage

### Basic Usage
```python
from dfa import create_even_a_dfa, is_accepted

# Create DFA
dfa = create_even_a_dfa()

# Test strings
print(is_accepted(dfa, "aa"))    # True (2 a's - even)
print(is_accepted(dfa, "aaa"))   # False (3 a's - odd)
print(is_accepted(dfa, "bbb"))   # True (0 a's - even)
```

### Import/Export Usage
```python
from dfa import export_dfa_to_json, import_dfa_from_json, is_accepted

# Export a DFA to JSON
dfa = create_even_a_dfa()
export_dfa_to_json(dfa, "my_dfa.json")

# Import a DFA from JSON
loaded_dfa = import_dfa_from_json("my_dfa.json")

# Use the imported DFA
result = is_accepted(loaded_dfa, "aba")
print(result)  # True
```

### Step-by-Step Debugging
```python
from dfa import create_even_a_dfa, trace_execution

dfa = create_even_a_dfa()

# Debug a string
for step in trace_execution(dfa, "aba"):
    print(step)
```

### Detailed Debugging Demo
```bash
python debugger_demo.py
```

This shows:
- Detailed trace with box-drawing characters
- Compact table format
- Multiple example strings

### GUI Visualization
```bash
# Install GUI dependencies first
pip install PyQt5 matplotlib networkx

# Run the full visualizer
python dfa_visualizer.py

# Run the interactive step-by-step debugger
python interactive_debugger.py
```

Features:
- Interactive graph visualization
- Load DFA from JSON files
- Test strings with visual feedback
- Step-by-step execution traces
- Path highlighting
- **Interactive debugger with step-through execution**
- **Visual highlighting of current state and transitions**

See `GUI_README.md` and `INTERACTIVE_DEBUGGER_GUIDE.md` for detailed documentation.

## Files

### Core Implementation
- `dfa.py` - Main DFA implementation with all core functions
- `debugger_demo.py` - Demonstration of debugging capabilities with formatted output
- `test_import_export.py` - Comprehensive test suite for import/export functionality
- `import_export_example.py` - Simple examples of import/export usage
- `complete_workflow_demo.py` - Complete workflow demonstration

### GUI Application
- `dfa_visualizer.py` - Full-featured GUI application with PyQt5 and NetworkX
- `interactive_debugger.py` - **Interactive step-by-step debugger with visual highlighting**
- `simple_visualizer.py` - Minimal visualization example
- `visualization_demo.py` - Static visualization generator

### Documentation
All documentation is now organized in the `docs/` folder:
- **[docs/README.md](docs/README.md)** - Documentation index
- **[docs/setup/INSTALLATION.md](docs/setup/INSTALLATION.md)** - Installation guide
- **[docs/QUICKSTART.md](docs/QUICKSTART.md)** - Quick start guide
- **[docs/usage/USER_GUIDE.md](docs/usage/USER_GUIDE.md)** - Complete user guide
- **[docs/technical/](docs/technical/)** - Technical documentation
- **[docs/updates/](docs/updates/)** - Recent updates and changes

### Data Files
- `*.json` - Example DFA files in JSON format
- `requirements.txt` - Python package dependencies

## Error Handling

The simulator includes robust error handling:
- Validates DFA structure on initialization
- Checks for invalid symbols in input strings
- Provides descriptive error messages with symbol position
- Validates JSON structure and format on import
- Handles missing fields, invalid formats, and file I/O errors

## Example Output

```
┌─ Step 1: TRANSITION
│  Read Symbol:   'a'
│  Current State: q0
│  Next State:    q1
│  Transition:    δ(q0, 'a') → q1
│  Processed:     'a'
│  Remaining:     'ba'
└─
```
