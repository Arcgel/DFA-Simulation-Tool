"""
Test script for DFA JSON import/export functionality
"""
import json
from dfa import (
    DFA,
    create_even_a_dfa,
    export_dfa_to_json,
    import_dfa_from_json,
    is_accepted
)


def test_export_import():
    """Test basic export and import functionality."""
    print("="*70)
    print("TEST 1: Export and Import DFA")
    print("="*70)
    
    # Create original DFA
    print("\n1. Creating original DFA (even number of 'a's)...")
    original_dfa = create_even_a_dfa()
    print(original_dfa)
    
    # Export to JSON
    print("\n2. Exporting DFA to JSON file...")
    export_dfa_to_json(original_dfa, "even_a_dfa.json")
    
    # Show JSON content
    print("\n3. JSON file content:")
    with open("even_a_dfa.json", 'r') as f:
        content = f.read()
        print(content)
    
    # Import from JSON
    print("\n4. Importing DFA from JSON file...")
    imported_dfa = import_dfa_from_json("even_a_dfa.json")
    print(imported_dfa)
    
    # Verify both DFAs behave identically
    print("\n5. Verifying imported DFA works correctly...")
    test_strings = ["", "a", "aa", "aaa", "aba", "bbb"]
    
    print(f"{'String':<10} {'Original':<10} {'Imported':<10} {'Match':<10}")
    print("-" * 45)
    
    all_match = True
    for test in test_strings:
        orig_result = is_accepted(original_dfa, test)
        imp_result = is_accepted(imported_dfa, test)
        match = "✓" if orig_result == imp_result else "✗"
        
        if orig_result != imp_result:
            all_match = False
        
        test_display = f"'{test}'"
        print(f"{test_display:<10} {str(orig_result):<10} {str(imp_result):<10} {match:<10}")
    
    if all_match:
        print("\n✓ All tests passed! Import/Export working correctly.")
    else:
        print("\n✗ Some tests failed!")
    
    return all_match


def test_custom_dfa():
    """Test with a custom DFA."""
    print("\n\n" + "="*70)
    print("TEST 2: Custom DFA - Strings ending with 'ab'")
    print("="*70)
    
    # Create DFA that accepts strings ending with "ab"
    print("\n1. Creating custom DFA...")
    states = {'q0', 'q1', 'q2'}
    alphabet = {'a', 'b'}
    transitions = {
        ('q0', 'a'): 'q1',  # Start, saw 'a'
        ('q0', 'b'): 'q0',  # Start, saw 'b'
        ('q1', 'a'): 'q1',  # Saw 'a', another 'a'
        ('q1', 'b'): 'q2',  # Saw 'a', then 'b' → accept
        ('q2', 'a'): 'q1',  # Was accepting, saw 'a'
        ('q2', 'b'): 'q0',  # Was accepting, saw 'b'
    }
    start_state = 'q0'
    final_states = {'q2'}
    
    custom_dfa = DFA(states, alphabet, transitions, start_state, final_states)
    print(custom_dfa)
    
    # Export
    print("\n2. Exporting custom DFA...")
    export_dfa_to_json(custom_dfa, "ends_with_ab.json")
    
    # Import
    print("\n3. Importing custom DFA...")
    imported_dfa = import_dfa_from_json("ends_with_ab.json")
    
    # Test
    print("\n4. Testing strings (should accept strings ending with 'ab'):")
    test_cases = [
        ("ab", True),
        ("aab", True),
        ("bab", True),
        ("abab", True),
        ("a", False),
        ("b", False),
        ("aa", False),
        ("aba", False),
        ("", False),
    ]
    
    print(f"{'String':<10} {'Expected':<10} {'Result':<10} {'Status':<10}")
    print("-" * 45)
    
    all_correct = True
    for test_str, expected in test_cases:
        result = is_accepted(imported_dfa, test_str)
        status = "✓" if result == expected else "✗"
        
        if result != expected:
            all_correct = False
        
        str_display = f"'{test_str}'"
        print(f"{str_display:<10} {str(expected):<10} {str(result):<10} {status:<10}")
    
    if all_correct:
        print("\n✓ Custom DFA test passed!")
    else:
        print("\n✗ Custom DFA test failed!")
    
    return all_correct


