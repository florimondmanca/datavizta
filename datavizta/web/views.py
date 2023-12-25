from starlette.requests import Request
from starlette.responses import Response

from .templating import templates


async def index(request: Request) -> Response:
    context = {"request": request}
    return templates.TemplateResponse(request, "index.jinja", context)
