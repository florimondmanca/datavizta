from typing import Callable
from fluent.runtime import FluentLocalization, FluentResourceLoader

from ... import settings

TranslateFunc = Callable[[str], str]


def make_translate(roots: list[str]) -> TranslateFunc:
    loader = FluentResourceLoader(roots)

    def _make_l10n():
        return FluentLocalization(["fr"], ["main.ftl"], loader)

    _production_l10n = _make_l10n()

    def _get_l10n() -> FluentLocalization:
        if settings.DEBUG:
            # Apply new translations during development
            return _make_l10n()
        return _production_l10n

    def translate(msg_id: str, params: dict | None = None) -> str:
        l10n = _get_l10n()
        msg_id = msg_id.replace(".", "-")  # svelte-i18n compatibility
        return l10n.format_value(msg_id, params)

    return translate
