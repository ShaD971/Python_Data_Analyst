import pandas as pd
import pytest

from src.data_cleaning import (
    fill_missing_values,
    normalize_column_names,
    remove_duplicates,
)


def test_remove_duplicates_preserves_types() -> None:
    source = pd.DataFrame({"id": [1, 1, 2], "label": ["a", "a", "b"]})
    result = remove_duplicates(source)
    assert len(result) == 2
    assert result.dtypes.to_dict() == source.dtypes.to_dict()


def test_fill_missing_values_without_mutation() -> None:
    source = pd.DataFrame({"score": [1.0, None], "group": ["a", None]})
    result = fill_missing_values(source, {"score": 0.0, "group": "inconnu"})
    assert result.isna().sum().sum() == 0
    assert source.isna().sum().sum() == 2
    assert result["score"].dtype == source["score"].dtype


def test_fill_missing_values_rejects_unknown_column() -> None:
    with pytest.raises(KeyError, match="Colonnes inconnues"):
        fill_missing_values(pd.DataFrame({"a": [None]}), {"b": 0})


def test_normalize_column_names() -> None:
    source = pd.DataFrame(columns=["Prénom Client", "Total (€)", " Déjà-vu "])
    result = normalize_column_names(source)
    assert result.columns.tolist() == ["prenom_client", "total", "deja_vu"]
