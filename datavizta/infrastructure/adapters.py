import httpx


class BoaviztAPIClient:
    def __init__(self) -> None:
        self._client = httpx.AsyncClient(base_url="https://api.boavizta.org/v1")

    async def get_subcategories(self, category: str) -> dict:
        response = await self._client.request("GET", f"/{category}/all")
        response.raise_for_status()
        return response.json()

    async def get_archetypes(self, category: str, subcategory: str) -> list[str]:
        response = await self._client.request(
            "GET", f"/{category}/{subcategory}/archetypes"
        )
        response.raise_for_status()
        return response.json()

    async def get_regions(self) -> list[str]:
        response = await self._client.request("GET", "/utils/country_code")
        response.raise_for_status()
        return response.json()

    async def get_terminal_impacts(
        self,
        category: str,
        subcategory: str,
        archetype: str,
        region: str,
    ) -> dict:
        url = f"/{category}/{subcategory}"
        payload = {
            "category": category,
            "subcategory": subcategory,
            "archetype": archetype,
            "usage": {
                "usage_location": region,
            },
        }
        params = {
            "archetype": archetype,
            "criteria": ["gwp", "ir", "pe", "adpe", "odp", "ap", "ept"],
        }
        response = await self._client.request("POST", url, json=payload, params=params)
        response.raise_for_status()
        return response.json()
