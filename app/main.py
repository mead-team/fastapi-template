from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.metadata import swagger_metadata
from app.core.middleware import ProcessTimeMiddleware
from app.core.setting import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    print(f"INFO:     Hello, Run the server in the {settings.APP_ENV} environment 👋")
    yield
    print(
        f"INFO:     Bye, Shut down the server in the {settings.APP_ENV} environment 👋"
    )


app = FastAPI(**swagger_metadata, lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(ProcessTimeMiddleware)


@app.get("/api-health-check")
def api_health_check():
    return {
        "api_health_check": "api-server-template is Ok",
        "debug-mode": settings.DEBUG,
    }
