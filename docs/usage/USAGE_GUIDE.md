# DFA Simulator - Complete Usage Guide

## Quick Start

### 1. Basic DFA Creation and Testing

```python
from dfa import DFA, is_accepted

# Define DFA components
states = {'q0', 'q1'}
alphabet = {'a', 'b'}
transitions = {
    ('q0', 'a'): 'q1',
    ('q0', 'b'): 'q0',
    ('q1', 'a'): 'q0',
    ('q1', 'b'): 'q1',
}
start_state = 'q0'
final_states = {'q0'}

# Create DFA
dfa = DFA(states, alphabet, transitions, start_state, final_states)

# Test strings
print(is_accepted(dfa, "aa"))   # True
print(is_accepted(dfa, "aaa"))  # False
```

### 2. Using Pre-built DFA

```python
from dfa import create_even_a_dfa, is_accepted

dfa = create_even_a_dfa()
print(is_accepted(dfa, "aba"))  # True (2 a's - even)
```

### 3. Step-by-Step Debugging

```python
from dfa import create_even_a_dfa, trace_execution

dfa = create_even_a_dfa()

for step in trace_execution(dfa, "aba"):
    if not step['is_final_step'] and step['symbol']:
        print(f"Read '{step['symbol']}': {step['current_state']} → {step['next_state']}")
    elif step['is_final_step']:
        print(f"Result: {'ACCEPT' if step['accepted'] else 'REJECT'}")
```

### 4. Export DFA to JSON

```python
from dfa import create_even_a_dfa, export_dfa_to_json

dfa = create_even_a_dfa()
export_dfa_to_json(dfa, "my_dfa.json")
```

### 5. Import DFA from JSON

```python
from dfa import import_dfa_from_json, is_accepted

dfa = import_dfa_from_json("my_dfa.json")
print(is_accepted(dfa, "test_string"))
```

## Running Examples

### Run All Tests
```bash
python test_import_export.py
```

### Run Debugger Demo
```bash
python debugger_demo.py
```

### Run Import/Export Examples
```bash
python import_export_example.py
```

### Run Main DFA Tests
```bash
python dfa.py
```

## Creating Custom DFAs

### Example: Strings Starting with 'a'

```python
from dfa import DFA, is_accepted

states = {'q0', 'q1', 'q2'}
alphabet = {'a', 'b'}
transitions = {
    ('q0', 'a'): 'q1',  # Start with 'a' → accept state
    ('q0', 'b'): 'q2',  # Start with 'b' → reject state
    ('q1', 'a'): 'q1',  # Stay in accept
    ('q1', 'b'): 'q1',  # Stay in accept
    ('q2', 'a'): 'q2',  # Stay in reject
    ('q2', 'b'): 'q2',  # Stay in reject
}
start_state = 'q0'
final_states = {'q1'}

dfa = DFA(states, alphabet, transitions, start_state, final_states)

# Test
print(is_accepted(dfa, "abc"))   # True
print(is_accepted(dfa, "bac"))   # False
```

### Example: Exactly Two 'a's

```python
from dfa import DFA, is_accepted

states = {'q0', 'q1', 'q2', 'q3'}
alphabet = {'a', 'b'}
transitions = {
    ('q0', 'a'): 'q1',  # Saw 1 'a'
    ('q0', 'b'): 'q0',  # Still 0 'a's
    ('q1', 'a'): 'q2',  # Saw 2 'a's (accept)
    ('q1', 'b'): 'q1',  # Still 1 'a'
    ('q2', 'a'): 'q3',  # Saw 3 'a's (too many)
    ('q2', 'b'): 'q2',  # Still 2 'a's
    ('q3', 'a'): 'q3',  # More than 2 'a's
    ('q3', 'b'): 'q3',  # More than 2 'a's
}
start_state = 'q0'
final_states = {'q2'}

dfa = DFA(states, alphabet, transitions, start_state, final_states)

# Test
print(is_accepted(dfa, "aa"))    # True
print(is_accepted(dfa, "aba"))   # True
print(is_accepted(dfa, "aaa"))   # False
```

