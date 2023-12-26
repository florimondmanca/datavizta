from ..application.services import ImpactCalculator
from ..application.views import ImpactsView, Impact, ImpactValue

from .adapters import BoaviztAPIClient


class BoaviztAPIImpactCalculator(ImpactCalculator):
    def __init__(self, client: BoaviztAPIClient) -> None:
        self._client = client

    async def get_terminal_impacts(
        self,
        category: str,
        subcategory: str,
        archetype: str,
        region: str,
    ) -> ImpactsView:
        data = await self._client.get_terminal_impacts(
            category, subcategory, archetype, region
        )

        impacts: ImpactsView = []

        for name, value in data["impacts"].items():
            unit = value["unit"]

            decimals = {
                "kgCO2e": 1,
                "MJ": 0,
            }.get(unit, 6)

            impacts.append(
                Impact(
                    name=name,
                    description=value["description"],
                    use=(
                        ImpactValue(**value["use"])
                        if value["use"] != "not implemented"
                        else None
                    ),
                    embedded=(
                        ImpactValue(**value["embedded"])
                        if value["embedded"] != "not implemented"
                        else None
                    ),
                    decimals=decimals,
                    unit=unit,
                )
            )

        return impacts
