from starlette.requests import Request
from starlette.responses import Response
from starlette.templating import Jinja2Templates

from ..di import resolve
from ..application.queries import (
    get_categories,
    get_subcategories,
    get_archetypes,
    get_regions,
    get_terminal_impacts,
)


async def index(request: Request) -> Response:
    templates: Jinja2Templates = resolve("templates")

    context = {
        "request": request,
    }

    return templates.TemplateResponse(request, "index.jinja", context)


async def terminal_impact(request: Request) -> Response:
    templates: Jinja2Templates = resolve("templates")

    categories = await get_categories()
    category = request.query_params.get("category", categories[0].value)

    subcategories = await get_subcategories(category)
    subcategory = request.query_params.get("subcategory", subcategories[0].value)

    archetypes = await get_archetypes(category, subcategory)
    archetype = request.query_params.get("archetype", archetypes[0].value)

    regions = await get_regions()
    region = request.query_params.get("region", regions[0].value)

    impacts = await get_terminal_impacts(category, subcategory, archetype, region)

    context = {
        "request": request,
        "category": category,
        "subcategory": subcategory,
        "archetype": archetype,
        "region": region,
        "categories": categories,
        "subcategories": subcategories,
        "archetypes": archetypes,
        "regions": regions,
        "impacts": impacts,
    }

    return templates.TemplateResponse(request, "terminal_impact.jinja", context)
