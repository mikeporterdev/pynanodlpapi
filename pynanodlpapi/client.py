import aiohttp
import logging

from pynanodlpapi.api import NanoDlpApi
from pynanodlpapi.status import NanoDlpPrinterStatus

_LOGGER = logging.getLogger(__name__)

class NanoDlpClient:

    def __init__(self, host: str, session: aiohttp.ClientSession = None, port: int = 8080) -> None:
        protocol = "http"
        self.base_url = f"{protocol}://{host}:{port}"
        _LOGGER.info(f"connecting with ${self.base_url}")
        if (session is None):
            connector = aiohttp.TCPConnector(force_close=True)
            session = aiohttp.ClientSession(connector)
        self._api = NanoDlpApi(self.base_url, session)

    async def get_status(self) -> NanoDlpPrinterStatus:
        response = await self._api.get_printer_status()
        return NanoDlpPrinterStatus(response)