## Working with JSON Files

### Manual JSON Creation

Create a file `my_dfa.json`:

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

Then import it:

```python
from dfa import import_dfa_from_json

dfa = import_dfa_from_json("my_dfa.json")
```

### Modifying Exported DFAs

1. Export a DFA to JSON
2. Edit the JSON file manually
3. Import the modified DFA

```python
from dfa import create_even_a_dfa, export_dfa_to_json, import_dfa_from_json

# Export
dfa = create_even_a_dfa()
export_dfa_to_json(dfa, "temp.json")

# Manually edit temp.json...

# Import modified version
modified_dfa = import_dfa_from_json("temp.json")
```

## Advanced Debugging

### Detailed Trace with Custom Formatting

```python
from dfa import create_even_a_dfa, trace_execution

dfa = create_even_a_dfa()

print("Tracing execution of 'aba':")
print("-" * 50)

for step in trace_execution(dfa, "aba"):
    if step['symbol'] is None and not step['is_final_step']:
        print(f"Initial: {step['current_state']}")
    elif step['is_final_step']:
        result = "✓ ACCEPTED" if step['accepted'] else "✗ REJECTED"
        print(f"Final: {step['current_state']} → {result}")
    else:
        print(f"Step {step['step_number']}: "
              f"δ({step['current_state']}, '{step['symbol']}') = {step['next_state']}")
```

### Collecting All States Visited

```python
from dfa import create_even_a_dfa, trace_execution

dfa = create_even_a_dfa()

states_visited = []
for step in trace_execution(dfa, "aba"):
    if step['current_state'] not in states_visited:
        states_visited.append(step['current_state'])

print(f"States visited: {states_visited}")
```

## Error Handling

### Catching Invalid Symbols

```python
from dfa import create_even_a_dfa, is_accepted

dfa = create_even_a_dfa()

try:
    result = is_accepted(dfa, "abc")  # 'c' not in alphabet
except ValueError as e:
    print(f"Error: {e}")
```

### Catching Invalid JSON

```python
from dfa import import_dfa_from_json

try:
    dfa = import_dfa_from_json("invalid.json")
except (ValueError, IOError) as e:
    print(f"Failed to import: {e}")
```

## Tips and Best Practices

1. **State Naming**: Use descriptive names (e.g., "even", "odd") or standard notation (e.g., "q0", "q1")

2. **Testing**: Always test your DFA with both accepting and rejecting strings

3. **Validation**: The DFA class automatically validates completeness on creation

4. **Debugging**: Use `trace_execution()` to understand why a string is accepted/rejected

5. **JSON Files**: Keep JSON files organized and use descriptive filenames

6. **Documentation**: Add comments explaining what language your DFA accepts

7. **Reusability**: Export DFAs to JSON for easy sharing and reuse

## Common Patterns

### Accept Empty String Only
```python
final_states = {start_state}  # Only start state is accepting
# All transitions lead away from start state
```

### Accept All Strings
```python
final_states = states  # All states are accepting
```

### Accept No Strings
```python
final_states = set()  # No accepting states
```

## Troubleshooting

### "Missing transition for (state, symbol)"
- Ensure every state has a transition for every symbol in the alphabet
- The transition function must be complete

### "Symbol not in alphabet"
- Check that your input string only contains symbols from the DFA's alphabet
- Verify the alphabet includes all necessary symbols

### "Start state not in states"
- Ensure the start state is included in the states set

### JSON Import Fails
- Validate JSON syntax using a JSON validator
- Check that all required fields are present
- Verify transition keys use "state,symbol" format

## Further Reading

- `README.md` - Project overview and features
- `JSON_SCHEMA.md` - Detailed JSON schema documentation
- `dfa.py` - Source code with inline documentation
