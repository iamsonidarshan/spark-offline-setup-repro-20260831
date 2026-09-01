.PHONY: setup

PROFILE ?= local

setup:
	@/usr/bin/python3 tools/bootstrap.py --workspace-profile "$(PROFILE)"
