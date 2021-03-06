# Contributing to Qurro's codebase

If you'd like to make changes to Qurro's codebase, then first off --
thanks a ton! This document describes (briefly) how you'd go about doing this.

**Note that these are very in-progress instructions.** If you have any
questions on things that were missed/unclear here, feel free to file an issue
in this repository or email the Qurro development team
([mfedarko@ucsd.edu](mailto:mfedarko@ucsd.edu)).

## Setting up a development environment

1. Fork Qurro.
1. Clone your fork of Qurro's source code to your computer.
2. Create a development conda environment for Qurro:
    1. Install the latest version of QIIME 2 natively,
       [as you would normally](https://docs.qiime2.org/2019.7/install/native/).
       _You'll need to install a QIIME 2 version of at least 2019.7._
    2. In a terminal, navigate to the folder to which you cloned your fork of
       Qurro's source code above. Run `pip install -e .[dev]` inside this folder to
       install Qurro along with its normal and development Python dependencies.
    4. Install the various Node.js requirements for testing Qurro's JavaScript
       code. This can be done by running
       `npm install -g mocha-headless-chrome jshint prettier nyc`. Note that
       this will install these programs globally on your system.
3. Run the following commands to verify everything was installed correctly:
```bash
qiime dev refresh-cache
make test
make stylecheck
```
If these commands succeed, then you can start making changes to Qurro.

## Before submitting a pull request to Qurro

Both of the following criteria should be followed:

1. All the tests pass (i.e. `make test` succeeds).
2. The code is properly formatted (i.e. `make stylecheck` succeeds).

Assuming all of Qurro's development dependencies are installed, you can run
`make style` to perform auto-formatting. (In rare occasions I've observed black
and flake8 disagreeing, in which case you'd need to manually resolve the
problem to get `make stylecheck` to pass. But I don't think this should happen
very often or at all by this point -- contact me if you have questions.)

## Common problems

### I get a `FileNotFoundError` that says `No such file or directory: 'docs/demos/matching_test/main.js`

This is due to how Qurro's test suite is set up. The "matching test" output is
generated by Qurro's Python tests, and is used to populate some of the
JavaScript tests. Long story short, you'll just need to run `make test` (or
just `make pytest`) before running `make jstest`.

## Acknowledgements

This document was loosely based on Emperor's [CONTRIBUTING.md file](https://github.com/biocore/emperor/blob/new-api/CONTRIBUTING.md).
