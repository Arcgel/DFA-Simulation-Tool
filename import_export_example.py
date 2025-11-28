"""
Simple example demonstrating DFA import/export functionality
"""
from dfa import DFA, export_dfa_to_json, import_dfa_from_json, is_accepted


# Example 1: Create and export a DFA
print("="*70)
print("EXAMPLE 1: Creating and Exporting a DFA")
print("="*70)

# Create a DFA that accepts binary strings divisible by 3
print("\nCreating DFA that accepts binary numbers divisible by 3...")
states = {'q0', 'q1', 'q2'}  # Remainders: 0, 1, 2
alphabet = {'0', '1'}
transitions = {
    ('q0', '0'): 'q0',  # 0 mod 3 = 0
    ('q0', '1'): 'q1',  # 1 mod 3 = 1
    ('q1', '0'): 'q2',  # 2 mod 3 = 2
    ('q1', '1'): 'q0',  # 3 mod 3 = 0
    ('q2', '0'): 'q1',  # 4 mod 3 = 1
    ('q2', '1'): 'q2',  # 5 mod 3 = 2
}
start_state = 'q0'
final_states = {'q0'}  # Accept when divisible by 3

div3_dfa = DFA(states, alphabet, transitions, start_state, final_states)
print(div3_dfa)

# Export to JSON
print("\nExporting to 'divisible_by_3.json'...")
export_dfa_to_json(div3_dfa, "divisible_by_3.json")

# Test the DFA
print("\nTesting binary strings:")
test_cases = [
    ("0", 0),      # 0 ÷ 3 = 0
    ("11", 3),     # 3 ÷ 3 = 1
    ("110", 6),    # 6 ÷ 3 = 2
    ("111", 7),    # 7 ÷ 3 = 2 remainder 1
    ("1001", 9),   # 9 ÷ 3 = 3
]

for binary, decimal in test_cases:
    accepted = is_accepted(div3_dfa, binary)
    status = "✓ ACCEPT" if accepted else "✗ REJECT"
    divisible = "Yes" if decimal % 3 == 0 else "No"
    print(f"{status} | {binary:6} = {decimal:2} | Divisible by 3: {divisible}")


# Example 2: Import and use a DFA
print("\n\n" + "="*70)
print("EXAMPLE 2: Importing and Using a DFA")
print("="*70)

print("\nImporting DFA from 'even_a_dfa.json'...")
imported_dfa = import_dfa_from_json("even_a_dfa.json")
print(imported_dfa)

print("\nTesting imported DFA:")
test_strings = ["", "a", "aa", "aaa", "aaaa", "ababab"]

for test in test_strings:
    accepted = is_accepted(imported_dfa, test)
    status = "✓ ACCEPT" if accepted else "✗ REJECT"
    a_count = test.count('a')
    parity = "even" if a_count % 2 == 0 else "odd"
    print(f"{status} | '{test:8}' | {a_count} a's ({parity})")


# Example 3: Modify and re-export
print("\n\n" + "="*70)
print("EXAMPLE 3: Modifying and Re-exporting a DFA")
print("="*70)

print("\nImporting 'divisible_by_3.json'...")
dfa = import_dfa_from_json("divisible_by_3.json")

print("\nCreating a modified version (accepts remainder 1 instead of 0)...")
# Create new DFA with different final states
modified_dfa = DFA(
    dfa.states,
    dfa.alphabet,
    dfa.transitions,
    dfa.start_state,
    {'q1'}  # Accept remainder 1 instead of 0
)

print("\nExporting modified DFA...")
export_dfa_to_json(modified_dfa, "remainder_1_mod_3.json")

print("\nComparing original vs modified:")
print(f"{'Binary':<8} {'Decimal':<8} {'Original':<10} {'Modified':<10}")
print("-" * 40)

for binary, decimal in test_cases:
    orig = is_accepted(dfa, binary)
    mod = is_accepted(modified_dfa, binary)
    orig_str = "✓" if orig else "✗"
    mod_str = "✓" if mod else "✗"
    print(f"{binary:<8} {decimal:<8} {orig_str:<10} {mod_str:<10}")

print("\n" + "="*70)
print("Examples completed successfully!")
print("="*70)
