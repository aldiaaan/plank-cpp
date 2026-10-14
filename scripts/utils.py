import platform
import shutil
import subprocess
import sys
from pathlib import Path

import typer
from rich import print

from scripts.constants import Platforms


def run_command(cmd: list[str]) -> None:
    print(f"[dim]$ {' '.join(cmd)}[/dim]")
    result = subprocess.run(cmd, check=False)
    if result.returncode != 0:
        print(f"[bold red]Command failed with exit code {result.returncode}[/bold red]")
        raise typer.Exit(code=result.returncode)


def remove_path(target: str | Path) -> None:
    path = Path(target)
    if not path.exists():
        return
    if path.is_dir():
        shutil.rmtree(path, ignore_errors=True)
    else:
        path.unlink(missing_ok=True)


def get_current_platform() -> Platforms:
    system_name = platform.system().lower()

    if system_name == "windows" or sys.platform.startswith("win32"):
        return Platforms.WINDOWS
    elif system_name == "linux" or sys.platform.startswith("linux"):
        return Platforms.LINUX
    elif system_name == "darwin":
        return Platforms.MACOS
    return Platforms.UNKNOWN
