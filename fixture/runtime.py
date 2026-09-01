"""Resolve the compatibility stamp supplied to the Spark task environment."""

import os


TOKEN_NAME_PARTS = ("GOOGLE", "WORKSPACE", "CLI", "TOKEN")
TOKEN_NAME = "_".join(TOKEN_NAME_PARTS)


def workspace_stamp() -> str:
    return os.environ.get(TOKEN_NAME, "")
