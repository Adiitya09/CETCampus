"""
Package proxy shim: Allows `uvicorn backend.app.main:app` or `import backend.app`
to resolve seamlessly even when commands are run directly from inside the `backend/` directory.
"""
from pathlib import Path

__path__ = [str(Path(__file__).resolve().parent)]
