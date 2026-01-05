import sys
import os
project_root=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)


from src.boston import model_reg_boston

def test_ac():
    assert model_reg_boston("BostonHousing.csv")>0.7


