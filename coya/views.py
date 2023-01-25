from jinja2 import TemplateNotFound
from flask import render_template, abort, current_app


@current_app.route("/<presentation_name/>", methos=["GET"])
def landing(presentation_name):
    try:
        return render_template(f"""{presentation_name}.html""")
    except TemplateNotFound:
        abort(404)
