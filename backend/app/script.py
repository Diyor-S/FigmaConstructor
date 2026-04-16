import uvicorn

from core.config import settings


def main():
    uvicorn.run(
        app=settings.run.app,
        host=settings.run.host,
        port=settings.run.port,
        reload=True,
    )


if __name__ == "__main__":
    main()
