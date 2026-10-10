# Snakefile — orchestrates the replication pipeline end-to-end.
# Each rule executes a jupytext notebook (the notebook is the source of truth).
#
# Usage:
#   pixi run snakemake --cores 1        # run everything
#   pixi run snakemake --cores 1 -n     # dry run

NOTEBOOKS = "notebooks"
DATA = "data"
RESULTS = "results"
FIGURES = "figures"


def run_nb(name):
    return f"cd {NOTEBOOKS} && jupytext --to notebook --execute {name}"


rule all:
    input:
        f"{FIGURES}/main_result.png",
        f"{RESULTS}/summary.csv",


rule data_download:
    input:
        f"{NOTEBOOKS}/01_data_download.py",
    output:
        f"{DATA}/raw/pgph.0001995.s001.xlsx",
        f"{DATA}/raw/sources.json",
    shell:
        run_nb("01_data_download.py")


rule data_clean:
    input:
        f"{NOTEBOOKS}/02_data_clean.py",
        f"{DATA}/raw/pgph.0001995.s001.xlsx",
    output:
        f"{DATA}/processed/noma_clean.csv",
    shell:
        run_nb("02_data_clean.py")


rule analysis:
    input:
        f"{NOTEBOOKS}/03_analysis.py",
        f"{DATA}/processed/noma_clean.csv",
    output:
        f"{RESULTS}/summary.csv",
    shell:
        run_nb("03_analysis.py")


rule figures:
    input:
        f"{NOTEBOOKS}/04_figures.py",
        f"{RESULTS}/summary.csv",
        f"{DATA}/processed/noma_clean.csv",
    output:
        f"{FIGURES}/main_result.png",
    shell:
        run_nb("04_figures.py")
