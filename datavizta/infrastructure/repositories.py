from ..domain.entities import Category, Subcategory, Archetype, Region
from ..domain.repositories import (
    CategoryRepository,
    SubcategoryRepository,
    ArchetypeRepository,
    RegionRepository,
)
from ..di import resolve
from ..infrastructure.l10n.fluent import TranslateFunc
from .adapters import BoaviztAPIClient


class HardcodedCategoryRepository(CategoryRepository):
    async def find_all(self) -> list[Category]:
        trans: TranslateFunc = resolve("trans")

        return [
            Category(value="terminal", label=trans("terminal-config-terminals")),
            Category(value="peripheral", label=trans("terminal-config-peripherals")),
        ]


class BoaviztAPISubcategoryRepository(SubcategoryRepository):
    def __init__(self, client: BoaviztAPIClient) -> None:
        self._client = client

    async def find_all_by_category(self, category: str) -> list[Subcategory]:
        items = await self._client.get_subcategories(category)
        return [Subcategory(label=k, value=k) for k, _ in items.items()]


class BoaviztAPIArchetypeRepository(ArchetypeRepository):
    def __init__(self, client: BoaviztAPIClient) -> None:
        self._client = client

    async def find_all(self, category: str, subcategory: str) -> list[Archetype]:
        items = await self._client.get_archetypes(category, subcategory)
        return [Archetype(label=item, value=item) for item in items]


class BoaviztAPIRegionRepository(RegionRepository):
    def __init__(self, client: BoaviztAPIClient) -> None:
        self._client = client

    async def find_all(self) -> list[Region]:
        items = await self._client.get_regions()
        return [Region(label=item, value=item) for item in items]
