import asyncio, json, os, pty, subprocess
from urllib.parse import urlparse, parse_qs
import websockets

async def handler(ws):
    qs = parse_qs(urlparse(ws.path).query)
    if not qs.get("token"):
        await ws.close(code=4001, reason="token required")
        return
    master, slave = pty.openpty()
    proc = subprocess.Popen(["/bin/sh"], stdin=slave, stdout=slave, stderr=slave, text=False)

    async def read_pty():
      loop = asyncio.get_event_loop()
      while True:
        data = await loop.run_in_executor(None, os.read, master, 1024)
        if not data:
          break
        await ws.send(data.decode(errors="ignore"))

    reader = asyncio.create_task(read_pty())
    try:
        async for msg in ws:
            frame = json.loads(msg)
            if frame.get("type") == "stdin":
                os.write(master, frame.get("data", "").encode())
    finally:
        reader.cancel()
        proc.terminate()

async def main():
    async with websockets.serve(handler, "0.0.0.0", 8090, ping_interval=20, ping_timeout=20):
        await asyncio.Future()

asyncio.run(main())
