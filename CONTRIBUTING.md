# Contributing to Track Job Applications

A big welcome and thank you for considering contributing to this project!

Reading and following these guidelines will help us make the contribution process easy and effective for everyone involved. It also communicates that you agree to respect the time of the developers managing and developing these open source projects. In return, we will reciprocate that respect by addressing your issue, assessing changes, and helping you finalize your pull requests.

## Quicklinks

* [Code of Conduct](#code-of-conduct)
* [Getting Started](#getting-started)
    * [Issues](#issues)
    * [Pull Requests](#pull-requests)
* [Setting up the development environment](#setting-up-the-development-environment)
  * [Contributing to Code](#contributing-to-code)
  * [Contributing to Docs](#contributing-to-docs)
* [Pre-commit hooks](#pre-commit-hooks)

## Code of Conduct

We take our open source community seriously and hold ourselves and other contributors to high standards of communication. By participating and contributing to this project, you agree to uphold our [Code of Conduct](https://github.com/Aditya-Gupta/job-application-cli/blob/main/CODE_OF_CONDUCT.md).

## Getting Started

Contributions are made to this repo via Issues and Pull Requests (PRs). A few general guidelines that cover both:

- Search for existing Issues and PRs before creating your own.
- We work hard to makes sure issues are handled in a timely manner but, depending on the impact, it could take a while to investigate the root cause. A friendly ping in the comment thread to the submitter or a contributor can help draw attention if your issue is blocking.

### Issues

Issues should be used to report problems with the library, request a new feature, or to discuss potential changes before a PR is created. When you create a new Issue, a template will be loaded that will guide you through collecting and providing the information we need to investigate.

If you find an Issue that addresses the problem you're having, please add your own reproduction information to the existing issue rather than creating a new one. Adding a [reaction](https://github.blog/2016-03-10-add-reactions-to-pull-requests-issues-and-comments/) can also help be indicating to our maintainers that a particular problem is affecting more than just the reporter.

### Pull Requests

PRs are always welcome and can be a quick way to get your fix or improvement slated for the next release. In general, PRs should:

- Only fix/add the functionality in question **OR** address wide-spread whitespace/style issues, not both.
- Add unit or integration tests for fixed or changed functionality (if a test suite already exists).
- Address a single concern in the least number of changed lines as possible.
- Be accompanied by a complete Pull Request template (loaded automatically when a PR is created).

For changes that address core functionality or would require breaking changes (e.g. a major release), it's best to open an Issue to discuss your proposal first. This is not required but can save time creating and reviewing changes.

In general, we follow the ["fork-and-pull" Git workflow](https://github.com/susam/gitpr)

1. Fork the repository to your own GitHub account
2. Clone the project to your machine
3. Create a branch locally with a succinct but descriptive name
4. Commit changes to the branch
5. Following any formatting and testing guidelines specific to this repo
6. Push changes to your fork
7. Open a PR in our repository and follow the PR template so that we can efficiently review the changes.

## Setting up the development environment

1. Install [Poetry](https://python-poetry.org/docs/#installation). Make sure to add it to the path as mentioned in the documentation.
2. Run the following commands:
```commandline
git clone https://github.com/Aditya-Gupta1/track-job-applications.git
cd track-job-applications
poetry install
poetry shell
```
3. Poetry will spin up a shell where all the commands for the application can be executed and tested.

### Contributing to Code

* Make the necessary code changes as per the issue worked upon.
* Inside the poetry shell, run the command and ensure it's working as expedted.
* Add test cases in the `tests` folder and run it using [Pytest](https://docs.pytest.org/en/7.2.x/).
* Once the tests are running and the changes are working fine, raise a PR.

### Contributing to Docs

* Docs templates are present in the `docs` folder. The markdown files present in the folder are compiled by mkdocs as per the configuration mentioned in the [mkdocs.yml]() file.
* If you need to modify the existing documentation for a method or a class, just modify its docstring in the source code.
* If you need to add documentation for a new method or a class:
  * add docstrings to them in [google style](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html).
  * add the method's or class's path from repository root prefixed by `:::` in any of the markdown files present in the `docs` folder. (You can take reference of how other entities are mentioned there)
* After making the changes, run `mkdocs server` to see a live preview of the docs.
* If everything looks fine, raise a PR.

## Pre-commit hooks

Various pre-commit hooks are executed before every commit to maintain code quality. Here's a list of them:
* [Black](https://github.com/psf/black)
* [Flake](https://flake8.pycqa.org/en/latest/)
* [Isort](https://pycqa.github.io/isort/)
* [Interrogate](https://interrogate.readthedocs.io/en/latest/)
* [Poetry Check](https://python-poetry.org/docs/master/pre-commit-hooks/#poetry-check)
* [Poetry Lock](https://python-poetry.org/docs/master/pre-commit-hooks/#poetry-lock)
* [Poetry Export](https://python-poetry.org/docs/master/pre-commit-hooks/#poetry-export)
