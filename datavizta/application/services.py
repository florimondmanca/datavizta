from typing import Protocol

from .views import ImpactsView


class ImpactCalculator(Protocol):
    async def get_terminal_impacts(
        self,
        category: str,
        subcategory: str,
        archetype: str,
        region: str,
    ) -> ImpactsView:
        ...
