from pathlib import Path 
import shutil 

from rich import print 
from config import DESTINATION_FOLDERS

def get_category(file_path: Path) -> str | None:
    suffix = file_path.suffix.lower()

    for category, extensions in DESTINATION_FOLDERS.items():
        if suffix in extensions:
            return category
    return None

def make_unique_destination(destination: Path) -> Path:
    if not destination.exists():
        return destination