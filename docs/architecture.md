# Architecture

The fixture uses `make`, the Python standard library, and the system `curl`
binary. It does not require package installation, compilation, or generated
files.

Environment setup is represented by one standard Make target from the repository
README. The Makefile delegates to a thin bootstrap which loads the fixture
package. The bootstrap accepts an opaque workspace-profile value so the same
project can be tested against multiple local runtime profiles.
