from enum import Enum
from pathlib import Path


class Platforms(str, Enum):
    WINDOWS = "windows"
    LINUX = "linux"
    MACOS = "macos"
    UNKNOWN = "unknown"


COMMANDS_DIRECTORY = Path(__file__).parent / "commands"

CXX_COMPILER = "clang++"
C_COMPILER = "clang"
EXPORT_COMPILE_COMMANDS = True

BUILD_DIRECTORY = "build"
BINARY_NAME = "application"
