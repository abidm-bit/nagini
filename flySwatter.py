import asyncio
from bleak import BleakClient

DEVICE_UUID = "E247D86B-2200-FFA6-5068-75482F8D00FC"  # UUID


# disconnect using the UUID
async def disconnect_ble():
    async with BleakClient(DEVICE_UUID) as client:
        await client.disconnect()
        print("Disconnected.")

asyncio.run(disconnect_ble())
