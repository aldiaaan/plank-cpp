import importlib

import typer

from scripts.constants import COMMANDS_DIRECTORY

app = typer.Typer()


if __name__ == "__main__":
    for file_path in COMMANDS_DIRECTORY.glob("*.py"):
        if file_path.name.startswith("__"):
            continue

        module = importlib.import_module(f"scripts.commands.{file_path.stem}")
        if hasattr(module, "run"):
            # print(f"Registering {file_path.stem}")
            app.command(name=file_path.stem)(module.run)  # pyright: ignore[reportAny]
    app()
