# coding: utf-8
from __future__ import absolute_import

from flask import Blueprint, render_template

from .correios import correios_client
from .utils import get_objetos

bp = Blueprint('websro', __name__)


@bp.route("/")
def index():
    objetos, _redirect = get_objetos()
    if _redirect:
        return _redirect

    response = correios_client.buscaEventos(objetos)
    return render_template('websro.html', objeto=response["objeto"][0])


def init_app(app, url_prefix=None):
    app.register_blueprint(bp, url_prefix=url_prefix)
