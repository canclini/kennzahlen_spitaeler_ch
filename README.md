# Analyse der Kennzahlen der Schweizer Spitäler

exploartive Analyse der vom BAG veröffentlichten Kennzahlen zu den Schweizer Spitäler.
Die Kennzahlen sind auf [opendata.swiss verfügbar](https://opendata.swiss/de/organization/bundesamt-fur-gesundheit-bag?keywords_de=kennzahlen).

## Setup
1. clone the repository
2. install the environment `make create_environment`. 
3. Activate the environment. If using conda: `source activate kennzahlen_schweizer_spitaeler`
4. install the required packages `make requirements`

## Getting the data
the data is downloaded from [opendata.swiss]([https://opendata.swiss) to the data/raw directory. Just type `make download_data`.

## Projektstruktur

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── src                <- Source code for use in this project.
        ├── __init__.py    <- Makes src a Python module
        │
        ├── data           <- Scripts to download or generate data
        │   └── make_dataset.py
        │
        └── visualization  <- Scripts to create exploratory and results oriented visualizations
            └── visualize.py


<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
