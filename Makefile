run-parser:
	@poetry run python -m scripts.parser.parser

run-api:
	@poetry run python -m quake_arena_api.main

blue:
	@poetry run blue .

blue-check:
	@poetry run blue --check .

lint: isort blue

test:
	@poetry run pytest -s

test-matching:
	@poetry run pytest -s -rx -k $(Q) --pdb ./tests/

.PHONY: test isort blue
