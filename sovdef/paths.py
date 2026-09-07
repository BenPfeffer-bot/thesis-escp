from pathlib import Path


def _find_root(start: Path) -> Path:
    """
    Function to get the main root of the project.
    It ensure its will always find the proper path even if we moves the paths.py file out of the folder
    assert there is no silent break
    """
    for p in [start, *start.parents]:
        if (p / "pyproject.toml").exists():
            return p
    raise FileNotFoundError(
        "Impossible to found the root of the project (missing pyproject.toml)"
    )


# Set ROOT as constant for the path of the project
ROOT = _find_root(Path(__file__).resolve())

# Config
CONFIG = ROOT / "config/"

# Database
DATA = ROOT / "data/"
INTERIM = DATA / "interim/"
PROCESSED = DATA / "processed/"
RAW = DATA / "raw/"
REFERENCE = DATA / "reference/"

# Main codebase
SOVDEF = ROOT / "sovdef/"

# Scripts & Misc.
REPORTS = ROOT / "reports/"
RUNS = ROOT / "runs/"
SCRIPTS = ROOT / "scripts/"

# Explicitly called at the head of the script, never upon import, to prevent creating empty directories if a notebook is run from the wrong path.
_WRITABLE = (INTERIM, PROCESSED, RAW, REPORTS, RUNS)


def ensure_dirs() -> None:
    for d in _WRITABLE:
        d.mkdir(parents=True, exist_ok=True)
