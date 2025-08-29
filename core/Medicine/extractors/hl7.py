import requests
from bs4 import BeautifulSoup


class FHIRPageExtractorException(Exception):
    pass


class FHIRPageExtractor(object):
    def __init__(self, url: str):
        self.url = url
        self.content: str = ''
        self.data: list[dict] = list()
        self.headers: list[str] = list()

    def get_content(self):
        try:
            response = requests.get(url=self.url)
            response.raise_for_status()
        except Exception as e:
            raise FHIRPageExtractorException(e)

        self.content = response.content
        return self.content

    def extract_from_table(self, table_class: str = 'codes'):
        soup = BeautifulSoup(self.content, 'html.parser')
        table = soup.find('table', {'class': table_class})
        if not table:
            return []

        header_cells = table.find('tr').find_all(['td', 'th'])
        self.headers = [cell.get_text(strip=True).lower() for cell in header_cells]

        for row in table.find_all('tr')[1:]:
            cols = row.find_all('td')
            if len(cols) != len(self.headers):
                continue

            item = {}
            for h, col in zip(self.headers, cols):
                text = col.get_text(strip=True)
                item[h] = text
            self.data.append(item)

        return self.data
