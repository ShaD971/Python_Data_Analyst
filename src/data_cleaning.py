"""Fonctions simples de nettoyage de DataFrames."""

import re
import unicodedata
from collections.abc import Mapping

import pandas as pd


def normalize_column_names(dataframe: pd.DataFrame) -> pd.DataFrame:
    """Retourne une copie dont les colonnes suivent la convention snake_case."""
    cleaned = dataframe.copy()
    normalized: list[str] = []
    for column in cleaned.columns:
        text = unicodedata.normalize("NFKD", str(column))
        text = text.encode("ascii", "ignore").decode("ascii").lower().strip()
        normalized.append(re.sub(r"[^a-z0-9]+", "_", text).strip("_"))
    cleaned.columns = normalized
    return cleaned


def remove_duplicates(dataframe: pd.DataFrame) -> pd.DataFrame:
    """Retourne une copie sans lignes dupliquées, avec un index continu."""
    return dataframe.drop_duplicates().reset_index(drop=True)


def fill_missing_values(
    dataframe: pd.DataFrame, values: Mapping[str, object]
) -> pd.DataFrame:
    """Remplit les valeurs manquantes sans modifier le DataFrame d'origine."""
    unknown = set(values) - set(dataframe.columns)
    if unknown:
        raise KeyError(f"Colonnes inconnues : {sorted(unknown)}")
    return dataframe.fillna(dict(values))
