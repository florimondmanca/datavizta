import pathlib
from starlette.config import Config

config = Config(".env")

HERE = pathlib.Path(__file__).parent

DEBUG = config.get("DATAVIZTA_DEBUG", cast=bool, default=False)

STATIC_DIR = HERE / "web" / "static"
STATIC_ROOT = "/static"

TEMPLATES_DIR = HERE / "web" / "templates"

FLUENT_ROOT = HERE / "l10n" / "{locale}"
