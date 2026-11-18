"""Run every plot script in this folder and write all PNGs to images/08-statistics/."""
import runpy
from pathlib import Path

here = Path(__file__).resolve().parent
for script in sorted(here.glob("[0-9][0-9]_*.py")):
    print("running", script.name)
    runpy.run_path(str(script), run_name="__main__")
