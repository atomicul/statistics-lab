.PHONY: help install check fix clean run

help:
	@echo "Available commands:"
	@echo "  make install         - Sync virtual environment and dependencies using uv"
	@echo "  make check           - Run ruff format check, ruff linter, and pyright"
	@echo "  make fix             - Auto-format code and apply safe lint fixes"
	@echo "  make clean           - Remove cache directories, bytecode, and temp files"
	@echo "  make run file=X.py   - Run a specific script (e.g. make run file=lab1.py)"

install:
	uv sync

check:
	uv run ruff format --check
	uv run ruff check
	uv run pyright

fix:
	uv run ruff format
	uv run ruff check --fix

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.py[co]" -delete
	rm -rf .ruff_cache .pytest_cache dist build *.egg-info

run:
ifndef file
	$(error Missing file parameter. Usage: make run file=<script_name>.py)
endif
	uv run python $(file)
