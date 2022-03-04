from typing import Dict, List
import requests
from bs4 import BeautifulSoup
from requests.models import Response
import base64


class Scraper:

    """
    Classe para a realização do scrapper no site http://free-proxy.cz/en/main/
    """

    base_url: str = "http://free-proxy.cz/en/main/"

    def __init__(self) -> None:
        pass

    @classmethod
    def _requester(cls, page: int = 1) -> Response:
        """
        Realiza a conexão com o site e retorna a resposta

        args:
            page: número da página para se realizar a raspagem

        """
        response: Response = requests.get(
            f"http://free-proxy.cz/en/main/{page}",
            headers={"User-Agent": "Mozilla/5.0"},
        )
        if response.status_code == 200:
            return response
        else:
            return None

    def _data_processor(self, soup: BeautifulSoup) -> List[Dict]:
        """
        Função para processar os dados

        args:
            soup: html analisado pela biblioteca bs4
        """
        table = soup.find_all("table")[1]
        headers = [
            header.text.replace(" ", "_").lower() for header in table.find_all("th")
        ]
        results = [
            {
                headers[i]: cell.text.strip() or cell.find("script")
                for i, cell in enumerate(row.find_all("td"))
            }
            for row in table.find_all("tr")
        ]
        for result in results:
            if result:
                result["ip_address"] = self._decode_ip_address(result["ip_address"])
        return results

    def _decode_ip_address(self, result: str) -> str:
        """
        Função para decodificar o ip address disponibilizado na tabela do site.
        Foi verificado que no html, o ip está codificado em base64, por isso foi
        necessária a criação dessa função

        args:
            result: o ip_address codificado

        """
        if result.string:
            base64_encoded = result.string.split('"')[-2]
            message_bytes = base64.b64decode(base64_encoded)
            return message_bytes.decode("ascii")
        else:
            return ""

    def crawler(self):
        """
        Função para executar a raspagem
        """
        response = self._requester()
        soup = BeautifulSoup(response.text, "lxml")
        last_page = (
            soup.find_all("div", {"class": "paginator"})[0].find_all("a")[-3].text
        )
        results = self._data_processor(soup)
        for i in range(2, int(last_page) + 1):
            response = self._requester(i)
            soup = BeautifulSoup(response.text, "lxml")
            results.extend(self._data_processor(soup))
        results = [result for result in results if result.get("ip_address", None)]
        return results
