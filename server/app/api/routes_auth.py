from fastapi import APIRouter, HTTPException, Request, Response

from app.schemas import AuthResponse, LoginRequest
from app.services.synbiohub_client import synbiohub_client

router = APIRouter(prefix="/api/auth", tags=["auth"])
SESSION_COOKIE = "synbioinventory_session"


@router.post("/login", response_model=AuthResponse)
def login(payload: LoginRequest, response: Response) -> AuthResponse:
    try:
        session = synbiohub_client.login(payload.username, payload.password)
    except ValueError as exc:
        raise HTTPException(status_code=401, detail=str(exc)) from exc

    response.set_cookie(SESSION_COOKIE, session.session_id, httponly=True, samesite="lax")
    return AuthResponse(authenticated=True, username=session.username)


@router.post("/logout")
def logout(request: Request, response: Response) -> dict:
    session_id = request.cookies.get(SESSION_COOKIE)
    if session_id:
        synbiohub_client.logout(session_id)
    response.delete_cookie(SESSION_COOKIE)
    return {"authenticated": False}


@router.get("/me", response_model=AuthResponse)
def me(request: Request) -> AuthResponse:
    session = synbiohub_client.get_session(request.cookies.get(SESSION_COOKIE))
    if not session:
        return AuthResponse(authenticated=False)
    return AuthResponse(authenticated=True, username=session.username)
