from dataclasses import dataclass


@dataclass(frozen=True)
class Category:
    value: str
    label: str


@dataclass(frozen=True)
class Subcategory:
    value: str
    label: str


@dataclass(frozen=True)
class Archetype:
    value: str
    label: str


@dataclass(frozen=True)
class Region:
    value: str
    label: str
