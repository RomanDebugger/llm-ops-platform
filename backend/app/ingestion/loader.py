from pathlib import Path

def load_text(file_path: str) -> str:
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError

    if path.suffix.lower() == ".txt":
        return path.read_text()

    raise ValueError("Unsupported file type")
