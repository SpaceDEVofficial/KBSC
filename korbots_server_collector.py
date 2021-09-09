import pickle
import aiohttp
from discord.ext import tasks
import aiofiles
import asyncio

with open("server/db/serversdata.bin", "rb") as ff:
    servers_count_list = pickle.load(ff)

@tasks.loop(minutes=10)
async def req_timer():
    async with aiohttp.ClientSession() as cs:
        async with cs.get("https://koreanbots.dev/api/v2/bots/807262470347030545") as res:
            re = await res.json()
            servs = re["data"]["servers"]
            servers_count_list.append(servs)
            async with aiofiles.open("server/db/serversdata.bin", "wb") as f:
                await f.write(pickle.dumps(servers_count_list))
            print(f"Updated. Servers: {servs}")


req_timer.start()

asyncio.get_event_loop().run_forever()
