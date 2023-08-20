import asyncio
import socket

async def check_online_device(ip):
    try:
        _, _ = await asyncio.wait_for(
            asyncio.open_connection(ip, 80),
            timeout=1
        )
        return ip
    except (OSError, asyncio.TimeoutError):
        return None

async def find_online_devices():
    tasks = []
    online_devices = []

    for i in range(1, 255):
        ip = f'192.168.1.{i}'
        tasks.append(check_online_device(ip))

    online_results = await asyncio.gather(*tasks)
    online_devices = [ip for ip in online_results if ip is not None]

    return online_devices

async def main():
    online_devices = await find_online_devices()
    print(online_devices)

if __name__ == '__main__':
    asyncio.run(main())
