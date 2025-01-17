import pytest
from httpx import AsyncClient
from app.main import app
from app.database import database

@pytest.fixture(scope="module")
async def test_client():
    async with AsyncClient(app=app, base_url="http://test") as client:
        await database.connect()
        yield client
        await database.disconnect()

@pytest.mark.asyncio
async def test_add_site(test_client):
    payload = {
        "url": "https://example.com",
        "check_interval_seconds": 300,
        "name": "Test Website",
        "expected_status_code": 200,
    }
    response = await test_client.post("/sites", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["url"] == payload["url"]

@pytest.mark.asyncio
async def test_list_sites(test_client):
    response = await test_client.get("/sites")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0

@pytest.mark.asyncio
async def test_delete_site(test_client):
    # Assuming the first site's ID is 1
    response = await test_client.delete("/sites/1")
    assert response.status_code == 200
    assert response.json()["message"] == "Site deleted successfully"
