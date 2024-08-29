# BeagleBoard.org documentation build configuration file.
# 
# References: 
# https://github.com/zephyrproject-rtos/zephyr/blob/main/doc/conf.py
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
import re
import yaml
from pathlib import Path
import pydata_sphinx_theme
from sphinx.ext.imgconverter import ImagemagickConverter

# -- Project information --
project = 'BeagleBoard Docs'
copyright = '2024, BeagleBoard.org Foundation'
author = 'BeagleBoard.org Foundation'

ImagemagickConverter.conversion_rules.append(('image/webp', 'image/png'))

sys.path.append(str(Path(".").resolve()))

# Add latest images to rst_epilog
rst_epilog =""
rst_epilog_path = "_static/epilog/"
for (dirpath, dirnames, filenames) in os.walk(rst_epilog_path):
    for filename in filenames:
        with open(dirpath + filename) as f:
            rst_epilog += f.read()

# Configure PDF build and sidebar links
latex_documents = []
pdf_paths = []
oshw_details = []
board_details = []

with open('conf.yml', 'r') as conf_file:
    conf_data = yaml.safe_load(conf_file)

    pdf_build_all = True
    pdf_build = []
    if(conf_data["pdf_build"] != "all"):
        for name in conf_data["pdf_build"].split(","):
            pdf_build.append(name.lstrip())
        pdf_build_all = False

    for type, data in conf_data.items():
        # Boards
        if(type == "boards"):
            for board, data in conf_data["boards"].items():
                name = board
                path = data['path']
                pdf = data.get('pdf', False)
                page = data.get('page', False)
                git = data.get('git', False)
                forum = data.get('forum', False)
                
                # Board PDF build details
                if(pdf and (name in pdf_build or pdf_build_all)):
                    pdf_paths.append(path)
                    tex_name = '-'.join(path.split('/')[1:])
                    latex_documents.append((path+"/index", tex_name+".tex", "", author, "manual"))

                # Board OSHW mark details
                oshw_data = data.get('oshw', False)
                if oshw_data:
                    for oshw_mark_file in data['oshw'].split(','):
                        if oshw_mark_file.endswith('.svg'):
                            board, oshw_id = oshw_mark_file.lstrip().split(".")[0].split('_')
                            oshw_details.append([board, path, oshw_id])
                
                # Board basic details
                board_details.append([board, path, page, git, forum])

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
StandaloneHTMLBuilder.supported_image_types = ['image/webp', 'image/jpg', 'image/jpeg', 'image/svg+xml', 'image/png', 'image/gif']

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

# Define the json_url for our version switcher.
json_url = "_static/switcher.json"

# Define the version we use for matching in the version switcher.
version_match = os.environ.get("READTHEDOCS_VERSION")
release = pydata_sphinx_theme.__version__
# If READTHEDOCS_VERSION doesn't exist, we're not on RTD
# If it is an integer, we're in a PR build and the version isn't correct.
# If it's "latest" → change to "dev" (that's what we want the switcher to call it)
if not version_match or version_match.isdigit() or version_match == "latest":
    # For local development, infer the version to match from the package.
    if "dev" in release or "rc" in release:
        version_match = "dev"
        # We want to keep the relative reference if we are in dev mode
        # but we want the whole url if we are effectively in a released version
        json_url = "_static/switcher.json"
    else:
        version_match = f"v{release}"
elif version_match == "stable":
    version_match = f"v{release}"

# Pages entry without primary (left) sidebar

html_sidebars = {
    "**": ["sidebar-nav-bs", "mission"],
    "index": []
}

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
    "show_version_warning_banner": True,
    "navbar_center": ["version-switcher", "navbar-nav"],
    "navbar_start": ["navbar-logo"],
    "navbar_end": ["theme-switcher", "navbar-icon-links"],
    # "navbar_persistent": ["search-button"],
    "footer_start": ["copyright"],
    "footer_center": ["cc-by-sa"],
    "footer_end": ["last-updated"],
    # "content_footer_items": ["last-updated"],
    "secondary_sidebar_items": {
        "**": ["todo", "page-toc", "edit-this-page", "sourcelink","pdf", "feedback", "forum", "license-terms", "message", "oshw"]
    },
    "switcher": {
        "json_url": json_url,
        "version_match": version_match,
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
pages_slug = ""
gitlab_user = "docs"
gitlab_version = "main"
gitlab_url = "https://openbeagle.org"
gitlab_repo = "docs.beagleboard.io"
gitlab_project = "/".join((gitlab_url, gitlab_user, gitlab_repo))
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
        gitlab_project = "/".join((gitlab_url, gitlab_user, gitlab_repo))
        docs_url = "/".join((url, slug))

html_context = {
    "display_gitlab": True,
    "gitlab_url": gitlab_url,
    "gitlab_user": gitlab_user,
    "gitlab_repo": gitlab_repo,
    "gitlab_version": gitlab_version,
    "gitlab_project": gitlab_project,
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
    "pdf_paths": pdf_paths,
    "board_details": board_details
}

# -- Options for LaTeX output --
latex_engine = "xelatex"
latex_logo = "_static/images/logo-latex.pdf"
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