import httpx

BASE_URL = "https://fearless-enchantment-production-0db7.up.railway.app/"

async def get_books():
    async with httpx.AsyncClient() as client:
        r = await client.get(f'{BASE_URL}/books')
        r.raise_for_status()
        return r.json()

async def get_history(user_id: int):
    async with httpx.AsyncClient() as client:
        r = await client.get(f'{BASE_URL}/history/{user_id}')
        r.raise_for_status()
        return r.json()

async def post_history(payload: dict):
    async with httpx.AsyncClient() as client:
        r = await client.post(f'{BASE_URL}/history', json=payload)
        r.raise_for_status()
        return r.json()
