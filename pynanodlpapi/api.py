
import logging
import aiohttp

_LOGGER = logging.getLogger(__name__)

class NanoDlpApi:
    """Client for interacting with a NanoDLP API"""
    def __init__(self, base_url: str, session: aiohttp.ClientSession) -> None:
        if not base_url.endswith("/"):
            base_url += "/"
        self._base_url = base_url
        self._headers = {}
        self._session = session

    async def get_printer_status(self):

        url = self._base_url + "status"
        response = await self._session.get(url, headers=self._headers)
        return await response.json()