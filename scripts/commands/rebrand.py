from typing import Annotated

import typer

from scripts.utils import run_command


def run(name: Annotated[str, typer.Argument(help="The new brand name")]):
    pass
