"""Cleanup helper for the project.
Removes __pycache__ directories and .pyc files under the project folder.

Usage:
    python clean_project.py
"""
import shutil
from pathlib import Path


def clean(root: Path) -> None:
    removed = 0
    for p in root.rglob('__pycache__'):
        try:
            shutil.rmtree(p)
            removed += 1
            print(f"Removed directory: {p}")
        except Exception as e:
            print(f"Failed to remove {p}: {e}")

    for p in root.rglob('*.pyc'):
        try:
            p.unlink()
            removed += 1
            print(f"Removed file: {p}")
        except Exception as e:
            print(f"Failed to remove {p}: {e}")

    print(f"Cleanup complete — {removed} items removed.")


if __name__ == '__main__':
    project_root = Path(__file__).parent
    clean(project_root)
