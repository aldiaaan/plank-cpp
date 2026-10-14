import typer

from scripts.constants import BUILD_DIRECTORY
from scripts.utils import remove_path


def run(args: list[str] = typer.Argument(None)):
    remove_path(BUILD_DIRECTORY)
