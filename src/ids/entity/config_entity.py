from pathlib import Path
from dataclasses import dataclass

@dataclass(frozen=True)
class DataIngestionConfig:
    data_source: Path
    train_data_path: Path
    test_data_path: Path