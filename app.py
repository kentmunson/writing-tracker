"""
Offers Google Doc Analysis
"""
import os

import yaml
from fastapi import FastAPI

from routers.docs import docs_router

app = FastAPI()

app.include_router(docs_router, prefix="/docs")


@app.get("/")
def health_check():
    """Acknowledge that the service is running."""
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
