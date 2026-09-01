"""Run every repository check with locked tool versions."""

from pathlib import Path
from subprocess import run

ROOT = Path(__file__).parent


def check(*command: str, cwd: Path = ROOT) -> None:
    print(f"\n$ {' '.join(command)}", flush=True)
    run(command, cwd=cwd, check=True)


def main() -> None:
    check("uv", "sync", "--locked", "--group", "dev")
    check("uv", "run", "python", "-m", "unittest", "discover")
    check("uv", "run", "ruff", "check", "check.py", "python", "pyproject.toml")
    check("uv", "run", "ruff", "format", "--check", "check.py", "python", "pyproject.toml")
    check("uv", "run", "pyright")
    check("npm", "ci", cwd=ROOT / "typescript")
    check("npm", "run", "check", cwd=ROOT / "typescript")


if __name__ == "__main__":
    main()
