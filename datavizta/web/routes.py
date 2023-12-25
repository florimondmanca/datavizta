from starlette.routing import Route, Mount
from starlette.staticfiles import StaticFiles

from .. import settings
from . import views


def make_routes():
    static = StaticFiles(directory=settings.STATIC_DIR)

    return [
        Mount(settings.STATIC_ROOT, static, name="static"),
        Route("/", views.index, name="index"),
    ]
