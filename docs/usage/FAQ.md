# Frequently Asked Questions (FAQ)

## General Questions

### Q: What is a DFA?
**A:** A Deterministic Finite Automaton (DFA) is a mathematical model of computation that accepts or rejects strings based on a set of rules. It consists of:
- States (circles in the graph)
- Transitions (arrows between states)
- A start state (green with arrow)
- Final/accept states (double circles)
- An alphabet (valid input symbols)

---

### Q: What can I do with this simulator?
**A:** You can:
- Load DFAs from JSON files
- Test if strings are accepted or rejected
- Step through execution one transition at a time
- See visual highlighting of current state and transition
- Create and export your own DFAs
- Learn how DFAs work interactively

---

### Q: Do I need programming knowledge?
**A:** No! The GUI applications are designed for anyone to use. However, creating custom DFAs requires understanding JSON format (which is simple and documented).

---

## Installation Questions

### Q: What do I need to install?
**A:** 
- **Core functionality**: Just Python 3.7+
- **GUI applications**: Python 3.7+ plus PyQt5, matplotlib, and networkx

See [Installation Guide](../setup/INSTALLATION.md) for details.

---

### Q: Can I use it without installing packages?
**A:** Yes! The core `dfa.py` works without any additional packages. You just won't have the GUI visualizers.

---

