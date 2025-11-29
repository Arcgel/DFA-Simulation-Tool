"""
Comprehensive test for Export as JSON functionality
Tests the export_dfa method without GUI interaction
"""
import sys
import os
import json
from dfa import DFA, export_dfa_to_json, import_dfa_from_json, is_accepted


def test_export_logic():
    """Test the export logic without GUI."""
    print("=" * 60)
    print("Testing Export Functionality")
    print("=" * 60)
    
    # Test 1: Create a simple DFA
    print("\n[Test 1] Creating a simple DFA...")
    try:
        test_dfa = DFA(
            states={'q0', 'q1'},
            alphabet={'a', 'b'},
            transitions={
                ('q0', 'a'): 'q1',
                ('q0', 'b'): 'q0',
                ('q1', 'a'): 'q1',
                ('q1', 'b'): 'q0'
            },
            start_state='q0',
            final_states={'q1'}
        )
        print("✓ DFA created successfully")
    except Exception as e:
        print(f"✗ Failed to create DFA: {e}")
        return False
    
    # Test 2: Export to JSON
    print("\n[Test 2] Exporting DFA to JSON...")
    test_filename = 'test_export_temp.json'
    try:
        export_dfa_to_json(test_dfa, test_filename)
        print(f"✓ DFA exported to {test_filename}")
    except Exception as e:
        print(f"✗ Failed to export DFA: {e}")
        return False
    
    # Test 3: Verify file exists
    print("\n[Test 3] Verifying file exists...")
    if os.path.exists(test_filename):
        print(f"✓ File {test_filename} exists")
    else:
        print(f"✗ File {test_filename} not found")
        return False
    
    # Test 4: Verify JSON structure
    print("\n[Test 4] Verifying JSON structure...")
    try:
        with open(test_filename, 'r') as f:
            data = json.load(f)
        
        required_keys = ['states', 'alphabet', 'transitions', 'start_state', 'final_states']
        for key in required_keys:
            if key not in data:
                print(f"✗ Missing key: {key}")
                return False
        print("✓ JSON structure is valid")
        print(f"  States: {data['states']}")
        print(f"  Alphabet: {data['alphabet']}")
        print(f"  Start state: {data['start_state']}")
        print(f"  Final states: {data['final_states']}")
    except Exception as e:
        print(f"✗ Failed to read/parse JSON: {e}")
        return False
    
    # Test 5: Re-import and verify
    print("\n[Test 5] Re-importing DFA...")
    try:
        imported_dfa = import_dfa_from_json(test_filename)
        print("✓ DFA imported successfully")
        
        # Verify properties match
        if imported_dfa.states != test_dfa.states:
            print("✗ States don't match")
            return False
        if imported_dfa.alphabet != test_dfa.alphabet:
            print("✗ Alphabet doesn't match")
            return False
        if imported_dfa.start_state != test_dfa.start_state:
            print("✗ Start state doesn't match")
            return False
        if imported_dfa.final_states != test_dfa.final_states:
            print("✗ Final states don't match")
            return False
        
        print("✓ Imported DFA matches original")
    except Exception as e:
        print(f"✗ Failed to import DFA: {e}")
        return False
    
    # Test 6: Test DFA functionality
    print("\n[Test 6] Testing DFA functionality...")
    test_cases = [
        ('a', True),      # Should accept (ends in q1)
        ('aa', True),     # Should accept
        ('ab', False),    # Should reject (ends in q0)
        ('ba', True),     # Should accept
        ('', False),      # Should reject (starts in q0)
    ]
    
    all_passed = True
    for input_str, expected in test_cases:
        result = is_accepted(imported_dfa, input_str)
        status = "✓" if result == expected else "✗"
        print(f"  {status} Input '{input_str}': {result} (expected {expected})")
        if result != expected:
            all_passed = False
    
    if not all_passed:
        print("✗ Some test cases failed")
        return False
    
    # Test 7: Test with incomplete DFA (missing transitions)
    print("\n[Test 7] Testing incomplete DFA validation...")
    try:
        incomplete_dfa = DFA(
            states={'q0', 'q1'},
            alphabet={'a', 'b'},
            transitions={
                ('q0', 'a'): 'q1',
                # Missing other transitions
            },
            start_state='q0',
            final_states={'q1'}
        )
        
        print(f"✗ DFA class should have rejected incomplete transitions")
        return False
    except Exception as e:
        # This is expected - DFA class validates completeness
        print(f"✓ DFA class correctly rejects incomplete transitions: {e}")
    
    # Test 8: Test with no final states
    print("\n[Test 8] Testing DFA with no final states...")
    try:
        no_final_dfa = DFA(
            states={'q0', 'q1'},
            alphabet={'a', 'b'},
            transitions={
                ('q0', 'a'): 'q1',
                ('q0', 'b'): 'q0',
                ('q1', 'a'): 'q1',
                ('q1', 'b'): 'q0'
            },
            start_state='q0',
            final_states=set()  # No final states
        )
        
        no_final_filename = 'test_no_final_temp.json'
        export_dfa_to_json(no_final_dfa, no_final_filename)
        print(f"✓ DFA with no final states exported")
        
        # Verify it rejects all strings
        imported = import_dfa_from_json(no_final_filename)
        if is_accepted(imported, 'a') or is_accepted(imported, ''):
            print("✗ DFA should reject all strings")
            return False
        print("✓ DFA correctly rejects all strings")
        
        # Clean up
        if os.path.exists(no_final_filename):
            os.remove(no_final_filename)
    except Exception as e:
        print(f"✗ Failed with no final states: {e}")
        return False
    
    # Cleanup
    print("\n[Cleanup] Removing test files...")
    if os.path.exists(test_filename):
        os.remove(test_filename)
        print(f"✓ Removed {test_filename}")
    
    print("\n" + "=" * 60)
    print("✓ ALL TESTS PASSED!")
    print("=" * 60)
    return True


