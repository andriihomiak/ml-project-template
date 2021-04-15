from argparse import ArgumentParser
from pathlib import Path
import yaml


def train(data_folder: Path, splits_folder: Path, model_file: Path, params: dict):
    model_file.parent.mkdir(exist_ok=True, parents=True)
    model_file.write_text("dummy model")


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--data", type=Path, required=True)
    parser.add_argument("--splits", type=Path, required=True)
    parser.add_argument("--output-file", type=Path, required=True)
    args = parser.parse_args()
    params = yaml.safe_load(Path("params.yaml").read_text())["train"]
    train(data_folder=args.data,
          splits_folder=args.splits,
          model_file=args.output_file,
          params=params)