### Q: Installation failed, what do I do?
**A:** 
1. Check Python version: `python --version` (need 3.7+)
2. Try: `pip install --user PyQt5 matplotlib networkx`
3. See [Installation Guide - Troubleshooting](../setup/INSTALLATION.md#troubleshooting)

---

## Usage Questions

### Q: How do I load a DFA?
**A:** 
1. Click "📁 Load DFA" button
2. Navigate to a JSON file
3. Select and open it
4. DFA appears in the graph

---

### Q: What are the example DFAs?
**A:**
- `even_a_dfa.json` - Accepts strings with even number of 'a's
- `ends_with_ab.json` - Accepts strings ending with "ab"
- `divisible_by_3.json` - Accepts binary numbers divisible by 3
- `odd_b_dfa.json` - Accepts strings with odd number of 'b's

---

### Q: How do I test a string?
**A:**
1. Load a DFA first
2. Enter string in input field
3. Click "▶ Run / Reset"
4. Click "⏭ Next Step" to step through
5. Or click "⏯ Auto Play" for automatic stepping

---

### Q: What does "Invalid symbol" mean?
**A:** You entered a symbol that's not in the DFA's alphabet. Check the DFA info panel to see valid symbols.

---

### Q: Can I go backwards through execution?
**A:** Yes! Click the "⏮ Previous" button to go back one step.

---

### Q: How do I clear the loaded DFA?
**A:** Click the "🗑️ Clear" button next to the Load button. Confirm when prompted.

---

## Visual Questions

### Q: What do the colors mean?
**A:**
- **Blue**: Regular state
- **Green**: Start state (with arrow)
- **Red/Coral**: Final/accept state (double circle)
- **Gold**: Current state (during execution)
- **Red arrow**: Current transition (during execution)

---

### Q: What is the gold circle?
**A:** The gold circle with orange border shows the current state during step-by-step execution.

---

### Q: What is the red arrow?
**A:** The thick red arrow shows the transition being taken in the current step.

---

### Q: Why are some states double circles?
**A:** Double circles indicate final/accept states. If execution ends in one of these, the string is accepted.

---

### Q: Where is the legend?
**A:** The legend is in the left control panel at the bottom, labeled "Visual Guide".

---

### Q: Graph is too small, can I make it bigger?
**A:** Yes! Maximize the window or go fullscreen. The graph will use all available space.

---

## Technical Questions

### Q: What format are the DFA files?
**A:** JSON format. See [JSON Schema](../technical/JSON_SCHEMA.md) for complete specification.

---

### Q: Can I create my own DFA?
**A:** Yes! Create a JSON file following the schema, or use Python code with `export_dfa_to_json()`.

---

### Q: How do I export a DFA?
**A:** Use Python code:
```python
from dfa import export_dfa_to_json
export_dfa_to_json(my_dfa, "filename.json")
```

---

### Q: Can I edit a DFA?
**A:** Yes, edit the JSON file directly with any text editor. Then reload it in the visualizer.

---

### Q: What's the maximum DFA size?
**A:** No hard limit, but visualization works best with < 20 states. Larger DFAs may be cluttered.

---

## Troubleshooting Questions

### Q: "No DFA loaded" error?
**A:** You need to load a DFA first. Click "📁 Load DFA" and select a JSON file.

---

### Q: Graph looks cluttered?
**A:** Try:
- Maximize the window
- Use a simpler DFA
- Check if the DFA is correct

---

### Q: Can't see current state?
**A:** Look for the gold circle with orange border. It's the largest and most visible.

---

### Q: Auto-play is too fast/slow?
**A:** Currently fixed at 800ms per step. Use "Next Step" for manual control at your own pace.

---

### Q: Application won't start?
**A:** 
1. Check Python version
2. Verify packages installed: `pip list`
3. Try: `python -m pip install --force-reinstall PyQt5`
4. See [Installation Guide](../setup/INSTALLATION.md)

---

### Q: Content hidden in fullscreen?
**A:** This was fixed in recent updates. The left panel now scrolls automatically. Update to latest version.

---

## Feature Questions

### Q: Can I save my work?
**A:** The DFA JSON files are your saved work. Test results aren't saved, but you can export DFAs.

---

### Q: Is there an undo button?
**A:** Not currently. Use "Previous" button to go back during execution, or "Clear" to reset.

---

### Q: Can I compare two DFAs?
**A:** Yes! Load first DFA, test strings, note results. Click "Clear", load second DFA, test same strings, compare.

---

### Q: Can I export the graph as an image?
**A:** Not directly in the GUI. Use `visualization_demo.py` to create static images.

---

### Q: Are there keyboard shortcuts?
**A:** Currently only Enter (in input field) to run. More shortcuts may be added in future.

---

### Q: Can I change the colors?
**A:** Not in the GUI. You can modify the Python code to change colors. See source code comments.

---

## Learning Questions

### Q: I'm new to DFAs, where do I start?
**A:** 
1. Read [Quick Start](../QUICKSTART.md)
2. Load `even_a_dfa.json`
3. Test simple strings like "a", "aa", "aaa"
4. Use step-by-step to see how it works
5. Read [User Guide](USER_GUIDE.md)

---

### Q: How do I understand why a string is rejected?
**A:** 
1. Load the DFA
2. Enter the string
3. Click "Run"
4. Step through execution
5. Watch which state it ends in
6. Check if that state is a final state (double circle)

---

### Q: What's a good way to learn?
**A:**
1. Start with simple DFAs (2-3 states)
2. Test many different strings
3. Use step-by-step mode
4. Try to predict results before testing
5. Create your own simple DFAs

---

### Q: Can I use this for teaching?
**A:** Absolutely! It's designed for education. Use Auto-Play for demonstrations, step-by-step for detailed explanations.

---

## Advanced Questions

### Q: Can I use this programmatically?
**A:** Yes! Import the `dfa` module and use the classes and functions directly in Python.

---

### Q: Can I integrate this into my project?
**A:** Yes! The code is modular. Use `dfa.py` as a library in your own projects.

---

### Q: Can I modify the source code?
**A:** Yes! The code is well-documented. See [System Architecture](../technical/SYSTEM_ARCHITECTURE.md) for details.

---

### Q: Can I add new features?
**A:** Yes! The code is extensible. Common additions: NFA support, minimization, regex conversion.

---

## Performance Questions

### Q: Is it fast enough for large DFAs?
**A:** Yes for computation. Visualization may be slow for > 20 states due to graph layout.

---

### Q: Can I test very long strings?
**A:** Yes! String processing is O(n) where n is string length. Very efficient.

---

### Q: Does it work on slow computers?
**A:** Yes! Minimal requirements. GUI may be slower on very old hardware.

---

## Platform Questions

### Q: Does it work on Windows?
**A:** Yes! Tested on Windows 7+.

---

### Q: Does it work on Mac?
**A:** Yes! Works on macOS 10.12+.

---

### Q: Does it work on Linux?
**A:** Yes! Works on all modern Linux distributions.

---

### Q: Does it work on tablets/phones?
**A:** No, it's a desktop application. Requires Python and GUI packages.

---

## Getting Help

### Q: Where can I find more help?
**A:** 
- [User Guide](USER_GUIDE.md) - Complete usage instructions
- [Examples](EXAMPLES.md) - Usage examples
- [Installation Guide](../setup/INSTALLATION.md) - Setup help
- Error messages - Read them carefully, they're descriptive

---

### Q: How do I report a bug?
**A:** Document the issue with:
- What you did
- What you expected
- What actually happened
- Error messages
- DFA file (if relevant)

---

### Q: Can I request features?
**A:** Yes! Common requests: keyboard shortcuts, adjustable speed, export images, undo/redo.

---

## Still Have Questions?

If your question isn't answered here:
1. Check the [User Guide](USER_GUIDE.md)
2. Try the [Examples](EXAMPLES.md)
3. Review error messages carefully
4. Try with a simpler test case
5. Check the [Installation Guide](../setup/INSTALLATION.md)

---

**Most questions are answered in the documentation. Take time to explore!**
