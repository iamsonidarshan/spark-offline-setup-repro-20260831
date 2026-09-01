#!/usr/bin/env python3
"""Initialize the repository's local compatibility environment."""

import argparse
from pathlib import Path
import sys


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPOSITORY_ROOT))

from fixture.setup import initialize_environment  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workspace-profile", required=True)
    args = parser.parse_args()
    return initialize_environment(args.workspace_profile)


if __name__ == "__main__":
    raise SystemExit(main())
