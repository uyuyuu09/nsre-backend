import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from src.router import user

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user.user_router)


@app.get(
    "/",
    responses={
        200: {
            "description": "Root path",
            "content": {
                "application/json": {
                    "example": {"status": "ok", "hello": "world", "nsre-app": "backend"}
                }
            },
        },
    },
)
async def root():
    """
    This is the root path of the backend server.
    """
    return JSONResponse(
        content={"status": "ok", "hello": "world", "nsre-app": "backend"}
    )


if __name__ == "__main__":
    uvicorn.run(app=app)
