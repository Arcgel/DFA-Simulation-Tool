# DFA JSON Schema Documentation

## Overview

This document describes the JSON schema used for importing and exporting DFA (Deterministic Finite Automaton) structures.

## Schema Structure

```json
{
  "states": ["q0", "q1", "q2", ...],
  "alphabet": ["a", "b", "c", ...],
  "transitions": {
    "state,symbol": "next_state",
    ...
  },
  "start_state": "q0",
  "final_states": ["q0", "q2", ...]
}
```

## Field Descriptions

### `states` (required)
- **Type**: Array of strings
- **Description**: List of all state names in the DFA
- **Example**: `["q0", "q1", "q2"]`
- **Constraints**: 
  - Must contain at least one state
  - State names should be unique
  - All states referenced in transitions must be in this list

### `alphabet` (required)
- **Type**: Array of strings
- **Description**: Set of input symbols the DFA can process
- **Example**: `["a", "b"]` or `["0", "1"]`
- **Constraints**:
  - Must contain at least one symbol
  - Symbols should be unique
  - Typically single characters, but can be strings

### `transitions` (required)
- **Type**: Object (dictionary)
- **Description**: Transition function δ(state, symbol) → next_state
- **Key Format**: `"current_state,input_symbol"`
- **Value Format**: `"next_state"` (string)
- **Example**:
  ```json
  {
    "q0,a": "q1",
    "q0,b": "q0",
    "q1,a": "q0",
    "q1,b": "q1"
  }
  ```
- **Constraints**:
  - Must be complete: every (state, symbol) pair must have a transition
  - Keys use comma separator: `"state,symbol"`
  - All states in transitions must exist in `states` array
  - All symbols in transitions must exist in `alphabet` array

### `start_state` (required)
- **Type**: String
- **Description**: The initial state where DFA execution begins
- **Example**: `"q0"`
- **Constraints**:
  - Must be one of the states in the `states` array
  - Only one start state is allowed

### `final_states` (required)
- **Type**: Array of strings
- **Description**: Set of accepting/final states
- **Example**: `["q0"]` or `["q2", "q3"]`
- **Constraints**:
  - Can be empty (DFA accepts no strings)
  - All states must exist in the `states` array
  - States should be unique

## Complete Examples

### Example 1: Even Number of 'a's

DFA that accepts strings with an even number of 'a's over alphabet {a, b}.

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

**Language**: L = {w ∈ {a,b}* | w contains an even number of 'a's}

### Example 2: Strings Ending with "ab"

DFA that accepts strings ending with "ab" over alphabet {a, b}.

```json
{
  "states": ["q0", "q1", "q2"],
  "alphabet": ["a", "b"],
  "transitions": {
    "q0,a": "q1",
    "q0,b": "q0",
    "q1,a": "q1",
    "q1,b": "q2",
    "q2,a": "q1",
    "q2,b": "q0"
  },
  "start_state": "q0",
  "final_states": ["q2"]
}
```

**Language**: L = {w ∈ {a,b}* | w ends with "ab"}

### Example 3: Binary Numbers Divisible by 3

DFA that accepts binary numbers divisible by 3.

```json
{
  "states": ["q0", "q1", "q2"],
  "alphabet": ["0", "1"],
  "transitions": {
    "q0,0": "q0",
    "q0,1": "q1",
    "q1,0": "q2",
    "q1,1": "q0",
    "q2,0": "q1",
    "q2,1": "q2"
  },
  "start_state": "q0",
  "final_states": ["q0"]
}
```

**Language**: L = {w ∈ {0,1}* | binary(w) mod 3 = 0}

## Transition Function Notation

The transition function δ: Q × Σ → Q is represented in JSON as:

```
δ(q, σ) → q'  ⟺  "q,σ": "q'"
```

**Examples**:
- δ(q0, a) → q1 becomes `"q0,a": "q1"`
- δ(q1, b) → q0 becomes `"q1,b": "q0"`
- δ(q2, 0) → q2 becomes `"q2,0": "q2"`

## Validation Rules

When importing a DFA from JSON, the following validations are performed:

1. **Required Fields**: All five fields must be present
2. **Data Types**: 
   - `states`, `alphabet`, `final_states` must be arrays
   - `transitions` must be an object
   - `start_state` must be a string
3. **Completeness**: Transition function must be complete (all state-symbol pairs defined)
4. **Consistency**:
   - `start_state` must be in `states`
   - All `final_states` must be in `states`
   - All transition sources and targets must be in `states`
   - All transition symbols must be in `alphabet`

## Error Messages

Common errors and their meanings:

- `"Missing required fields in JSON: [...]"` - One or more required fields are missing
- `"Invalid transition key format: '...'"` - Transition key doesn't follow "state,symbol" format
- `"Start state ... not in states"` - Start state is not in the states list
- `"Final states must be subset of states"` - Some final states are not in the states list
- `"Missing transition for (..., ...)"` - Transition function is incomplete
- `"Invalid symbol '...' at position ..."` - Input string contains symbol not in alphabet

## Usage

### Exporting a DFA
```python
from dfa import export_dfa_to_json

export_dfa_to_json(my_dfa, "output.json")
```

### Importing a DFA
```python
from dfa import import_dfa_from_json

my_dfa = import_dfa_from_json("input.json")
```

## Best Practices

1. **State Naming**: Use descriptive names like "q0", "q1", or "even", "odd"
2. **Alphabets**: Keep symbols simple, typically single characters
3. **Formatting**: Use indentation (2 or 4 spaces) for readability
4. **Validation**: Always test imported DFAs with known inputs
5. **Documentation**: Add comments in separate files to explain the DFA's purpose
6. **Sorting**: States and alphabet are automatically sorted on export for consistency
