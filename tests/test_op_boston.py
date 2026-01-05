import sys
import os
project_root=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)
from pathlib import Path
import pandas as pd

DATA_PATH = Path(__file__).parent / "BostonHousing.csv"

from src.boston import model_reg_boston

def test_ac():
    assert model_reg_boston(DATA_PATH)>=0.6




