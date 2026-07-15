"""Création de graphiques cohérents et exportables."""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.axes import Axes


def plot_category_comparison(
    summary: pd.DataFrame,
    category: str,
    value: str,
    output_path: str | Path | None = None,
) -> Axes:
    """Trace une comparaison en barres et l'enregistre si demandé."""
    figure, axis = plt.subplots(figsize=(9, 5))
    axis.bar(summary[category].astype(str), summary[value], color="#2878B5")
    axis.set(title="Comparaison par catégorie", xlabel=category, ylabel=value)
    axis.tick_params(axis="x", rotation=30)
    figure.tight_layout()
    if output_path is not None:
        destination = Path(output_path)
        destination.parent.mkdir(parents=True, exist_ok=True)
        figure.savefig(destination, dpi=160, bbox_inches="tight")
    return axis
