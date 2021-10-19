#!/bin/sh
. "/opt/anaconda3/etc/profile.d/conda.sh"
conda env create --name kat-env --file environment-dev.yml
conda activate kat-env
pip install -e .
