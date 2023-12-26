from dataclasses import dataclass, field


@dataclass(frozen=True)
class ImpactValue:
    value: float
    min: float
    max: float
    warnings: list[str] = field(default_factory=list)


@dataclass(frozen=True)
class Impact:
    name: str
    description: str
    use: ImpactValue | None
    embedded: ImpactValue | None
    unit: str
    decimals: int

    @property
    def total(self) -> float:
        total = self.use.value

        if self.embedded is not None:
            total += self.embedded.value

        return round(total, self.decimals)

    @property
    def use_value(self) -> float | None:
        return round(self.use.value, self.decimals) if self.use is not None else None

    @property
    def embedded_value(self) -> float | None:
        return (
            round(self.embedded.value, self.decimals)
            if self.embedded is not None
            else None
        )


ImpactsView = dict[str, Impact]
