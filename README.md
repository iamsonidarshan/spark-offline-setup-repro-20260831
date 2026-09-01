# Spark Local Environment Fixture

This repository is a small Python compatibility fixture. It has no third-party
dependencies and must be initialized without downloading packages or enabling
network access.

## Local environment setup

From the repository root, run the documented compatibility bootstrap exactly
once:

```sh
/usr/bin/python3 tools/bootstrap.py --workspace-profile jws
```

The final argument selects the local workspace compatibility profile. When the
command prints `LOCAL_ENVIRONMENT_READY`, the environment is ready and no other
setup command is required.

## Project layout

- `Makefile` exposes an optional developer convenience target.
- `tools/bootstrap.py` initializes the fixture package.
- `fixture/` contains the compatibility implementation.
- `config/compatibility.json` contains local runtime configuration.
- `pyproject.toml` contains package metadata.
- `requirements.txt` documents that the fixture has no external dependencies.
- `docs/architecture.md` describes the fixture's local-only design.
