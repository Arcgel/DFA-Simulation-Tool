import json


class DFA:
    """
    Deterministic Finite Automaton (DFA) Simulator
    
    A DFA is defined by the 5-tuple (Q, Σ, δ, q0, F) where:
    - Q: Set of states
    - Σ: Alphabet (set of input symbols)
    - δ: Transition function (Q × Σ → Q)
    - q0: Start state
    - F: Set of final/accept states
    """
    
    def __init__(self, states, alphabet, transitions, start_state, final_states):
        """
        Initialize a DFA.
        
        Args:
            states: Set of state names (Q)
            alphabet: Set of input symbols (Σ)
            transitions: Dict mapping (state, symbol) -> next_state (δ)
            start_state: Initial state (q0)
            final_states: Set of accepting states (F)
        """
        self.states = set(states)
        self.alphabet = set(alphabet)
        self.transitions = transitions
        self.start_state = start_state
        self.final_states = set(final_states)
        
        # Validate the DFA
        self._validate()
    
    def _validate(self):
        """Validate that the DFA is well-formed."""
        if self.start_state not in self.states:
            raise ValueError(f"Start state {self.start_state} not in states")
        
        if not self.final_states.issubset(self.states):
            raise ValueError("Final states must be subset of states")
        
        # Check that transition function is complete
        for state in self.states:
            for symbol in self.alphabet:
                if (state, symbol) not in self.transitions:
                    raise ValueError(f"Missing transition for ({state}, {symbol})")
                if self.transitions[(state, symbol)] not in self.states:
                    raise ValueError(f"Invalid transition target for ({state}, {symbol})")
    
    def process(self, input_string):
        """
        Process an input string and return whether it's accepted.
        
        Args:
            input_string: String to process
            
        Returns:
            True if the string is accepted, False otherwise
        """
        current_state = self.start_state
        
        for symbol in input_string:
            if symbol not in self.alphabet:
                raise ValueError(f"Symbol '{symbol}' not in alphabet")
            
            current_state = self.transitions[(current_state, symbol)]
        
        return current_state in self.final_states
    
    def process_with_trace(self, input_string):
        """
        Process an input string and return the trace of states visited.
        
        Args:
            input_string: String to process
            
        Returns:
            Tuple of (accepted, trace) where trace is list of states visited
        """
        current_state = self.start_state
        trace = [current_state]
        
        for symbol in input_string:
            if symbol not in self.alphabet:
                raise ValueError(f"Symbol '{symbol}' not in alphabet")
            
            current_state = self.transitions[(current_state, symbol)]
            trace.append(current_state)
        
        accepted = current_state in self.final_states
        return accepted, trace
    
    def __str__(self):
        """String representation of the DFA."""
        return (f"DFA(\n"
                f"  States: {self.states}\n"
                f"  Alphabet: {self.alphabet}\n"
                f"  Start: {self.start_state}\n"
                f"  Final: {self.final_states}\n"
                f"  Transitions: {len(self.transitions)} rules\n"
                f")")


def is_accepted(dfa, input_string):
    """
    Core DFA simulation logic - determines if a string is accepted.
    
    Args:
        dfa: A DFA object with states, alphabet, transitions, start_state, and final_states
        input_string: The string to process
        
    Returns:
        True if the string is accepted by the DFA, False otherwise
        
    Raises:
        ValueError: If a symbol in the input string is not in the DFA's alphabet
    """
    # Start at the initial state
    current_state = dfa.start_state
    
    # Process each symbol in the input string
    for i, symbol in enumerate(input_string):
        # Error handling: check if symbol is in alphabet
        if symbol not in dfa.alphabet:
            raise ValueError(
                f"Invalid symbol '{symbol}' at position {i}. "
                f"Symbol not in alphabet {dfa.alphabet}"
            )
        
        # Apply transition function: δ(current_state, symbol) → next_state
        current_state = dfa.transitions[(current_state, symbol)]
    
    # Check if final state is an accept state
    return current_state in dfa.final_states


