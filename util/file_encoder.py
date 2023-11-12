import aiohttp
import base64


async def download_file(url: str) -> str:
    """Скачивает файл и возвращает его в формате base64, utf-8"""
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.read()
                return {
                    'file_in_base64': base64.b64encode(data).decode('utf-8'),
                }
            
            return {'message': 'failed'}
