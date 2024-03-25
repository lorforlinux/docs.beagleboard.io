# BeagleBoard.org documentation build configuration file.
# 
# References: 
# https://github.com/zephyrproject-rtos/zephyr/blob/main/doc/conf.py
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
import re
from pathlib import Path
import pydata_sphinx_theme
from sphinx.ext.imgconverter import ImagemagickConverter

ImagemagickConverter.conversion_rules.append(('image/webp', 'image/png'))

sys.path.append(str(Path(".").resolve()))

rst_epilog =""

# Add latest images to rst_epilog
rst_epilog_path = "_static/epilog/"
for (dirpath, dirnames, filenames) in os.walk(rst_epilog_path):
    for filename in filenames:
        with open(dirpath + filename) as f:
            rst_epilog += f.read() 

# Board OSHWA certification information
oshw_logos_path = "_static/images/oshw/"
oshw_details = []
for (dirpath, dirnames, filenames) in os.walk(oshw_logos_path):
    for filename in filenames:
        filename.replace("#","/")
        if filename.endswith('.svg'):
            oshw_logo_name = filename.split(".")[0]
            oshw_details.append(oshw_logo_name.split('_'))

# Unique boards path information
boards_path = []
for board, path, oshw_id in oshw_details:
    for (dirpath, dirnames, filenames) in os.walk("boards"):
        if '/'+path+'/' in dirpath+'/':
            if path+'/' not in dirpath:
                boards_path.append(dirpath)
boards_path = set(boards_path)

# -- Project information --
project = 'BeagleBoard Docs'
copyright = '2024, BeagleBoard.org Foundation'
author = 'BeagleBoard.org Foundation'

# -- General configuration --

sys.path.append(os.path.abspath("./_ext"))

extensions = [
    "callouts",
    "sphinxcontrib.rsvgconverter",
    "sphinx_design",
    "sphinxcontrib.images",
    "sphinx.ext.imgconverter",
    "sphinx.ext.graphviz",
    "sphinx.ext.todo",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx_tabs.tabs",
    "breathe",
    "sphinx_copybutton",
    "sphinxcontrib.youtube",
]

#graphviz_output_format = 'svg'

breathe_projects = {"librobotcontrol": "projects/librobotcontrol/docs/xml"}
breathe_default_project = "librobotcontrol"

exhale_args = {
    "containmentFolder": "./projects/librobotcontrol",
    "rootFileName": "index.rst",
    "rootFileTitle": "Robot Control Library",
    "createTreeView": True,
    "exhaleExecutesDoxygen": False,
    "doxygenStripFromPath": ".",
    "verboseBuild": False,
}

primary_domain = 'cpp'
highlight_language = 'cpp'

todo_include_todos = True

# Update (HTML) supported_image_types selection priority order
from sphinx.builders.html import StandaloneHTMLBuilder
StandaloneHTMLBuilder.supported_image_types = ['image/webp', 'image/jpg', 
                                       'image/jpeg', 'image/svg+xml', 'image/png', 'image/gif']

# Update (PDF) supported_image_types selection priority order
from sphinx.builders.latex import LaTeXBuilder
LaTeXBuilder.supported_image_types = ['application/pdf', 'image/jpg', 'image/jpeg', 'image/png']

templates_path = ['_templates']

source_suffix = ['.rst']
numfig = True

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'env', ".venv"]

html_theme = 'pydata_sphinx_theme'
html_static_path = ["_static"]
html_logo = "_static/images/logo.svg"
html_favicon = "_static/images/boris.svg"
html_sourcelink_suffix = ""
html_last_updated_fmt = ""
html_theme_path = [pydata_sphinx_theme.Path()]
html_title = "BeagleBoard Documentation"
html_baseurl = "docs.beagleboard.io"
html_css_files = [
    'css/custom.css',
]

# html_sidebars = {

# }

html_theme_options = {
    "external_links": [
        {
            "url": "https://www.beagleboard.org/about",
            "name": "About",
        },
        {
            "url": "https://www.beagleboard.org/donate",
            "name": "Donate",
        },
        {
            "url": "https://gsoc.beagleboard.org/",
            "name": "GSoC",
        },
        {
            "url": "https://forum.beagleboard.org/c/faq",
            "name": "FAQ",
        },
    ],
    # "header_links_before_dropdown": 4,
    "show_prev_next": True,
    "icon_links": [
        {
            "name": "OpenBeagle",
            "url": "https://openbeagle.org/",
            "icon": "fa-brands fa-gitlab",
            "attributes": {"target": "_blank"},
        },
        {
            "name": "Docs",
            "url": "https://docs.beagleboard.org/",
            "icon": "fa-solid fa-book",
            "attributes": {"target": "_blank"},
        },
        {
            "name": "Discord",
            "url": "https://bbb.io/discord",
            "icon": "fa-brands fa-discord",
            "attributes": {"target": "_blank"},
        },
        {
            "name": "Forum",
            "url": "https://forum.beagleboard.org/",
            "icon": "fa-brands fa-discourse",
            "attributes": {"target": "_blank"},
        },
        {
            "name": "BeagleBoard.org",
            "url": "https://www.beagleboard.org",
            "icon": "_static/images/boris.svg",
            "type": "local",
            "attributes": {"target": "_blank"},
        }
    ],
    "use_edit_page_button": True,
    "show_toc_level": 1,
    "navbar_align": "right",
    "show_nav_level": 1,
    "announcement": "Welcome to new site for BeagleBoard.org docs!",
    # "show_version_warning_banner": True,
    "navbar_center": ["navbar-nav"],
    "navbar_start": ["navbar-logo"],
    "navbar_end": ["theme-switcher", "navbar-icon-links"],
    # "navbar_persistent": ["search-button"],
    "footer_start": ["copyright"],
    "footer_center": ["cc-by-sa"],
    "footer_end": ["last-updated"],
    # "content_footer_items": ["last-updated"],
    "secondary_sidebar_items": {
        "**": ["page-toc", "edit-this-page", "sourcelink","pdf","oshw"]
    },
}

