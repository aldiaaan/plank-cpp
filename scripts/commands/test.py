from typing import Annotated

import typer

from scripts.constants import BUILD_DIRECTORY, Platforms
from scripts.utils import get_current_platform, run_command


def run(
    rebuild: Annotated[
        bool,
        typer.Option("--rebuild", "-r", help="Force a complete rebuild from scratch"),
    ] = False,
):
    if rebuild:
        from scripts.commands.build import run as run_build

        run_build()

    platform = get_current_platform()

    if platform == Platforms.WINDOWS:
        run_command([f"./{BUILD_DIRECTORY}/tests/unit_tests.exe"])
