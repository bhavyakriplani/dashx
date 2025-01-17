import pytest
from app.discord import send_discord_notification
import responses

@pytest.mark.asyncio
@responses.activate
async def test_send_discord_notification():
    responses.add(
        responses.POST,
        "https://discord.com/api/webhooks/your_webhook_id/your_token",
        status=204,
    )
    await send_discord_notification("Test Alert", "This is a test notification")
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == "https://discord.com/api/webhooks/your_webhook_id/your_token"
