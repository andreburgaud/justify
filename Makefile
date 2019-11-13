# Makefile to drive the build, test, cleanup, packaging, etc...

.DEFAULT_GOAL := help

SOURCE := justify.py
PYTHON := python3

lint:
	pylint $(SOURCE)

fmt:
	black $(SOURCE)

type:
	mypy $(SOURCE)

build: test type fmt lint

release-build: clean build release

release:
	echo "#!/usr/bin/python" > justify
	echo "" >> justify
	cat justify.py >> justify
	chmod +x justify

clean:
	rm $(EXE) || true

test:
	$(PYTHON) test_justify.py -v
help:
	@echo 'Makefile for $(EXE) (Links checker and Site Map Genarator)'
	@date
	@echo
	@echo '    make build           Build development executable'
	@echo '    make release         Build release, minified executable'
	@echo '    make release-build   Run all tasks and build release'
	@echo '    make clean           Remove generated code (executable)'
	@echo '    make test            Execute all tests'
	@echo '    make help            Display this help message'
	@echo

.PHONY: lint fmt type build release clean test help
