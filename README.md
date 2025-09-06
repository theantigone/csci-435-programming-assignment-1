# CSci 435 Programming Assignment 1

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

Navigate to the `src` directory, then run:
```bash
python main.py <xml_file> <png_file>
```
where `<xml_file>` and `<png_file>` are your `.xml` and `.png` files, respectively.
