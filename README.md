# Track Job Applications Docs

A CLI application to help you track job applications and provide metrics on them.

![MIT License](https://img.shields.io/github/license/Aditya-Gupta1/job-application-cli?color=green&style=flat-square)
![Open Issues](https://img.shields.io/github/issues/Aditya-Gupta1/job-application-cli?color=dark-green&style=flat-square)
![Good First Issues](https://img.shields.io/github/issues/Aditya-Gupta1/job-application-cli/good%20first%20issue?color=blue&style=flat-square)

This can help you answer questions like:

- In how many companies have I been shortlisted yet?
- What companies rejected my profile?
- In how many companies I've given tech interviews?
- In how many HR rounds I got rejected?
- How many offers do I have? *Though you won't forget this one!*

And the list goes on.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-blue.svg?logoColor=white&style=for-the-badge&color=red)

## Table of Contents

* [Documentation](#documentation)
* [Installation](#installation)
* [Getting Started](#getting-started)
* [Contributing](#contributing)
* [Reach out](#reach-out)
* [License](#license)

## Documentation

The documentation for this project is created using [Mkdocs](https://www.mkdocs.org/)
and deployed on [GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/about-github-pages).

You can find the documentation here: https://aditya-gupta1.github.io/track-job-applications/

>Markdown files that generates documentation are in `docs` folder. The website elements are generated from `docs` folder and moved to `gh-deploy` branch. It is from here that the GitHub pages picks up the files for deployment.

## Installation

**Prerequisites:** [Python](https://www.python.org/downloads/)

Run the following command to install the application:
```cmd
pip install track-job-applications
```

## Getting Started

```commandline
// add a job application
> track-job add CompanyX SDE-1

// display all the applications
> track-job ls

// update the application details
> track-job update company <application-id> <new company name>

// know more about any command
> track-job <command> --help

// know about all the commands available
> track-job --help

// get a report on all the applications
> track-job report

// get report on all the applications made within a date range
> track-job report -s <start date in YYYY-MM-DD> -e <end date in YYYY-MM-DD>

// total applications rejected
> track-job report status rejected
```

Refer to the [commands](https://aditya-gupta1.github.io/track-job-applications/Commands/) section in the documentation for the list of commands available.

> Note: All the commands have a `--start-date` or `-s` argument to mention the start date and `--end-date` or `-e` argument
> to specify the end date, in case the command is to run for applications made within a date range.
>  Also, the data model in which applications are stored can be found in [references](https://aditya-gupta1.github.io/track-job-applications/References/) section in the docs.

## Contributing

Contributions for docs as well as code are welcomed. Head over to the [Contributing](https://github.com/Aditya-Gupta1/track-job-applications/blob/main/CONTRIBUTING.md) 
guidelines for steps to set up a development environment, contributing to code and contributing to docs.

## Reach out

Feel free to start a [discussion](https://github.com/Aditya-Gupta1/track-job-applications/discussions) on anything you want to suggest or have more clarity on.  

## License

[MIT License](https://github.com/Aditya-Gupta1/track-job-applications/blob/main/LICENSE.md)
