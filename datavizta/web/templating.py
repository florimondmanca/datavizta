from starlette.templating import Jinja2Templates
from ..infrastructure.l10n.fluent import make_translate

from .. import settings

templates = Jinja2Templates(directory=settings.TEMPLATES_DIR)


templates.env.globals["_"] = make_translate(str(settings.FLUENT_ROOT))
