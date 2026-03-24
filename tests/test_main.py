import pytest
from src.utils import load_data, features_and_target
import os

def test_load_data():
    path = "data/wine_sample.csv"
    df = load_data(path)
    assert "quality" in df.columns

def test_features_and_target():
    path = "data/wine_sample.csv"
    df = load_data(path)
    X, y = features_and_target(df)
    assert X.shape[0] == y.shape[0]
    assert "quality" not in X.columns
