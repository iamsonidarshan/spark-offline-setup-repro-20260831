# Architecture

The fixture uses the Python standard library plus the system `curl` binary. It
does not require package installation, compilation, or generated files.

Environment setup is represented by one compatibility bootstrap command from
the repository README. The bootstrap accepts an opaque workspace-profile value
so the same project can be tested against multiple local runtime profiles.
