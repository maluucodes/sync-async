import asyncio
import httpx
from django.http import HttpResponse

# async views exercise
async def http_call_async():
    for num in range(1, 6):
        await asyncio.sleep(1)
        print(num)

    async with httpx.AsyncClient() as client:
        response = await client.get("https://httpbin.org/")
        print(response.status_code)


async def async_view(request):
    asyncio.create_task(http_call_async())
    return HttpResponse("Async started!")