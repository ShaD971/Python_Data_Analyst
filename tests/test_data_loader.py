from pathlib import Path

import pandas as pd
import pytest

from src.data_loader import load_csv


def test_load_valid_csv(tmp_path: Path) -> None:
    path = tmp_path / "sample.csv"
    path.write_text("name,score\nAda,10\n", encoding="utf-8")

    result = load_csv(path)

    pd.testing.assert_frame_equal(
        result, pd.DataFrame({"name": ["Ada"], "score": [10]})
    )
    assert result["score"].dtype.kind in "iu"


def test_load_missing_csv(tmp_path: Path) -> None:
    with pytest.raises(FileNotFoundError, match="introuvable"):
        load_csv(tmp_path / "missing.csv")
