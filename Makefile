all: test

# The @ makes sure that the command itself isn't echoed in the terminal
help:
	@echo "---------------HELP-----------------"
	@echo "To setup the project type make install"
	@echo "To test the project type make test"
	@echo "To check lint type make lint"
	@echo "To format the project type make format"
	@echo "To release a new version type make release"
	@echo "------------------------------------"

lint: FORCE
	@flake8
	@black --check .
	@isort --check .

format: FORCE
	@black .
	@isort .

install: FORCE
	@pip install -e .[dev,docs]

doctest: FORCE
	$(MAKE) -C docs doctest

test: lint FORCE
	@pytest -v

clean: FORCE
	@rm -rf docs/build
	@rm -r .pytest_cache
	@rm -r coverage.xml
	@rm -r .coverage
	@rm -r cricketbackend.egg-info

docs: FORCE
	$(MAKE) -C docs html

release: check_release
	@bump2version ${rule} --verbose
	@git push --tags
	@git push

check_release:
	@echo "Are you sure? [y/N]" && read ans && [ $${ans:-N} = y ]

FORCE: