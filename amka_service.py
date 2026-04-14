import httpx
from token_service import get_ked_token
from settings import settings

async def lookup_amka(amka: str):
    token = await get_ked_token()

    async with httpx.AsyncClient(timeout=10) as client:
        resp = await client.post(
            settings.KED_AMKA_URL,
            json={"amka": amka},
            headers={
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json",
            },
        )

    if resp.status_code == 400:
        return {"error": "INVALID_AMKA"}

    if resp.status_code == 401:
        return {"error": "UNAUTHORIZED"}

    if resp.status_code == 429:
        return {"error": "RATE_LIMIT"}

    resp.raise_for_status()
    return resp.json()
