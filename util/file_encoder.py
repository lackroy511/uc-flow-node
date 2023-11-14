import base64
from typing import Dict

import aiohttp


async def download_file(download_link: str) -> Dict[str, str]:
    """Скачивает файл и возвращает его в формате base64, utf-8"""
    async with aiohttp.ClientSession() as session:
        async with session.get(download_link) as response:
            if response.status == 200:
                data = await response.read()
                return {
                    'file_in_base64': base64.b64encode(data).decode('utf-8'),
                }
            
            return {'message': 'failed'}