def export_dfa_to_json(dfa, filename):
    """
    Export a DFA object to a JSON file.
    
    JSON Schema:
    {
        "states": ["q0", "q1", ...],
        "alphabet": ["a", "b", ...],
        "transitions": {
            "q0,a": "q1",
            "q0,b": "q0",
            ...
        },
        "start_state": "q0",
        "final_states": ["q0", ...]
    }
    
    Args:
        dfa: A DFA object to export
        filename: Path to the JSON file to create
        
    Returns:
        None
        
    Raises:
        IOError: If file cannot be written
    """
    # Convert DFA to JSON-serializable dictionary
    dfa_dict = {
        "states": sorted(list(dfa.states)),
        "alphabet": sorted(list(dfa.alphabet)),
        "transitions": {
            f"{state},{symbol}": next_state
            for (state, symbol), next_state in dfa.transitions.items()
        },
        "start_state": dfa.start_state,
        "final_states": sorted(list(dfa.final_states))
    }
    
    # Write to JSON file with pretty formatting
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(dfa_dict, f, indent=2, ensure_ascii=False)
        print(f"✓ DFA exported successfully to '{filename}'")
    except IOError as e:
        raise IOError(f"Failed to write DFA to file '{filename}': {e}")


def import_dfa_from_json(filename):
    """
    Import a DFA object from a JSON file.
    
    Expected JSON Schema:
    {
        "states": ["q0", "q1", ...],
        "alphabet": ["a", "b", ...],
        "transitions": {
            "q0,a": "q1",
            "q0,b": "q0",
            ...
        },
        "start_state": "q0",
        "final_states": ["q0", ...]
    }
    
    Args:
        filename: Path to the JSON file to load
        
    Returns:
        DFA object constructed from the JSON data
        
    Raises:
        IOError: If file cannot be read
        ValueError: If JSON is invalid or DFA structure is malformed
        json.JSONDecodeError: If file contains invalid JSON
    """
    # Read JSON file
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            dfa_dict = json.load(f)
    except IOError as e:
        raise IOError(f"Failed to read file '{filename}': {e}")
    except json.JSONDecodeError as e:
        raise json.JSONDecodeError(f"Invalid JSON in file '{filename}': {e.msg}", e.doc, e.pos)
    
    # Validate required fields
    required_fields = ["states", "alphabet", "transitions", "start_state", "final_states"]
    missing_fields = [field for field in required_fields if field not in dfa_dict]
    
    if missing_fields:
        raise ValueError(f"Missing required fields in JSON: {missing_fields}")
    
    # Extract and validate data
    try:
        states = set(dfa_dict["states"])
        alphabet = set(dfa_dict["alphabet"])
        start_state = dfa_dict["start_state"]
        final_states = set(dfa_dict["final_states"])
        
        # Convert transitions from "state,symbol" format to (state, symbol) tuple keys
        transitions = {}
        for key, next_state in dfa_dict["transitions"].items():
            parts = key.split(',', 1)
            if len(parts) != 2:
                raise ValueError(f"Invalid transition key format: '{key}'. Expected 'state,symbol'")
            state, symbol = parts
            transitions[(state, symbol)] = next_state
        
        # Validate data types
        if not isinstance(dfa_dict["states"], list):
            raise ValueError("'states' must be a list")
        if not isinstance(dfa_dict["alphabet"], list):
            raise ValueError("'alphabet' must be a list")
        if not isinstance(dfa_dict["transitions"], dict):
            raise ValueError("'transitions' must be a dictionary")
        if not isinstance(dfa_dict["final_states"], list):
            raise ValueError("'final_states' must be a list")
        
        # Create and return DFA (validation happens in DFA.__init__)
        dfa = DFA(states, alphabet, transitions, start_state, final_states)
        print(f"✓ DFA imported successfully from '{filename}'")
        return dfa
        
    except KeyError as e:
        raise ValueError(f"Missing or invalid field in JSON: {e}")
    except Exception as e:
        raise ValueError(f"Error constructing DFA from JSON: {e}")


