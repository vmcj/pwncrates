"""
This file handles the "global" variables for the Jinja2 templates.

Global variables are variables used by the base template, or its includes.
"""
from webapp import app
from flask import url_for


@app.context_processor
def inject_globals():
    return dict(name="StudSec",
                routes={
                    "Home": url_for("home"),
                    "Rules": url_for("rules"),
                    "Getting started": url_for("getting_started"),
                    "Challenges": url_for("challenges"),
                    "Contributing": url_for("contributing"),
                    "Scoreboard": url_for("scoreboard")
                })
