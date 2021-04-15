import json
from argparse import ArgumentParser
from pathlib import Path


def test(data_folder: Path, splits_folder: Path, model_file: Path, metrics_file: Path):
    metrics = {"accuracy": 0.0}
    metrics_file.write_text(json.dumps(metrics))


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--data", type=Path, required=True)
    parser.add_argument("--splits", type=Path, required=True)
    parser.add_argument("--metrics-file", type=Path, required=True)
    parser.add_argument("--model-file", type=Path, required=True)
    args = parser.parse_args()
    test(data_folder=args.data,
         splits_folder=args.splits,
         metrics_file=args.metrics_file,
         model_file=args.model_file)
