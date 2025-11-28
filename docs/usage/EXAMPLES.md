# DFA Simulator - Usage Examples

## Table of Contents
1. [Basic Examples](#basic-examples)
2. [Interactive Debugger Examples](#interactive-debugger-examples)
3. [Creating Custom DFAs](#creating-custom-dfas)
4. [Advanced Examples](#advanced-examples)

---

## Basic Examples

### Example 1: Testing a Simple String

```bash
# Start the interactive debugger
python interactive_debugger.py
```

**Steps:**
1. Click "📁 Load DFA"
2. Select `even_a_dfa.json`
3. Enter "aa" in the input field
4. Click "▶ Run / Reset"
5. Click "⏭ Next Step" three times
6. Observe: ACCEPTED ✓ (2 a's is even)

---

### Example 2: Understanding Why a String is Rejected

```bash
python interactive_debugger.py
```

**Steps:**
1. Load `even_a_dfa.json`
2. Enter "aaa"
3. Click "Run"
4. Step through execution:
   - Step 1: q0 (start, even)
   - Step 2: Read 'a' → q1 (odd)
   - Step 3: Read 'a' → q0 (even)
   - Step 4: Read 'a' → q1 (odd)
   - Step 5: Final state q1 (NOT in accept states)
5. Result: REJECTED ✗

**Lesson**: String ends in q1 (odd state), not q0 (even state)

---

### Example 3: Using Auto-Play

```bash
python interactive_debugger.py
```

**Steps:**
1. Load any DFA
2. Enter a test string
3. Click "Run"
4. Click "⏯ Auto Play"
5. Watch automatic step-through (800ms intervals)
6. Observe state transitions and highlighting

**Use Case**: Demonstrations, presentations, learning

---

## Interactive Debugger Examples

### Example 4: Comparing Accepted vs Rejected Strings

**DFA**: `even_a_dfa.json`

**Test 1 - Accepted:**
```
Input: "aa"
Steps:
  q0 --a--> q1 --a--> q0
Result: ACCEPTED ✓ (ends in q0)
```

**Test 2 - Rejected:**
```
Input: "aaa"
Steps:
  q0 --a--> q1 --a--> q0 --a--> q1
Result: REJECTED ✗ (ends in q1)
```

**Observation**: Even number of 'a's ends in q0, odd ends in q1

---

### Example 5: Testing Edge Cases

**DFA**: `ends_with_ab.json`

**Test Cases:**
```
""     → REJECTED ✗ (doesn't end with "ab")
"a"    → REJECTED ✗ (doesn't end with "ab")
"b"    → REJECTED ✗ (doesn't end with "ab")
"ab"   → ACCEPTED ✓ (ends with "ab")
"aab"  → ACCEPTED ✓ (ends with "ab")
"aba"  → REJECTED ✗ (ends with "a", not "ab")
"abab" → ACCEPTED ✓ (ends with "ab")
```

**Lesson**: Only strings ending with "ab" are accepted

---

### Example 6: Binary Number Testing

**DFA**: `divisible_by_3.json`

**Test Cases:**
```
"0"    → 0  → ACCEPTED ✓ (0 ÷ 3 = 0)
"11"   → 3  → ACCEPTED ✓ (3 ÷ 3 = 1)
"110"  → 6  → ACCEPTED ✓ (6 ÷ 3 = 2)
"111"  → 7  → REJECTED ✗ (7 ÷ 3 = 2 R 1)
"1001" → 9  → ACCEPTED ✓ (9 ÷ 3 = 3)
"1010" → 10 → REJECTED ✗ (10 ÷ 3 = 3 R 1)
```

**Lesson**: DFA tracks remainder when dividing by 3

---

## Creating Custom DFAs

### Example 7: DFA for Strings Starting with 'a'

**Create JSON file** (`starts_with_a.json`):
```json
{
  "states": ["q0", "q1", "q2"],
  "alphabet": ["a", "b"],
  "transitions": {
    "q0,a": "q1",
    "q0,b": "q2",
    "q1,a": "q1",
    "q1,b": "q1",
    "q2,a": "q2",
    "q2,b": "q2"
  },
  "start_state": "q0",
  "final_states": ["q1"]
}
```

**Test:**
```
"a"    → ACCEPTED ✓
"ab"   → ACCEPTED ✓
"aaa"  → ACCEPTED ✓
"b"    → REJECTED ✗
"ba"   → REJECTED ✗
```

---

### Example 8: DFA for Exactly Two 'a's

**Create JSON file** (`exactly_two_a.json`):
```json
{
  "states": ["q0", "q1", "q2", "q3"],
  "alphabet": ["a", "b"],
  "transitions": {
    "q0,a": "q1",
    "q0,b": "q0",
    "q1,a": "q2",
    "q1,b": "q1",
    "q2,a": "q3",
    "q2,b": "q2",
    "q3,a": "q3",
    "q3,b": "q3"
  },
  "start_state": "q0",
  "final_states": ["q2"]
}
```

**Test:**
```
"aa"   → ACCEPTED ✓
"aba"  → ACCEPTED ✓
"baa"  → ACCEPTED ✓
"a"    → REJECTED ✗ (only 1 'a')
"aaa"  → REJECTED ✗ (3 'a's)
```

---

## Advanced Examples

### Example 9: Debugging Complex Execution

**DFA**: `divisible_by_3.json`
**String**: "1101"

**Step-by-Step Analysis:**
```
Binary: 1101 = 13 in decimal
13 ÷ 3 = 4 R 1 → Should be REJECTED

Execution:
  q0 (rem 0) --1--> q1 (rem 1)
  q1 (rem 1) --1--> q0 (rem 0)  [11 = 3, rem 0]
  q0 (rem 0) --0--> q0 (rem 0)  [110 = 6, rem 0]
  q0 (rem 0) --1--> q1 (rem 1)  [1101 = 13, rem 1]
  
Final: q1 (rem 1) → REJECTED ✗
```

**Lesson**: DFA correctly tracks remainder through binary digits

---

### Example 10: Comparing Two DFAs

**DFA 1**: `even_a_dfa.json` (even 'a's)
**DFA 2**: `odd_b_dfa.json` (odd 'b's)

**Test String**: "aba"

**DFA 1 (even 'a's):**
```
'a' count: 2 (even)
Result: ACCEPTED ✓
```

**DFA 2 (odd 'b's):**
```
'b' count: 1 (odd)
Result: ACCEPTED ✓
```

**Observation**: Same string, different criteria, both accept

---

### Example 11: Using Previous Button

**Scenario**: Missed a transition

**Steps:**
1. Load DFA and run string
2. Click "Next Step" several times
3. Realize you missed something
4. Click "⏮ Previous" to go back
5. Review the transition again
6. Continue forward with "Next Step"

**Use Case**: Learning, reviewing, understanding

---

### Example 12: Testing Invalid Symbols

**DFA**: `even_a_dfa.json` (alphabet: {a, b})

**Test**: Enter "abc"

**Result:**
```
Error: Invalid symbol 'c' at position 2.
Symbol not in alphabet {'a', 'b'}
```

**Lesson**: DFA validates input against alphabet

---

## Practical Scenarios

### Scenario 1: Teaching Automata Theory

**Goal**: Show students how DFAs work

**Steps:**
1. Load simple DFA (e.g., `even_a_dfa.json`)
2. Use Auto-Play to demonstrate
3. Test various strings
4. Show accept vs reject
5. Explain state transitions

---

### Scenario 2: Debugging DFA Design

**Goal**: Verify DFA accepts correct language

**Steps:**
1. Create DFA in JSON
2. Load in visualizer
3. Test edge cases
4. Step through unexpected results
5. Identify incorrect transitions
6. Fix JSON and reload

---

### Scenario 3: Comparing Algorithms

**Goal**: Compare different DFA designs

**Steps:**
1. Load first DFA
2. Test strings, note results
3. Click "Clear"
4. Load second DFA
5. Test same strings
6. Compare efficiency/correctness

---

## Tips for Examples

### Creating Good Test Cases

1. **Empty String**: Always test ""
2. **Single Symbols**: Test each alphabet symbol
3. **Minimum Accept**: Shortest accepting string
4. **Minimum Reject**: Shortest rejecting string
5. **Edge Cases**: Boundary conditions
6. **Long Strings**: Verify scalability

### Understanding Results

1. **Watch State Changes**: Follow gold highlighting
2. **Check Transitions**: Red arrows show path
3. **Verify Final State**: Double circle = final
4. **Read Execution Log**: Text summary of steps

### Debugging Techniques

1. **Start Simple**: Test short strings first
2. **Use Step-by-Step**: Don't just check result
3. **Compare Similar**: Test "aa" vs "aaa"
4. **Check Alphabet**: Verify valid symbols
5. **Review DFA Info**: Understand structure

---

## Example Workflows

### Workflow 1: Quick Test
```
Load DFA → Enter string → Run → Check result
```

### Workflow 2: Deep Analysis
```
Load DFA → Enter string → Run → 
Step through → Observe each transition →
Understand why accepted/rejected
```

### Workflow 3: Batch Testing
```
Load DFA → Test string 1 → Note result →
Test string 2 → Note result →
Test string 3 → Note result →
Compare results
```

### Workflow 4: DFA Development
```
Create JSON → Load → Test → Find issue →
Fix JSON → Reload → Test → Verify
```

---

## Next Steps

- Try creating your own DFAs
- Test with complex strings
- Explore all example DFAs
- Read [JSON_SCHEMA.md](../technical/JSON_SCHEMA.md) for format details

---

**Practice makes perfect! Try these examples and experiment with your own.**
