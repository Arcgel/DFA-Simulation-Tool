# DFA Simulator - User Guide

## Table of Contents
1. [Getting Started](#getting-started)
2. [Interactive Debugger](#interactive-debugger)
3. [Basic Visualizer](#basic-visualizer)
4. [Working with JSON Files](#working-with-json-files)
5. [Common Tasks](#common-tasks)
6. [Tips and Tricks](#tips-and-tricks)

---

## Getting Started

### Launching the Application

**Interactive Debugger (Recommended):**
```bash
python interactive_debugger.py
```

**Basic Visualizer:**
```bash
python dfa_visualizer.py
```

### First Steps

1. **Load a DFA**
   - Click "📁 Load DFA" button
   - Select a JSON file (e.g., `even_a_dfa.json`)
   - DFA information appears in the panel

2. **Enter a Test String**
   - Type a string in the input field
   - Use only symbols from the DFA's alphabet

3. **Run the Debugger**
   - Click "▶ Run / Reset" button
   - The debugger initializes with your string

4. **Step Through Execution**
   - Click "⏭ Next Step" to advance
   - Watch the graph highlight current state and transition

---

## Interactive Debugger

### Interface Overview

```
┌──────────────┬────────────────────────┐
│  Controls    │   Graph Visualization  │
│              │                        │
│  1. Load DFA │   • States as circles  │
│  2. Input    │   • Transitions as     │
│  3. Step     │     arrows             │
│  4. Info     │   • Current state      │
│  5. Log      │     highlighted        │
│  6. Legend   │                        │
└──────────────┴────────────────────────┘
```

### Step-by-Step Debugging

#### 1. Load DFA Section
- **📁 Load DFA**: Open file dialog to load JSON
- **🗑️ Clear**: Remove loaded DFA and reset
- **DFA Info**: Shows states, alphabet, start, final states

#### 2. Enter Test String
- **Input Field**: Type your test string
- **▶ Run / Reset**: Initialize debugging session
- Only use symbols from the DFA's alphabet

#### 3. Step Through Execution
- **⏭ Next Step**: Advance one step forward
- **⏮ Previous**: Go back one step
- **⏯ Auto Play**: Automatically step through (800ms intervals)

#### 4. Current Step Information
- **Step Counter**: Shows current step / total steps
- **Symbol**: Current symbol being processed
- **Current State**: Active state in execution
- **Transition**: Shows state change (q0 → q1)
- **Processed**: Portion of string already read
- **Remaining**: Portion of string yet to process

#### 5. Execution Log
- Real-time log of all steps
- Shows each transition
- Final result (ACCEPTED ✓ or REJECTED ✗)

#### 6. Visual Legend
- 🔵 Regular State
- 🔴 Final State (double circle)
- 🟢 Start State (with arrow)
- 🟡 Current State (gold border)
- 🔴 Current Transition (red arrow)

### Visual Highlighting

#### Current State
- **Color**: Gold (#FFD700)
- **Border**: Orange, 4px thick
- **Size**: Larger than regular states
- **Purpose**: Shows exactly where execution is

#### Current Transition
- **Color**: Red
- **Width**: 5px (vs 2px regular)
- **Arrow**: Larger arrowhead
- **Purpose**: Shows active transition being taken

#### Visited States
- **Color**: Faded blue
- **Opacity**: 70%
- **Purpose**: Shows execution history

### Example Session

```
1. Load: even_a_dfa.json
2. Enter: "aba"
3. Click "Run"

Step 1: Initial
  • q0 highlighted (gold)
  • Symbol: [Initial]

Step 2: Read 'a'
  • q0 → q1 (red arrow)
  • q1 highlighted (gold)
  • Processed: "a"
  • Remaining: "ba"

Step 3: Read 'b'
  • q1 → q1 (red arrow)
  • q1 highlighted (gold)
  • Processed: "ab"
  • Remaining: "a"

Step 4: Read 'a'
  • q1 → q0 (red arrow)
  • q0 highlighted (gold)
  • Processed: "aba"
  • Remaining: ""

Step 5: Final
  • q0 highlighted (gold)
  • Result: ACCEPTED ✓
```

---

## Basic Visualizer

### Features

- Load DFA from JSON
- Test strings interactively
- View complete execution trace
- Path highlighting on graph

### Usage

1. **Load DFA**
   - Click "📁 Load DFA"
   - Select JSON file

2. **Test String**
   - Enter string in "Test String" field
   - Click "Test String" or press Enter
   - Result shows ACCEPTED ✓ or REJECTED ✗

3. **View Trace**
   - Click "Show Step-by-Step Trace"
   - See complete execution in trace panel
   - Graph highlights the path taken

4. **Clear**
   - Click "🗑️ Clear" to unload DFA
   - Resets all fields

---

## Working with JSON Files

### Loading a DFA

1. Click "📁 Load DFA" button
2. Navigate to JSON file location
3. Select file and click "Open"
4. DFA loads and displays in graph

### Example DFAs Included

#### even_a_dfa.json
- **Language**: Strings with even number of 'a's
- **Alphabet**: {a, b}
- **Test strings**: 
  - ✓ "" (0 a's)
  - ✓ "aa" (2 a's)
  - ✗ "a" (1 a)
  - ✗ "aaa" (3 a's)

#### ends_with_ab.json
- **Language**: Strings ending with "ab"
- **Alphabet**: {a, b}
- **Test strings**:
  - ✓ "ab"
  - ✓ "aab"
  - ✗ "a"
  - ✗ "aba"

#### divisible_by_3.json
- **Language**: Binary numbers divisible by 3
- **Alphabet**: {0, 1}
- **Test strings**:
  - ✓ "0" (0 ÷ 3 = 0)
  - ✓ "11" (3 ÷ 3 = 1)
  - ✓ "110" (6 ÷ 3 = 2)
  - ✗ "111" (7 ÷ 3 = 2 R 1)

### Creating Your Own DFA

See [JSON_SCHEMA.md](../technical/JSON_SCHEMA.md) for format details.

---

## Common Tasks

### Task 1: Test Multiple Strings

```
1. Load DFA
2. Enter first string → Run → Observe result
3. Enter second string → Run → Observe result
4. Repeat as needed
```

### Task 2: Debug Why String is Rejected

```
1. Load DFA
2. Enter string
3. Click "Run"
4. Click "Next Step" repeatedly
5. Watch where execution goes wrong
6. Check which state it ends in
7. Verify if it's a final state
```

### Task 3: Compare Two DFAs

```
1. Load first DFA
2. Test strings and note results
3. Click "Clear"
4. Load second DFA
5. Test same strings
6. Compare results
```

### Task 4: Understand DFA Behavior

```
1. Load DFA
2. Use "Auto Play" to watch execution
3. Observe state transitions
4. Note which paths lead to acceptance
5. Try edge cases (empty string, single symbol)
```

### Task 5: Export and Share DFA

```
1. Create DFA in Python (see dfa.py)
2. Use export_dfa_to_json(dfa, "filename.json")
3. Share JSON file
4. Others can load it in visualizer
```

---

## Tips and Tricks

### Debugging Tips

1. **Start Simple**
   - Test empty string first
   - Then single symbols
   - Then short strings
   - Build up complexity

2. **Use Auto Play**
   - Good for demonstrations
   - Shows flow clearly
   - 800ms between steps

3. **Check Final State**
   - Is it in the accept states?
   - Double circle = final state
   - Gold highlight = current state

4. **Watch Transitions**
   - Red arrow shows current transition
   - Follow the arrow direction
   - Check symbol on edge label

5. **Use Previous Button**
   - Go back if you missed something
   - Review confusing transitions
   - Compare before/after states

### Visualization Tips

1. **Fullscreen Mode**
   - Maximize window for better view
   - Left panel scrolls if needed
   - Graph uses full space

2. **Read the Legend**
   - Bottom of left panel
   - Color-coded explanations
   - Emoji icons for clarity

3. **Check DFA Info**
   - Shows alphabet (valid symbols)
   - Shows start state
   - Shows final states
   - Helps understand structure

### Testing Tips

1. **Test Edge Cases**
   - Empty string ""
   - Single symbols
   - Very long strings
   - All same symbol

2. **Test Boundaries**
   - Minimum to accept
   - Maximum to accept
   - Just below acceptance
   - Just above acceptance

3. **Invalid Symbols**
   - Try symbols not in alphabet
   - See error message
   - Understand validation

### Workflow Tips

1. **Save Interesting DFAs**
   - Export to JSON
   - Name descriptively
   - Keep organized

2. **Document Your DFAs**
   - Add comments in JSON (not standard, but helpful)
   - Keep separate notes
   - Describe the language

3. **Use Clear Button**
   - Quick reset
   - No need to restart app
   - Confirms before clearing

---

## Keyboard Shortcuts

Currently available:
- **Enter** (in input field): Run/Reset debugging

Future enhancements may include:
- Space: Next step
- Backspace: Previous step
- Escape: Stop auto-play

---

## Troubleshooting

### "No DFA loaded"
**Solution**: Click "📁 Load DFA" and select a JSON file

### "Invalid symbol"
**Solution**: Check DFA's alphabet, use only those symbols

### "Graph is cluttered"
**Solution**: Try a simpler DFA first, or maximize window

### "Can't see current state"
**Solution**: Look for gold circle with orange border

### "Lost track of execution"
**Solution**: Click "Previous" to go back, or "Run" to restart

### "Auto-play too fast/slow"
**Solution**: Currently fixed at 800ms, use Next Step for manual control

---

## Best Practices

1. **Start with Examples**
   - Load provided DFAs first
   - Understand how they work
   - Then create your own

2. **Test Thoroughly**
   - Try many different strings
   - Test edge cases
   - Verify expected behavior

3. **Use Step-by-Step**
   - Don't just check accept/reject
   - Understand WHY it accepts/rejects
   - Learn the execution path

4. **Keep DFAs Simple**
   - Start with 2-3 states
   - Add complexity gradually
   - Easier to visualize and debug

5. **Document Your Work**
   - Name files clearly
   - Keep notes on what each DFA does
   - Save interesting test cases

---

## Next Steps

- Explore [JSON_SCHEMA.md](../technical/JSON_SCHEMA.md) to create custom DFAs
- Read [EXAMPLES.md](EXAMPLES.md) for more usage examples
- Check [FAQ.md](FAQ.md) for common questions

---

## Getting Help

If you need assistance:
1. Check this user guide
2. Review example DFAs
3. Read error messages carefully
4. Try simpler test cases
5. Restart the application if needed
