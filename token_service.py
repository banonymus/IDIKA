import httpx
from datetime import datetime, timedelta
from settings import settings

_cached_token = None
_token_expiry = None

async def get_ked_token():
    global _cached_token, _token_expiry

    if _cached_token and _token_expiry > datetime.utcnow():
        return _cached_token

    async with httpx.AsyncClient(timeout=10) as client:
        resp = await client.post(
            settings.KED_TOKEN_URL,
            data={
                "grant_type": "client_credentials",
                "client_id": settings.KED_CLIENT_ID,
                "client_secret": settings.KED_CLIENT_SECRET,
            },
            headers={"Content-Type": "application/x-www-form-urlencoded"},
        )

    resp.raise_for_status()
    data = resp.json()

    _cached_token = data["access_token"]
    _token_expiry = datetime.utcnow() + timedelta(seconds=data["expires_in"] - 30)

    return _cached_token
