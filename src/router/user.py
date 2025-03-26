from fastapi import Depends, HTTPException, status, APIRouter
from fastapi.responses import JSONResponse
from ..schema.user import NewUser

# import database

user_router = APIRouter(
    prefix="/user",
    tags=["user"],
    # dependencies=[Depends(database.dbsession)],
)


@user_router.get(
    "/",
    responses={
        200: {
            "description": "User-Root path",
            "content": {"application/json": {"example": {"message": "Hi user!"}}},
        }
    },
)
async def root():
    """
    This is the root path of the user server. If you recieve "Hi user!" as a response, the user server is working.
    """
    return JSONResponse(content={"message": "Hi user!"})


@user_router.post(
    "/new",
    responses={
        200: {
            "description": "Create a new user",
            "content": {
                "application/json": {
                    "example": {
                        "new_user_id": 0,
                        "new_user_name": "new_user_name",
                        "new_user_email": "new_user_email",
                    }
                }
            },
        },
    },
)
async def create_user(user: NewUser):
    """
    Create a new user.
    """
    return JSONResponse(
        content={
            "new_user_id": user.new_user_id,
            "new_user_name": user.new_user_name,
            "new-user_email": user.new_user_email,
        }
    )
