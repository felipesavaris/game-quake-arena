# Game Quake Arena

This project captures game actions made available in log, structures the result of each game through Parser and provides an API for queries of these results.

## Requirements

To run this project it is necessary to configure the following technologies on the machine.

- [Python >= 3.11](https://www.python.org/)
- [Pyenv](https://github.com/pyenv/pyenv)
- [Poetry](https://python-poetry.org/)
- [Git](https://git-scm.com/)
- [GNU Make](https://www.gnu.org/software/make/)

## Local Environment Setup

Run the commands below to create the virtual environment and install the project dependencies.

```shell
$ pyenv install 3.11
$ pyenv shell 3.11
$ poetry env use 3.11
$ poetry install
```

If you are accessing the project and want to enter the virtual environment, run:

```shell
$ poetry shell
```

After the setup if you want to run your project locally, you can use the command:

```bash
$ make run-parser
```

This command reads the data from the log file, structures the data for each game and saves it in the file "games_results.json".

To run the API in sequence:

```bash
$ make run-api
```

Go to the link "http://127.0.0.1:8000/docs" in your web browser to view the "Swagger" / Open API. In this way, it will be possible to run the endpoints, and check the documentation of each object and return codes. 

## Tests

### Localy

To execute tests, run:

```bash
$ make test
```

To execute an especific test or a collection of tests with common name, run:

```bash
$ make test-matching Q={test_name}
```
