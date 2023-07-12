run-parser:
	@poetry run python scripts/parser/parser.py

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