from starlette.applications import Starlette
from starlette.types import ASGIApp

from .routes import make_routes


def create_app() -> ASGIApp:
    return Starlette(
        routes=make_routes(),
    )