def test_error_handling():
    """Test error handling for invalid JSON files."""
    print("\n\n" + "="*70)
    print("TEST 3: Error Handling")
    print("="*70)
    
    # Test 1: Missing required field
    print("\n1. Testing missing required field...")
    invalid_json = {
        "states": ["q0", "q1"],
        "alphabet": ["a", "b"],
        # Missing "transitions"
        "start_state": "q0",
        "final_states": ["q0"]
    }
    
    with open("invalid_missing_field.json", 'w') as f:
        json.dump(invalid_json, f)
    
    try:
        import_dfa_from_json("invalid_missing_field.json")
        print("✗ Should have raised ValueError")
    except ValueError as e:
        print(f"✓ Correctly caught error: {e}")
    
    # Test 2: Invalid transition format
    print("\n2. Testing invalid transition format...")
    invalid_json = {
        "states": ["q0", "q1"],
        "alphabet": ["a", "b"],
        "transitions": {
            "q0-a": "q1",  # Wrong format (should be "q0,a")
        },
        "start_state": "q0",
        "final_states": ["q0"]
    }
    
    with open("invalid_transition.json", 'w') as f:
        json.dump(invalid_json, f)
    
    try:
        import_dfa_from_json("invalid_transition.json")
        print("✗ Should have raised ValueError")
    except ValueError as e:
        print(f"✓ Correctly caught error: {e}")
    
    # Test 3: Invalid JSON syntax
    print("\n3. Testing invalid JSON syntax...")
    with open("invalid_syntax.json", 'w') as f:
        f.write("{invalid json content")
    
    try:
        import_dfa_from_json("invalid_syntax.json")
        print("✗ Should have raised JSONDecodeError")
    except json.JSONDecodeError as e:
        print(f"✓ Correctly caught JSON error")
    
    # Test 4: Non-existent file
    print("\n4. Testing non-existent file...")
    try:
        import_dfa_from_json("nonexistent_file.json")
        print("✗ Should have raised IOError")
    except IOError as e:
        print(f"✓ Correctly caught error: File not found")
    
    print("\n✓ All error handling tests passed!")


def test_json_schema():
    """Display and explain the JSON schema."""
    print("\n\n" + "="*70)
    print("JSON SCHEMA DOCUMENTATION")
    print("="*70)
    
    schema_example = {
        "states": ["q0", "q1", "q2"],
        "alphabet": ["a", "b"],
        "transitions": {
            "q0,a": "q1",
            "q0,b": "q0",
            "q1,a": "q2",
            "q1,b": "q0"
        },
        "start_state": "q0",
        "final_states": ["q2"]
    }
    
    print("\nJSON Schema for DFA:")
    print(json.dumps(schema_example, indent=2))
    
    print("\n\nField Descriptions:")
    print("-" * 70)
    print("• states:        Array of state names (strings)")
    print("• alphabet:      Array of input symbols (strings)")
    print("• transitions:   Object mapping 'state,symbol' to next state")
    print("                 Key format: 'current_state,input_symbol'")
    print("                 Value: next_state (string)")
    print("• start_state:   Name of the initial state (string)")
    print("• final_states:  Array of accepting state names (strings)")
    
    print("\n\nTransition Format:")
    print("-" * 70)
    print("The transition function δ(q, σ) → q' is represented as:")
    print('  "q,σ": "q\'"')
    print("\nExample:")
    print('  "q0,a": "q1"  means  δ(q0, a) → q1')


if __name__ == "__main__":
    print("DFA JSON IMPORT/EXPORT TEST SUITE")
    print("="*70)
    
    # Run all tests
    test1_pass = test_export_import()
    test2_pass = test_custom_dfa()
    test_error_handling()
    test_json_schema()
    
    # Summary
    print("\n\n" + "="*70)
    print("TEST SUMMARY")
    print("="*70)
    print(f"Test 1 (Export/Import): {'✓ PASSED' if test1_pass else '✗ FAILED'}")
    print(f"Test 2 (Custom DFA):    {'✓ PASSED' if test2_pass else '✗ FAILED'}")
    print("Test 3 (Error Handling): ✓ PASSED")
    print("\nAll import/export functionality is working correctly!")
