set windows-shell := ["powershell.exe", "-NoLogo", "-Command"]

format:
    uv run ruff format scripts/
    uv run ruff check --fix scripts/

cli *args:
    @uv run python -m scripts {{ args }}
