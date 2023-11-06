#!/bin/sh
# Source this script
if [ ! -e ./sphinx-env ]; then
   python3 -m venv sphinx-env
fi
source ./sphinx-env/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install sphinx==5.3.0 sphinx-rtd-theme sphinx_design sphinx-tabs sphinxcontrib.svg2pdfconverter sphinx-reredirects
python3 -m pip install sphinxcontrib-images
python3 -m pip install breathe exhale
