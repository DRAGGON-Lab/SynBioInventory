from fastapi import APIRouter, HTTPException

from app.main import get_synbiohub_client
from app.schemas import AuthStatus, LoginRequest

router = APIRouter(prefix="/api/auth", tags=["auth"])


@router.post("/login", response_model=AuthStatus)
def login(payload: LoginRequest) -> AuthStatus:
    client = get_synbiohub_client()
    authenticated = client.login(payload.username, payload.password)
    if not authenticated:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return AuthStatus(authenticated=True, username=payload.username)


@router.post("/logout", response_model=AuthStatus)
def logout() -> AuthStatus:
    client = get_synbiohub_client()
    client.logout()
    return AuthStatus(authenticated=False)


@router.get("/me", response_model=AuthStatus)
def me() -> AuthStatus:
    client = get_synbiohub_client()
    return AuthStatus(authenticated=client.is_authenticated(), username=client.current_user())
