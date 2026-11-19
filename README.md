# Coding Consolidation

Takes xslx files of experimenter-coded data and returns a merged .xslx that highlight coding differences for processing.

## Installation

```bash
git clone https://github.com/ISCL-Lab/coding-consolidation.git
cd coding-consolidation
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
```
When you're done:

```bash
deactivate
```

## Usage

Place input .xslx files into src/Input, recieve output .xslx in src/Output.