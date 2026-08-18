# QCoder Contest Solutions 

This repository contains my solutions and circuit implementations for quantum coding challenges and contests on [QCoder](https://qcoder.com).

All solutions are implemented in Python using **Qiskit** and verified against target statevectors and unitaries.




##  Environment Setup & Installation

To run and verify the solutions locally:

### 1. Clone the repository
```bash
git clone https://github.com/<YOUR_USERNAME>/qcoder-solutions.git
cd qcoder-solutions
```

### 2. Create and activate a virtual environment
```bash
# Create virtual environment
python -m venv .venv

# Activate on Windows (PowerShell)
.\.venv\Scripts\Activate.ps1

# Activate on Linux / macOS
source .venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

---

##  Running a Solution

You can run any solution script directly with Python:

```bash
python "Contest 002/A1 Generate State.py"
```

Each script outputs the circuit diagram and validates the generated statevector against the problem requirements.
