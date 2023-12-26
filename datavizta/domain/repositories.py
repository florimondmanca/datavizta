from typing import Protocol

from .entities import Category, Subcategory, Archetype, Region


class CategoryRepository(Protocol):
    async def find_all(self) -> list[Category]:
        ...


class SubcategoryRepository(Protocol):
    async def find_all_by_category(self, category: str) -> list[Subcategory]:
        ...


class ArchetypeRepository(Protocol):
    async def find_all(self, category: str, subcategory: str) -> list[Archetype]:
        ...


class RegionRepository(Protocol):
    async def find_all(self) -> list[Region]:
        ...
