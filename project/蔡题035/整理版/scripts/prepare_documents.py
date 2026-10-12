from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from tools.document_pipeline import prepare_set

if __name__ == "__main__":
    prepare_set("035")
