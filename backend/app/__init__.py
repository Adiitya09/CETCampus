import sys
from pathlib import Path

# Ensure project root (parent of 'backend') is in sys.path so 'backend.app' imports
# work seamlessly whether running from project root or inside the backend directory.
_backend_dir = Path(__file__).resolve().parent.parent
_project_root = str(_backend_dir.parent)
if _project_root not in sys.path:
    sys.path.insert(0, _project_root)