def trace_execution(dfa, input_string):
    """
    Step-by-step debugger for DFA simulation.
    
    Yields execution steps as the DFA processes the input string.
    Each step contains detailed information about the transition.
    
    Args:
        dfa: A DFA object
        input_string: The string to process
        
    Yields:
        Dictionary containing step information:
        - step_number: The step number (0-indexed)
        - symbol: The symbol being processed (None for initial/final steps)
        - current_state: State before transition
        - next_state: State after transition (None for initial step)
        - remaining_input: Unprocessed portion of input string
        - processed_input: Already processed portion
        - is_final_step: Whether this is the final step
        - accepted: Whether string is accepted (only on final step)
        
    Raises:
        ValueError: If a symbol in the input string is not in the DFA's alphabet
    """
    current_state = dfa.start_state
    
    # Initial step - show starting configuration
    yield {
        'step_number': 0,
        'symbol': None,
        'current_state': current_state,
        'next_state': None,
        'remaining_input': input_string,
        'processed_input': '',
        'is_final_step': False,
        'accepted': None,
        'message': 'Initial configuration'
    }
    
    # Process each symbol
    for i, symbol in enumerate(input_string):
        # Validate symbol
        if symbol not in dfa.alphabet:
            raise ValueError(
                f"Invalid symbol '{symbol}' at position {i}. "
                f"Symbol not in alphabet {dfa.alphabet}"
            )
        
        # Get next state
        next_state = dfa.transitions[(current_state, symbol)]
        
        # Yield transition step
        yield {
            'step_number': i + 1,
            'symbol': symbol,
            'current_state': current_state,
            'next_state': next_state,
            'remaining_input': input_string[i+1:],
            'processed_input': input_string[:i+1],
            'is_final_step': False,
            'accepted': None,
            'message': f'δ({current_state}, {symbol}) → {next_state}'
        }
        
        # Move to next state
        current_state = next_state
    
    # Final step - show result
    accepted = current_state in dfa.final_states
    yield {
        'step_number': len(input_string) + 1,
        'symbol': None,
        'current_state': current_state,
        'next_state': None,
        'remaining_input': '',
        'processed_input': input_string,
        'is_final_step': True,
        'accepted': accepted,
        'message': f'Final state {current_state} is {"" if accepted else "NOT "}in accept states → {"ACCEPT" if accepted else "REJECT"}'
    }


def create_even_a_dfa():
    """
    Create a DFA that accepts strings with an even number of 'a's.
    
    Language: L = {w ∈ {a,b}* | w contains an even number of 'a's}
    
    States:
    - q0 (even): Even number of 'a's seen (accepting state)
    - q1 (odd): Odd number of 'a's seen
    
    Transitions:
    - From q0: 'a' → q1, 'b' → q0
    - From q1: 'a' → q0, 'b' → q1
    """
    states = {'q0', 'q1'}
    alphabet = {'a', 'b'}
    transitions = {
        ('q0', 'a'): 'q1',  # Even → Odd
        ('q0', 'b'): 'q0',  # Even → Even
        ('q1', 'a'): 'q0',  # Odd → Even
        ('q1', 'b'): 'q1',  # Odd → Odd
    }
    start_state = 'q0'
    final_states = {'q0'}  # Accept when even number of 'a's
    
    return DFA(states, alphabet, transitions, start_state, final_states)


