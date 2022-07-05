import argparse

# parse command-line arguments
parser = argparse.ArgumentParser(
    description="""CLI tool that finds phrases in a given text file.
    Returns the top unique 5 matched words."""
)
parser.add_argument(
    "file_path",
    help="Text file path.",
)
parser.add_argument(
    "phrase",
    type=string,
    help="Search phrase.")
args = parser.parse_args()
