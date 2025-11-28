"""
Demonstration of the DFA step-by-step debugger
"""
from dfa import create_even_a_dfa, trace_execution


def print_detailed_trace(dfa, input_string):
    """Print a detailed, formatted trace of DFA execution."""
    print(f"\n{'='*70}")
    print(f"DEBUGGING: '{input_string}'")
    print(f"{'='*70}\n")
    
    for step in trace_execution(dfa, input_string):
        step_num = step['step_number']
        
        if step['symbol'] is None and not step['is_final_step']:
            # Initial configuration
            print(f"┌─ Step {step_num}: INITIAL STATE")
            print(f"│  Current State: {step['current_state']}")
            print(f"│  Input String:  '{step['remaining_input']}'")
            print(f"└─ Ready to process...\n")
            
        elif step['is_final_step']:
            # Final result
            accepted = step['accepted']
            symbol = "✓" if accepted else "✗"
            result = "ACCEPTED" if accepted else "REJECTED"
            print(f"┌─ Step {step_num}: FINAL RESULT")
            print(f"│  Final State: {step['current_state']}")
            print(f"│  In Accept States: {step['current_state'] in dfa.final_states}")
            print(f"└─ {symbol} STRING {result}")
            
        else:
            # Transition step
            print(f"┌─ Step {step_num}: TRANSITION")
            print(f"│  Read Symbol:   '{step['symbol']}'")
            print(f"│  Current State: {step['current_state']}")
            print(f"│  Next State:    {step['next_state']}")
            print(f"│  Transition:    δ({step['current_state']}, '{step['symbol']}') → {step['next_state']}")
            print(f"│  Processed:     '{step['processed_input']}'")
            print(f"│  Remaining:     '{step['remaining_input']}'")
            print(f"└─\n")


def print_compact_trace(dfa, input_string):
    """Print a compact table-style trace."""
    print(f"\nCompact Trace for: '{input_string}'")
    print("-" * 75)
    print(f"{'Step':<6} {'Symbol':<8} {'From':<8} {'To':<8} {'Processed':<15} {'Remaining':<15}")
    print("-" * 75)
    
    for step in trace_execution(dfa, input_string):
        step_num = step['step_number']
        
        if step['symbol'] is None and not step['is_final_step']:
            print(f"{step_num:<6} {'START':<8} {'-':<8} {step['current_state']:<8} "
                  f"{'':<15} '{step['remaining_input']}'")
        elif step['is_final_step']:
            result = "ACCEPT ✓" if step['accepted'] else "REJECT ✗"
            print(f"{step_num:<6} {result:<8} {step['current_state']:<8} {'-':<8} "
                  f"'{step['processed_input']}'")
        else:
            symbol_display = f"'{step['symbol']}'"
            processed_display = f"'{step['processed_input']}'"
            remaining_display = f"'{step['remaining_input']}'"
            print(f"{step_num:<6} {symbol_display:<8} {step['current_state']:<8} "
                  f"{step['next_state']:<8} {processed_display:<15} {remaining_display}")
    
    print("-" * 75)


if __name__ == "__main__":
    # Create DFA that accepts even number of 'a's
    dfa = create_even_a_dfa()
    
    print("DFA: Accepts strings with EVEN number of 'a's over {a, b}")
    print("States: q0 (even - accept), q1 (odd - reject)")
    
    # Example 1: Accepted string
    print_detailed_trace(dfa, "aba")
    
    # Example 2: Rejected string
    print_detailed_trace(dfa, "aaa")
    
    # Example 3: Empty string
    print_detailed_trace(dfa, "")
    
    # Compact traces for multiple strings
    print("\n" + "="*75)
    print("COMPACT TRACE FORMAT - Multiple Examples")
    print("="*75)
    
    test_cases = ["", "a", "aa", "aab", "bba", "aabba"]
    
    for test in test_cases:
        print_compact_trace(dfa, test)
        print()
