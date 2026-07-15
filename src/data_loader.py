"""Chargement fiable des données tabulaires."""

from pathlib import Path

import pandas as pd


def load_csv(path: str | Path, **kwargs: object) -> pd.DataFrame:
    """Charge un CSV et fournit un message clair si le fichier est absent.

    Les options supplémentaires sont transmises à :func:`pandas.read_csv`.
    """
    csv_path = Path(path)
    if not csv_path.is_file():
        raise FileNotFoundError(f"Fichier CSV introuvable : {csv_path}")
    return pd.read_csv(csv_path, **kwargs)