if __name__ == "__main__":
    # Create the DFA for even number of 'a's
    dfa = create_even_a_dfa()
    print(dfa)
    print()
    
    # Test cases
    test_strings = [
        "",           # 0 a's (even) → Accept
        "b",          # 0 a's (even) → Accept
        "a",          # 1 a (odd) → Reject
        "aa",         # 2 a's (even) → Accept
        "ab",         # 1 a (odd) → Reject
        "ba",         # 1 a (odd) → Reject
        "aab",        # 2 a's (even) → Accept
        "aba",        # 2 a's (even) → Accept
        "baa",        # 2 a's (even) → Accept
        "aaa",        # 3 a's (odd) → Reject
        "aaaa",       # 4 a's (even) → Accept
        "bbbbb",      # 0 a's (even) → Accept
        "aabba",      # 3 a's (odd) → Reject
        "aabbaa",     # 4 a's (even) → Accept
    ]
    
    print("Testing with is_accepted() function:")
    print("-" * 60)
    
    for test in test_strings:
        # Use the is_accepted function
        accepted = is_accepted(dfa, test)
        status = "✓ ACCEPT" if accepted else "✗ REJECT"
        a_count = test.count('a')
        print(f"{status:10} | '{test:10}' | {a_count} a's")
    
    print("\n" + "=" * 60)
    print("Testing with process_with_trace() method (shows state transitions):")
    print("-" * 60)
    
    for test in ["", "a", "aa", "aab", "aba"]:
        accepted, trace = dfa.process_with_trace(test)
        status = "✓ ACCEPT" if accepted else "✗ REJECT"
        trace_str = " → ".join(trace)
        print(f"{status:10} | '{test:10}' | {trace_str}")
    
    # Test error handling
    print("\n" + "=" * 60)
    print("Testing error handling for invalid symbols:")
    print("-" * 60)
    
    invalid_strings = ["abc", "a1b", "a b"]
    
    for test in invalid_strings:
        try:
            result = is_accepted(dfa, test)
            print(f"'{test}' → {result}")
        except ValueError as e:
            print(f"'{test}' → ERROR: {e}")
    
    # Test trace_execution debugger
    print("\n" + "=" * 60)
    print("STEP-BY-STEP DEBUGGER - trace_execution() function:")
    print("=" * 60)
    
    debug_strings = ["aba", "aaa", ""]
    
    for test_string in debug_strings:
        print(f"\nDebugging string: '{test_string}'")
        print("-" * 60)
        
        for step in trace_execution(dfa, test_string):
            step_num = step['step_number']
            
            if step['symbol'] is None and not step['is_final_step']:
                # Initial step
                print(f"Step {step_num}: {step['message']}")
                print(f"  State: {step['current_state']}")
                print(f"  Input: '{step['remaining_input']}'")
            elif step['is_final_step']:
                # Final step
                print(f"\nStep {step_num}: {step['message']}")
                result = "✓ ACCEPTED" if step['accepted'] else "✗ REJECTED"
                print(f"  Result: {result}")
            else:
                # Transition step
                print(f"\nStep {step_num}: Read symbol '{step['symbol']}'")
                print(f"  Transition: {step['message']}")
                print(f"  Processed: '{step['processed_input']}'")
                print(f"  Remaining: '{step['remaining_input']}'")
        
        print()
    
    # Detailed trace with table format
    print("=" * 60)
    print("DETAILED TRACE TABLE FORMAT:")
    print("=" * 60)
    
    test_string = "aabba"
    print(f"\nTracing: '{test_string}'")
    print("-" * 80)
    print(f"{'Step':<6} {'Symbol':<8} {'Current':<10} {'Next':<10} {'Processed':<12} {'Remaining':<12}")
    print("-" * 80)
    
    for step in trace_execution(dfa, test_string):
        if step['symbol'] is None and not step['is_final_step']:
            # Initial
            symbol_str = 'START'
            next_str = '-'
            proc_str = ''
            print(f"{step['step_number']:<6} {symbol_str:<8} {step['current_state']:<10} {next_str:<10} "
                  f"'{proc_str}'<12 '{step['remaining_input']}'")
        elif step['is_final_step']:
            # Final
            result = "ACCEPT" if step['accepted'] else "REJECT"
            next_str = '-'
            print(f"{step['step_number']:<6} {result:<8} {step['current_state']:<10} {next_str:<10} "
                  f"'{step['processed_input']}'")
        else:
            # Transition
            symbol_str = f"'{step['symbol']}'"
            print(f"{step['step_number']:<6} {symbol_str:<8} {step['current_state']:<10} "
                  f"{step['next_state']:<10} '{step['processed_input']}'<12 '{step['remaining_input']}'")
    
    print("-" * 80)
