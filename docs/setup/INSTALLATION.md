# DFA Simulator - Installation Guide

## System Requirements

### Software Requirements
- **Python**: 3.7 or higher
- **Operating System**: Windows, macOS, or Linux

### Hardware Requirements
- **CPU**: Any modern processor
- **RAM**: 512MB minimum, 1GB recommended
- **Display**: 1024x768 minimum, 1920x1080 recommended

## Installation Steps

### Step 1: Verify Python Installation

```bash
python --version
```

Should show Python 3.7 or higher.

### Step 2: Core Functionality (No Dependencies)

The core DFA simulator works without any additional packages:

```bash
# Test core functionality
python dfa.py
```

If this works, you can use:
- DFA creation and validation
- String acceptance testing
- Step-by-step execution traces
- JSON import/export

### Step 3: GUI Dependencies (Optional)

For the graphical interface, install these packages:

```bash
pip install PyQt5 matplotlib networkx
```

Or use the requirements file:

```bash
pip install -r requirements.txt
```

### Step 4: Verify Installation

Test the GUI applications:

```bash
# Test interactive debugger
python interactive_debugger.py

# Test basic visualizer
python dfa_visualizer.py
```

## Installation Options

### Option 1: Minimal (Core Only)
**No installation needed!**
- Just Python 3.7+
- Use: `dfa.py` and all demo scripts
- No GUI, but full DFA functionality

### Option 2: Full (With GUI)
**Install GUI packages:**
```bash
pip install PyQt5 matplotlib networkx
```
- Use: All features including GUI
- Interactive debugger
- Visual graph rendering

## Package Details

### PyQt5 (>= 5.15.0)
- **Purpose**: GUI framework
- **Size**: ~50MB
- **Used for**: Windows, buttons, layouts

### matplotlib (>= 3.5.0)
- **Purpose**: Plotting and visualization
- **Size**: ~30MB
- **Used for**: Graph canvas, rendering

### networkx (>= 2.6.0)
- **Purpose**: Graph algorithms
- **Size**: ~5MB
- **Used for**: Graph layout, node positioning

## Troubleshooting

### "No module named 'PyQt5'"

**Solution:**
```bash
pip install PyQt5
```

### "No module named 'matplotlib'"

**Solution:**
```bash
pip install matplotlib
```

### "No module named 'networkx'"

**Solution:**
```bash
pip install networkx
```

### "pip not found"

**Solution:**
```bash
# Windows
python -m pip install PyQt5 matplotlib networkx

# macOS/Linux
python3 -m pip install PyQt5 matplotlib networkx
```

### Permission Errors

**Solution:**
```bash
# Use --user flag
pip install --user PyQt5 matplotlib networkx
```

### Python Version Too Old

**Solution:**
- Download Python 3.7+ from python.org
- Or use conda: `conda install python=3.9`

## Platform-Specific Notes

### Windows
- Use PowerShell or Command Prompt
- May need to add Python to PATH
- PyQt5 works out of the box

### macOS
- Use Terminal
- May need Xcode Command Line Tools
- Use `python3` instead of `python`

### Linux
- Use Terminal
- May need python3-pip: `sudo apt install python3-pip`
- May need python3-tk: `sudo apt install python3-tk`

## Virtual Environment (Recommended)

### Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Install Packages
```bash
pip install PyQt5 matplotlib networkx
```

### Deactivate
```bash
deactivate
```

## Verification Checklist

After installation, verify:

- [ ] `python --version` shows 3.7+
- [ ] `python dfa.py` runs without errors
- [ ] `python interactive_debugger.py` opens GUI (if installed packages)
- [ ] Can load JSON files
- [ ] Can test strings
- [ ] Can step through execution

## Quick Start After Installation

```bash
# 1. Test core functionality
python dfa.py

# 2. Run interactive debugger
python interactive_debugger.py

# 3. Load example DFA
# Click "Load DFA" → Select "even_a_dfa.json"

# 4. Test a string
# Enter "aba" → Click "Run"

# 5. Step through execution
# Click "Next Step" repeatedly
```

## Getting Help

If you encounter issues:
1. Check Python version: `python --version`
2. Check installed packages: `pip list`
3. Try reinstalling: `pip install --force-reinstall PyQt5`
4. Check error messages carefully
5. Verify file paths are correct

## Next Steps

After installation:
- Read [USER_GUIDE.md](../usage/USER_GUIDE.md) for usage instructions
- Try example DFAs in the project folder
- Explore the interactive debugger features

## Uninstallation

To remove the packages:

```bash
pip uninstall PyQt5 matplotlib networkx
```

To remove the project:
- Simply delete the project folder
- No system files are modified
