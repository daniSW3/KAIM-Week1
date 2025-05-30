Modularized Stock News and Technical Analysis Project
This repository contains modularized Python code for analyzing stock news data and performing technical analysis.
Setup

Clone the repository: git clone <https://github.com/daniSW3/KAIM-Week1>
Create a virtual environment: python -m venv venv_wk1
Activate the virtual environment:
Windows: venv_wk1\Scripts\activate
Unix/Linux/Mac: source venv/bin/activate


Install dependencies: pip install -r requirements.txt

Folder Structure

src/: Modularized source code.
data/: Data loading modules.
analysis/: Analysis modules (EDA and technical).
visualization/: Plotting utilities.


notebooks/: Jupyter notebooks for EDA.
tests/: Unit tests.
scripts/: Utility scripts.
.github/workflows/: CI/CD pipeline configurations.

Running the Analysis

Scripted: python src/main.py
Interactive EDA: Open notebooks/eda_notebook.ipynb in Jupyter (jupyter notebook).

