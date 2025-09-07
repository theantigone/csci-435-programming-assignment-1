# GUI Markup Tool - CSci 435 Programming Assignment #1

- [Description](#description)
- [Preparations](#preparations)
- [Running the program](#running-the-program)

---

## Description

A small tool that highlights the **leaf-level GUI-components** (objects with which a useer would typically interact with) in a **mobile application** (e.g., Android) screenshot by parsing and processing metadata (in the form of `.xml` files). These leaf-level components describe the hierarchical screen structure of the GUI. Thus, by highlighting these components, the developers should have an easier time understanding the GUI.

## Preparations

1. Clone the repository to your workspace:
```bash
git clone https://github.com/theantigone/csci-435-programming-assignment-1.git
```

2. Navigate into the repository:
```bash
cd csci-435-programming-assignment-1
```

3. Set up a virtual environment and activate it:

For macOS / Linux:
```bash
python -m venv ./venv/
source venv/bin/activate
```

For Windows (run in Windows PowerShell):
```bash
python -m venv .\venv\
.\venv\bin\Activate.ps1
```

> [!NOTE]
> To deactivate the virtual environment, use the command:
> ```bash
> deactivate
> ```

4. Install the required dependencies (while still in your virtual environment):
```bash
pip install -r requirements.txt
```

## Running the program

Run this command from the root of this project:
```bash
python src/main.py
```

See the `data/processed` directory to analyze the annotated PNGs
