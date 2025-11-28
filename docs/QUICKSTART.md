# DFA Simulator - Quick Start Guide

## 5-Minute Quick Start

### Step 1: Verify Python Installation
```bash
python --version
# Should show Python 3.7 or higher
```

### Step 2: Test Core Functionality (No Installation Needed!)
```bash
python dfa.py
```

You should see output showing DFA tests passing.

### Step 3: Try the Debugger
```bash
python debugger_demo.py
```

This shows step-by-step execution traces.

### Step 4: Test Import/Export
```bash
python test_import_export.py
```

This demonstrates JSON import/export functionality.

## GUI Installation (Optional)

### Install GUI Dependencies
```bash
pip install PyQt5 matplotlib networkx
```

### Run the Visualizer
```bash
python dfa_visualizer.py
```

### What You'll See
1. A window with two panels
2. Left panel: Controls (Load, Test, Trace)
3. Right panel: Graph visualization
4. Click "Load DFA from JSON" and select `even_a_dfa.json`
5. Enter a test string like "aba" and click "Test String"
6. Click "Show Step-by-Step Trace" to see execution

## Your First DFA

### Create a Simple DFA in Python

```python
from dfa import DFA, is_accepted

# DFA that accepts strings starting with 'a'
states = {'q0', 'q1', 'q2'}
alphabet = {'a', 'b'}
transitions = {
    ('q0', 'a'): 'q1',  # Start with 'a' → accept
    ('q0', 'b'): 'q2',  # Start with 'b' → reject
    ('q1', 'a'): 'q1',  # Stay in accept
    ('q1', 'b'): 'q1',
    ('q2', 'a'): 'q2',  # Stay in reject
    ('q2', 'b'): 'q2',
}
start_state = 'q0'
final_states = {'q1'}

dfa = DFA(states, alphabet, transitions, start_state, final_states)

# Test it
print(is_accepted(dfa, "abc"))   # True
print(is_accepted(dfa, "bac"))   # False
```

### Export Your DFA

```python
from dfa import export_dfa_to_json

export_dfa_to_json(dfa, "my_first_dfa.json")
```

### Load and Visualize

```bash
python dfa_visualizer.py
# Click "Load DFA from JSON"
# Select "my_first_dfa.json"
```

## Common Tasks

### Task 1: Test a String
```python
from dfa import import_dfa_from_json, is_accepted

dfa = import_dfa_from_json("even_a_dfa.json")
result = is_accepted(dfa, "aba")
print(f"String 'aba' is {'accepted' if result else 'rejected'}")
```

### Task 2: Debug Execution
```python
from dfa import import_dfa_from_json, trace_execution

dfa = import_dfa_from_json("even_a_dfa.json")

for step in trace_execution(dfa, "aba"):
    if step['symbol']:
        print(f"Read '{step['symbol']}': {step['current_state']} → {step['next_state']}")
```

### Task 3: Create from JSON

Create `my_dfa.json`:
```json
{
  "states": ["q0", "q1"],
  "alphabet": ["a", "b"],
  "transitions": {
    "q0,a": "q1",
    "q0,b": "q0",
    "q1,a": "q0",
    "q1,b": "q1"
  },
  "start_state": "q0",
  "final_states": ["q0"]
}
```

Load it:
```python
from dfa import import_dfa_from_json

dfa = import_dfa_from_json("my_dfa.json")
```

## Example DFAs Included

Try these pre-built examples:

### 1. Even Number of 'a's
```bash
python -c "from dfa import import_dfa_from_json, is_accepted; dfa = import_dfa_from_json('even_a_dfa.json'); print(is_accepted(dfa, 'aa'))"
```

### 2. Strings Ending with "ab"
```bash
python -c "from dfa import import_dfa_from_json, is_accepted; dfa = import_dfa_from_json('ends_with_ab.json'); print(is_accepted(dfa, 'aab'))"
```

### 3. Binary Divisible by 3
```bash
python -c "from dfa import import_dfa_from_json, is_accepted; dfa = import_dfa_from_json('divisible_by_3.json'); print(is_accepted(dfa, '110'))"
```

## Troubleshooting

### "No module named 'PyQt5'"
GUI dependencies not installed. Either:
- Install them: `pip install PyQt5 matplotlib networkx`
- Or use core functionality only (no GUI needed)

### "File not found"
Make sure you're in the DFASimulator directory:
```bash
cd DFASimulator
python dfa.py
```

### "Invalid symbol"
The input string contains a symbol not in the DFA's alphabet.
Check the DFA's alphabet and use only those symbols.

### GUI doesn't show graph
Make sure all dependencies are installed:
```bash
pip install PyQt5 matplotlib networkx
```

## Next Steps

### Learn More
- **Core Usage**: Read `USAGE_GUIDE.md`
- **JSON Format**: Read `JSON_SCHEMA.md`
- **GUI Features**: Read `GUI_README.md`
- **Complete Overview**: Read `PROJECT_SUMMARY.md`

### Try Examples
```bash
python complete_workflow_demo.py    # Complete workflow
python import_export_example.py     # Import/export examples
python debugger_demo.py             # Debugging features
```

### Create Your Own DFA
1. Design your DFA on paper
2. Create JSON file with the schema
3. Load in visualizer
4. Test with various strings
5. Debug with trace feature

## Cheat Sheet

### Import/Export
```python
from dfa import export_dfa_to_json, import_dfa_from_json

# Export
export_dfa_to_json(my_dfa, "output.json")

# Import
dfa = import_dfa_from_json("input.json")
```

### Testing
```python
from dfa import is_accepted

result = is_accepted(dfa, "test_string")
# Returns True or False
```

### Debugging
```python
from dfa import trace_execution

for step in trace_execution(dfa, "test_string"):
    print(step)  # Dictionary with step info
```

### Creating DFA
```python
from dfa import DFA

dfa = DFA(
    states={'q0', 'q1'},
    alphabet={'a', 'b'},
    transitions={
        ('q0', 'a'): 'q1',
        ('q0', 'b'): 'q0',
        ('q1', 'a'): 'q0',
        ('q1', 'b'): 'q1',
    },
    start_state='q0',
    final_states={'q0'}
)
```

## Getting Help

1. **Check documentation**: Start with README.md
2. **Run examples**: All `*_demo.py` files
3. **Read guides**: USAGE_GUIDE.md, JSON_SCHEMA.md
4. **Check code**: dfa.py has detailed docstrings

## Success Checklist

- [ ] Python 3.7+ installed
- [ ] Can run `python dfa.py` successfully
- [ ] Can load and test DFAs
- [ ] Understand JSON schema
- [ ] (Optional) GUI dependencies installed
- [ ] (Optional) Can visualize DFAs

## You're Ready!

You now have a complete DFA simulator. Start by:
1. Loading an example DFA
2. Testing some strings
3. Viewing execution traces
4. Creating your own DFA

Happy automata exploration! 🎉