# parse version from 'VERSION' file
with open("VERSION") as f:
    m = re.match(
        (
            r"^VERSION_MAJOR\s*=\s*(\d+)$\n"
            + r"^VERSION_MINOR\s*=\s*(\d+)$\n"
            + r"^PATCHLEVEL\s*=\s*(\d+)$\n"
            + r"^VERSION_TWEAK\s*=\s*\d+$\n"
            + r"^EXTRAVERSION\s*=\s*(.*)$"
        ),
        f.read(),
        re.MULTILINE,
    )

    if not m:
        sys.stderr.write("Warning: Could not extract docs version\n")
        version = "Unknown"
    else:
        major, minor, patch, extra = m.groups(1)
        version = ".".join((major, minor, patch))
        release_version = ".".join((major, minor))
        if extra:
            version += "-" + extra

release = version

# Variables here holds default settings
pages_url = "https://docs.beagleboard.io"
pages_slug = "latest"
gitlab_user = "docs"
gitlab_version = "main"
gitlab_url = "https://openbeagle.org"
gitlab_repo = "docs.beagleboard.io"
docs_url = "https://docs.beagleboard.io"

# parse pages details from 'PAGES' file
with open("PAGES") as f:
    m = re.match(
        (
            r"^PAGES_URL\s*=\s*(\S+)$\n"
            + r"^PAGES_SLUG\s*=\s*(\S+)$\n"
            + r"^GITLAB_USER\s*=\s*(\S+)$\n"
            + r"^PROJECT_BRANCH\s*=\s*(\S+)$\n"
            + r"^GITLAB_HOST\s*=\s*(\S+)$\n"
            + r"^PROJECT_REPO\s*=\s*(\S+)$\n"
        ),
        f.read(),
        re.MULTILINE,
    )

    if not m:
        sys.stderr.write("Warning: Could not extract pages information\n")
    else:
        url, slug, user, branch, host, repo = m.groups(1)
        slug = "latest" if slug == "main" else slug
        pages_url = url
        pages_slug = slug
        gitlab_user = user
        gitlab_version = branch
        gitlab_url = host
        gitlab_repo = repo
        docs_url = "/".join((url, slug))

html_context = {
    "display_gitlab": True,
    "gitlab_url": gitlab_url,
    "gitlab_user": gitlab_user,
    "gitlab_repo": gitlab_repo,
    "gitlab_version": gitlab_version,
    "doc_path": "",
    #"use_edit_page_button": True,
    #"edit_page_url_template": "https://openbeagle.org/XXXX/{{ file_name }}",
    "conf_py_path": "",
    "show_license": True,
    "pages_url": pages_url,
    "pages_slug": pages_slug,
    "docs_url": docs_url,
    "edit_page_url_template": "{{ my_vcs_site }}{{ file_name }}",
    "edit_page_provider_name": "OpenBeagle",
    "my_vcs_site": "https://openbeagle.org/docs/docs.beagleboard.io/-/edit/main/",
    "oshw_details": oshw_details,
    "boards_path": boards_path
}

# -- Options for LaTeX output --
latex_engine = "xelatex"
latex_logo = "_static/images/logo-latex.pdf"
latex_documents = []
latex_elements = {
    "papersize": "a4paper",
    "maketitle": open("_static/latex/title.tex").read(),
    "preamble": open("_static/latex/preamble.tex").read(),
    "sphinxsetup": ",".join(
        (
            "verbatimwithframe=false",
            "VerbatimColor={HTML}{f0f2f4}",
            "InnerLinkColor={HTML}{2980b9}",
            "warningBgColor={HTML}{e9a499}",
            "warningborder=0pt",
            r"HeaderFamily=\rmfamily\bfseries",
        )
    ),
}

for board_path in boards_path:
    board_tex_name = board_path.split('/')[-1]
    latex_documents.append((board_path+"/index", board_tex_name+".tex", "", author, "manual"))