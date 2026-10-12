"""015 per-page PDF preview; generated pages do not certify actual review."""
from pathlib import Path
import importlib.util
ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT.parents[1]/'蔡题020/整理版/scripts/preview_working_pages.py'
spec=importlib.util.spec_from_file_location('preview_rules020',SOURCE)
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);module.ROOT=ROOT
if __name__=='__main__':module.main()
