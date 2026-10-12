from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]
BATCH=ROOT.parent.parent/'复核批次'/'第042—038套'
sys.path.insert(0,str(BATCH/'工具'))
import build
build.build(ROOT,39)
