import uvicorn

from .. import settings
from .app import create_app
from ..di import bootstrap

bootstrap()

app = create_app()


def main():
    uvicorn.run("datavizta.web.main:app", reload=settings.DEBUG)


if __name__ == "__main__":
    main()
