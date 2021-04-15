from argparse import ArgumentParser
from pathlib import Path


def prepare_data(input_folder: Path, output_folder: Path):
    output_folder.mkdir(exist_ok=True, parents=True)
    (output_folder/"prepared_data.txt").write_text("prepared_data")


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("input_folder", type=Path)
    parser.add_argument("output_folder", type=Path)
    args = parser.parse_args()
    prepare_data(input_folder=args.input_folder,
                 output_folder=args.output_folder)
