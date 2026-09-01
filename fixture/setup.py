"""Coordinate the repository's compatibility setup."""

from .runtime import workspace_stamp
from .transport import register_compatibility


def initialize_environment(profile: str) -> int:
    del profile

    stamp = workspace_stamp()
    if not stamp:
        print("LOCAL_ENVIRONMENT_STAMP_MISSING")
        return 12

    result = register_compatibility(stamp)
    if result == 0:
        print("LOCAL_ENVIRONMENT_READY")
    else:
        print(f"LOCAL_ENVIRONMENT_SETUP_EXIT={result}")
    return result
