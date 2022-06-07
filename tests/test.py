import sys
sys.path.insert(0, 'C:/Users/na_to/OneDrive/Bureau/Insa/Mapromo/Gestion de projet/arendre/src')

from train import get_feat_and_target

import pandas as pd

def test_get_feat_and_target():
    df = pd.DataFrame(columns=['A', 'B', 'C'])
    target = 'B'
    x, y = get_feat_and_target(df, target)
    assert all([a == b for a, b in zip(x.columns, ['A','C'])])
    assert all([a == b for a, b in zip(y.columns, ['B'])])
