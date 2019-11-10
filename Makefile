# Makefile to drive the build, test, cleanup, packaging, etc...

.DEFAULT_GOAL := help

SOURCE := justify.py

lint:
	pylint $(SOURCE)

fmt:
	black $(SOURCE)

type:
	mypy $(SOURCE)

build: type fmt lint

release: build
	echo "#!/usr/bin/python" > justify
	cat justify.py >> justify
	chmod +x justify

clean:
	rm $(EXE) || true

test:
	python test_justify.py -v
help:
	@echo 'Makefile for $(EXE) (Links checker and Site Map Genarator)'
	@date
	@echo
	@echo '    make build           Build development executable'
	@echo '    make release         Build release, minified executable'
	@echo '    make clean           Remove generated code (executable)'
	@echo '    make test            Execute all tests'
	@echo '    make help            Display this help message'
	@echo

.PHONY: lint fmt type build release clean test help
