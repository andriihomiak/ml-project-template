from argparse import ArgumentParser
from pathlib import Path


def split_data(input_folder: Path, output_folder: Path):
    output_folder.mkdir(exist_ok=True, parents=True)
    (output_folder/"train.txt").write_text("data")
    (output_folder/"test.txt").write_text("data")
    (output_folder/"val.txt").write_text("data")


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("input_folder", type=Path)
    parser.add_argument("output_folder", type=Path)
    args = parser.parse_args()
    split_data(input_folder=args.input_folder,
               output_folder=args.output_folder)
