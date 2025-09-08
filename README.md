# GUI Markup Tool - CSci 435 Programming Assignment #1

- [Description](#description)
- [Explanation of Solution](#explanation)
- [Preparations](#preparations)
- [Running the program](#running-the-program)

---

## Description

A small tool that highlights the **leaf-level GUI-components** (objects with which a user would typically interact) in a **mobile application** (e.g., Android) screenshot by parsing and processing metadata (in the form of `.xml` files). Since these leaf-level components describe the hierarchical screen structure of the GUI, by highlighting these components, the developers should have an easier time understanding the mobile application's GUI.

## Explanation

I separated the code into four **Python** scripts: `parse_xml.py`, `draw_image.py`, `handle_filenames.py`, and `main.py`. I did this because I thought that separating the helper methods into their respective files would result in a cleaner and more easily understandable codebase.

The empty `__init__.py` files in the `src` and `functions` directories designate them as **Python** packages. This allows for clean, organised imports of helper functions across the project, such as importing `annotate_image` into the `handle_filenames.py` script.

The [Pillow](https://python-pillow.github.io/) library draws on the PNG files, the [os](https://docs.python.org/3/library/os.html) library navigates the filesystem, the [re](https://docs.python.org/3/library/re.html) library finds numbers within a tree of nodes, and [BeautifulSoup](https://pypi.org/project/beauti.ulsoup4/) and [lxml](https://lxml.de/) parse XML files.

The reason why I opted for the [BeautifulSoup](https://pypi.org/project/beautifulsoup4/) and [lxml](https://lxml.de/) libraries instead of other similar libraries, such as the [ElementTree XML API](https://docs.python.org/3/library/xml.etree.elementtree.html) is because of the flexibility of the former two libraries: they can work with imperfect code, and the code logic is easier to understand.

`parse_xml.py` parses an XML file and returns the coordinates of all leaf nodes in the file.

`draw_image.py` draws yellow rectangles on a PNG file based on its given list of coordinates.

`handle_filenames.py` uses the logic of both of the previous Python files to process the XML files in an input directory, annotate the PNG files, and save the annotations as a new PNG file in an output directory.

`main.py` runs the entire operation.

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

See the `data/processed` directory to analyse the annotated PNGs
