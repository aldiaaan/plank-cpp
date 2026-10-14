import typer

from scripts.constants import BUILD_DIRECTORY
from scripts.utils import run_command


def run(args: list[str] = typer.Argument(None)):
    command = ["cmake", "--build", BUILD_DIRECTORY]

    run_command(command)