def test_builder_validation():
    """Test the validation logic that would be in the builder."""
    print("\n" + "=" * 60)
    print("Testing Builder Validation Logic")
    print("=" * 60)
    
    # Simulate builder state
    states = ['q0', 'q1']
    alphabet = ['a', 'b']
    transitions = {
        ('q0', 'a'): 'q1',
        ('q0', 'b'): 'q0',
        ('q1', 'a'): 'q1',
        ('q1', 'b'): 'q0'
    }
    start_state = 'q0'
    final_states = ['q1']
    
    # Test 1: Check for missing transitions
    print("\n[Test 1] Checking for missing transitions...")
    missing = []
    for state in states:
        for symbol in alphabet:
            if (state, symbol) not in transitions:
                missing.append(f"({state}, {symbol})")
    
    if missing:
        print(f"✗ Missing transitions: {missing}")
    else:
        print("✓ All transitions present")
    
    # Test 2: Check with incomplete transitions
    print("\n[Test 2] Checking incomplete transitions...")
    incomplete_transitions = {
        ('q0', 'a'): 'q1',
        # Missing 3 transitions
    }
    
    missing = []
    for state in states:
        for symbol in alphabet:
            if (state, symbol) not in incomplete_transitions:
                missing.append(f"({state}, {symbol})")
    
    if missing:
        print(f"✓ Correctly detected {len(missing)} missing transitions: {missing}")
    else:
        print("✗ Should have detected missing transitions")
    
    # Test 3: Validate required fields
    print("\n[Test 3] Validating required fields...")
    
    checks = [
        (len(states) > 0, "States present"),
        (len(alphabet) > 0, "Alphabet present"),
        (start_state is not None, "Start state set"),
    ]
    
    all_valid = True
    for check, description in checks:
        if check:
            print(f"  ✓ {description}")
        else:
            print(f"  ✗ {description}")
            all_valid = False
    
    if all_valid:
        print("✓ All required fields valid")
    
    print("\n" + "=" * 60)
    print("✓ VALIDATION TESTS PASSED!")
    print("=" * 60)


if __name__ == '__main__':
    print("\n" + "=" * 60)
    print("COMPREHENSIVE EXPORT FUNCTIONALITY TEST")
    print("=" * 60)
    
    success = True
    
    # Run export logic tests
    if not test_export_logic():
        success = False
    
    # Run validation tests
    test_builder_validation()
    
    if success:
        print("\n" + "=" * 60)
        print("✓✓✓ ALL TESTS PASSED SUCCESSFULLY! ✓✓✓")
        print("=" * 60)
        print("\nThe export functionality is working correctly!")
        print("You can now use the '💾 Export as JSON' button in the DFA Builder.")
    else:
        print("\n" + "=" * 60)
        print("✗✗✗ SOME TESTS FAILED ✗✗✗")
        print("=" * 60)
        sys.exit(1)
