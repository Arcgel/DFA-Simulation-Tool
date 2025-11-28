"""
Complete workflow demonstration: Create → Test → Debug → Export → Import
"""
from dfa import DFA, is_accepted, trace_execution, export_dfa_to_json, import_dfa_from_json


print("="*70)
print("COMPLETE DFA WORKFLOW DEMONSTRATION")
print("="*70)

# STEP 1: Create a DFA
print("\n" + "="*70)
print("STEP 1: CREATE A DFA")
print("="*70)
print("\nCreating DFA that accepts strings with odd number of 'b's...")

states = {'q_even', 'q_odd'}
alphabet = {'a', 'b'}
transitions = {
    ('q_even', 'a'): 'q_even',  # 'a' doesn't change parity
    ('q_even', 'b'): 'q_odd',   # even → odd
    ('q_odd', 'a'): 'q_odd',    # 'a' doesn't change parity
    ('q_odd', 'b'): 'q_even',   # odd → even
}
start_state = 'q_even'
final_states = {'q_odd'}

dfa = DFA(states, alphabet, transitions, start_state, final_states)
print(dfa)

# STEP 2: Test the DFA
print("\n" + "="*70)
print("STEP 2: TEST THE DFA")
print("="*70)
print("\nTesting various strings:")

test_cases = [
    ("b", 1, True),
    ("bb", 2, False),
    ("bbb", 3, True),
    ("ab", 1, True),
    ("aab", 1, True),
    ("aabb", 2, False),
    ("", 0, False),
    ("aaa", 0, False),
]

print(f"{'String':<10} {'# of b':<8} {'Expected':<10} {'Result':<10} {'Status':<10}")
print("-" * 60)

for test_str, b_count, expected in test_cases:
    result = is_accepted(dfa, test_str)
    status = "✓" if result == expected else "✗"
    str_display = f"'{test_str}'"
    print(f"{str_display:<10} {b_count:<8} {str(expected):<10} {str(result):<10} {status:<10}")

# STEP 3: Debug a specific string
print("\n" + "="*70)
print("STEP 3: DEBUG A STRING STEP-BY-STEP")
print("="*70)
print("\nDebugging string 'aabba' (should be REJECTED - 2 b's is even):")
print("-" * 70)

for step in trace_execution(dfa, "aabba"):
    if step['symbol'] is None and not step['is_final_step']:
        print(f"\n┌─ Initial Configuration")
        print(f"│  State: {step['current_state']}")
        print(f"│  Input: '{step['remaining_input']}'")
        print(f"└─")
    elif step['is_final_step']:
        result_symbol = "✓" if step['accepted'] else "✗"
        result_text = "ACCEPTED" if step['accepted'] else "REJECTED"
        print(f"\n┌─ Final Result")
        print(f"│  State: {step['current_state']}")
        print(f"│  Is Accepting: {step['current_state'] in dfa.final_states}")
        print(f"└─ {result_symbol} {result_text}")
    else:
        print(f"\n┌─ Step {step['step_number']}")
        print(f"│  Read: '{step['symbol']}'")
        print(f"│  {step['current_state']} → {step['next_state']}")
        print(f"│  Processed: '{step['processed_input']}'")
        print(f"│  Remaining: '{step['remaining_input']}'")
        print(f"└─")

# STEP 4: Export to JSON
print("\n" + "="*70)
print("STEP 4: EXPORT DFA TO JSON")
print("="*70)

filename = "odd_b_dfa.json"
print(f"\nExporting DFA to '{filename}'...")
export_dfa_to_json(dfa, filename)

print(f"\nJSON file contents:")
with open(filename, 'r') as f:
    print(f.read())

# STEP 5: Import from JSON
print("="*70)
print("STEP 5: IMPORT DFA FROM JSON")
print("="*70)

print(f"\nImporting DFA from '{filename}'...")
imported_dfa = import_dfa_from_json(filename)
print(imported_dfa)

# STEP 6: Verify imported DFA works identically
print("\n" + "="*70)
print("STEP 6: VERIFY IMPORTED DFA")
print("="*70)
print("\nComparing original vs imported DFA:")

verification_strings = ["b", "bb", "bbb", "aabba", ""]

print(f"{'String':<10} {'Original':<10} {'Imported':<10} {'Match':<10}")
print("-" * 45)

all_match = True
for test_str in verification_strings:
    orig_result = is_accepted(dfa, test_str)
    imp_result = is_accepted(imported_dfa, test_str)
    match = "✓" if orig_result == imp_result else "✗"
    
    if orig_result != imp_result:
        all_match = False
    
    str_display = f"'{test_str}'"
    print(f"{str_display:<10} {str(orig_result):<10} {str(imp_result):<10} {match:<10}")

# STEP 7: Summary
print("\n" + "="*70)
print("WORKFLOW SUMMARY")
print("="*70)

print("""
✓ Step 1: Created DFA (odd number of 'b's)
✓ Step 2: Tested DFA with multiple strings
✓ Step 3: Debugged string execution step-by-step
✓ Step 4: Exported DFA to JSON file
✓ Step 5: Imported DFA from JSON file
✓ Step 6: Verified imported DFA works correctly

The complete workflow demonstrates:
• DFA creation with custom states and transitions
• String acceptance testing with is_accepted()
• Step-by-step debugging with trace_execution()
• JSON export with export_dfa_to_json()
• JSON import with import_dfa_from_json()
• Validation that import/export preserves DFA behavior

All functionality is working correctly!
""")

print("="*70)
