from ..di import resolve
from ..domain.entities import Category, Subcategory, Archetype, Region
from ..domain.repositories import (
    CategoryRepository,
    SubcategoryRepository,
    ArchetypeRepository,
    RegionRepository,
)
from .views import ImpactsView
from .services import ImpactCalculator


async def get_categories() -> list[Category]:
    repo: CategoryRepository = resolve("category_repository")
    return await repo.find_all()


async def get_subcategories(category: str) -> list[Subcategory]:
    repo: SubcategoryRepository = resolve("subcategory_repository")
    return await repo.find_all_by_category(category)


async def get_archetypes(category: str, subcategory: str) -> list[Archetype]:
    repo: ArchetypeRepository = resolve("archetype_repository")
    return await repo.find_all(category, subcategory)


async def get_regions() -> list[Region]:
    repo: RegionRepository = resolve("region_repository")
    return await repo.find_all()


async def get_terminal_impacts(
    category: str,
    subcategory: str,
    archetype: str,
    region: str,
) -> ImpactsView:
    calculator: ImpactCalculator = resolve("impact_calculator")
    return await calculator.get_terminal_impacts(
        category, subcategory, archetype, region
    )
