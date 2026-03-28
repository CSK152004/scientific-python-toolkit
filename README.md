# scientific-python-toolkit (satool)

A small scientific Python toolkit that demonstrates a complete mini workflow often used in computational science and physics-oriented programming.

This project generates synthetic decay-like data, fits an exponential decay model using SciPy, saves the fitted data to CSV, and creates a plot with Matplotlib. It is designed as a compact proof-of-skill repository that shows practical experience with the scientific Python ecosystem, command-line interfaces, project structure, packaging, and basic testing.

The goal of this repository is not to be a large research package, but to present a clean and understandable example of how a basic scientific Python script can be turned into a more professional and reusable project.

## Features

- Generate synthetic physics-like decay data
- Fit an exponential decay model with SciPy
- Save results to a CSV file
- Create a plot of data and fitted curve
- Provide a simple command-line interface
- Use a structured Python package layout
- Include basic tests for demonstration

## Example Plot

![Decay fit](docs/decay_fit.png)

## Why this project?

This repository can be used as a small portfolio project to demonstrate:

- Python programming
- Scientific computing with NumPy and SciPy
- Data visualization with Matplotlib
- Command-line tool design
- Packaging with `pyproject.toml`
- Basic software engineering practices such as tests and clear project structure

It is especially useful as a beginner-friendly project for GitHub when you want to show that you can go beyond a single script and organize code in a more professional way.

## Installation

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
