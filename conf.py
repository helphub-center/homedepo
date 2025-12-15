# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------

# Add paths here if your modules are outside the root
# sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------

project = 'HomeDepot Credit Card Guide'
copyright = '2025, HomeDepot MyCard Guide'
author = 'HomeDepot MyCard Help (Unofficial)'

# Release version
release = '1.0.0'

# -- General configuration ---------------------------------------------------

# Sphinx extensions
extensions = []

# Allow raw HTML in .rst files (needed for button)
raw_enabled = True

# Templates and excluded patterns
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

# Theme (optional)
# html_theme = 'sphinx_rtd_theme'

# SEO-friendly page titles
html_title = "HomeDepot.com/MyCard – Manage Your Home Depot Credit Card Online"
html_short_title = "HomeDepot MyCard Guide"

# Favicon (place in root or _static folder)
html_favicon = 'favicon.ico'

# Hide "View page source"
html_show_sourcelink = False

# Allow unsafe raw HTML (required for CTA button)
html_allow_unsafe = True

# Theme customization
html_theme_options = {
    'show_powered_by': False,
}

# Static files (optional)
# html_static_path = ['_static']
