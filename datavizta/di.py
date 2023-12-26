import punq
from starlette.templating import Jinja2Templates
from .infrastructure.l10n.fluent import make_translate

from . import settings

_CONTAINER: punq.Container


def bootstrap() -> punq.Container:
    global _CONTAINER

    from .infrastructure.adapters import BoaviztAPIClient
    from .infrastructure.repositories import (
        HardcodedCategoryRepository,
        BoaviztAPISubcategoryRepository,
        BoaviztAPIArchetypeRepository,
        BoaviztAPIRegionRepository,
    )
    from .infrastructure.services import (
        BoaviztAPIImpactCalculator,
    )

    container = punq.Container()

    trans = make_translate(str(settings.FLUENT_ROOT))
    container.register("trans", instance=trans)

    templates = Jinja2Templates(directory=settings.TEMPLATES_DIR)
    templates.env.globals["_"] = trans
    container.register("templates", instance=templates)

    boaviztapi_client = BoaviztAPIClient()

    container.register("category_repository", instance=HardcodedCategoryRepository())
    container.register(
        "subcategory_repository",
        instance=BoaviztAPISubcategoryRepository(client=boaviztapi_client),
    )
    container.register(
        "archetype_repository",
        instance=BoaviztAPIArchetypeRepository(client=boaviztapi_client),
    )
    container.register(
        "region_repository",
        instance=BoaviztAPIRegionRepository(client=boaviztapi_client),
    )

    container.register(
        "impact_calculator",
        instance=BoaviztAPIImpactCalculator(client=boaviztapi_client),
    )

    _CONTAINER = container


def resolve(key: str):
    return _CONTAINER.resolve(key)
