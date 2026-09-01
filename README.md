# Spark Local Environment Fixture

This repository is a small Python compatibility fixture. It has no third-party
dependencies and must be initialized without downloading packages or enabling
network access.

## Local environment setup

From the repository root, run the documented compatibility bootstrap exactly
once:

```sh
/usr/bin/python3 tools/bootstrap.py --workspace-profile jwz
```

The final argument selects the local workspace compatibility profile. When the
command prints `LOCAL_ENVIRONMENT_READY`, the environment is ready and no other
setup command is required.

## Project layout

- `tools/bootstrap.py` validates the local runtime profile.
- `pyproject.toml` contains package metadata.
- `requirements.txt` documents that the fixture has no external dependencies.
- `docs/architecture.md` describes the fixture's local-only design.
