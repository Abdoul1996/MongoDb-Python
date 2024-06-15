# Automation files for Project development 
import os 
from pathlib import Path

package_name = "mongodb_connect"

# List of files 
list_of_files = [
    ".github/workflows/.gitkeep",
    "src/__init__.py",
    f"src/{package_name}/__init__.py",
    f"src/{package_name}/mongo_crud.py",
    "tests/unit/__init__.py",
      "tests/unit/unit.py",
    "tests/Integration/__init__.py",
    "tests/Integration/int.py",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "experiment/experiments.ipynb"
]

for filepath in list_of_files:
    filepath = Path(filepath)  # Convert to pathlib.Path for better handling
    filedir = filepath.parent  # Get the parent directory
    os.makedirs(filedir, exist_ok=True)  # Ensure parent directories exist
    
    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
        with open(filepath, "w") as f:
            pass  # Create an empty file if it doesn't exist or is empty