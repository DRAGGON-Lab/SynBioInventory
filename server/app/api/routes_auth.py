from fastapi import APIRouter, HTTPException, Request

from app.schemas.auth import AuthResponse, LoginRequest

router = APIRouter(prefix="/api/auth", tags=["auth"])


@router.post("/login", response_model=AuthResponse)
def login(payload: LoginRequest, request: Request) -> AuthResponse:
    client = request.app.state.synbiohub_client
    try:
        identity = client.login(payload.username, payload.password)
    except ValueError as exc:
        raise HTTPException(status_code=401, detail=str(exc)) from exc

    request.app.state.session = {"username": identity.username, "token": identity.token}
    return AuthResponse(authenticated=True, username=identity.username)


@router.post("/logout", response_model=AuthResponse)
def logout(request: Request) -> AuthResponse:
    session = request.app.state.session
    if session:
        request.app.state.synbiohub_client.logout(session["token"])
    request.app.state.session = None
    return AuthResponse(authenticated=False, username=None)


@router.get("/me", response_model=AuthResponse)
def me(request: Request) -> AuthResponse:
    session = request.app.state.session
    if not session:
        return AuthResponse(authenticated=False, username=None)
    return AuthResponse(authenticated=True, username=session["username"])
