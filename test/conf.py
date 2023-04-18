# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'test'
copyright = '2023, Jason'
author = 'Jason'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.imgconverter']


templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

# -- Options for PDF output -------------------------------------------------

from sphinx.builders.latex import LaTeXBuilder

# add .webp to the LaTeX builder's image file extensions
LaTeXBuilder.supported_image_types += ['.webp']

class WebPConverter:
    def apply(self, **kwargs):
        from PIL import Image
        for infile in kwargs['images']:
            if infile.endswith('.webp'):
                outfile = infile.replace('.webp', '.png')
                try:
                    im = Image.open(infile)
                    im.save(outfile)
                except OSError:
                    print(f'Cannot convert {infile}')

# add WebPConverter to the imgconverter extension's converters list
imgconverter_image_converters = {
    '.webp': WebPConverter,
}

#latex_engine = 'xelatex'
imgconverter_image_format = 'png'

latex_elements = {
  'extraclassoptions': 'openany,oneside'
}
