import asyncio
from bleak import BleakScanner, BleakClient

# enumerate devices

async def main():
    devices = await BleakScanner.discover()
    for d in devices:
        print(d)

asyncio.run(main())

