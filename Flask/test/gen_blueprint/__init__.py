# pylint: disable=all
"""Flask"""
from flask import Blueprint
gen_blue = Blueprint("leviathan", __name__, url_prefix="/leviathan")
from . import gen  # noqa: F401,E402
__all__ = ["gen"]  # pylint: disable=E0603
