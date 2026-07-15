"""Agrégations utilisées dans les analyses pédagogiques."""

import pandas as pd


def summarize_by_category(
    dataframe: pd.DataFrame, category: str, value: str
) -> pd.DataFrame:
    """Calcule effectif, moyenne et médiane d'une mesure par catégorie."""
    return (
        dataframe.groupby(category, dropna=False)[value]
        .agg(observations="count", moyenne="mean", mediane="median")
        .reset_index()
    )
