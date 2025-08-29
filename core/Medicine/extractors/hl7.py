import requests
from bs4 import BeautifulSoup


class FHIRPageExtractorException(Exception):
    pass


class FHIRPageExtractor(object):
    def __init__(self, url: str = None):
        self.url = url or 'https://hl7.org/fhir/valueset-allergyintolerance-code.html'
        self.content: str = ''
        self.data: list[dict] = list()

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

        rows = table.find_all('tr')[1:]

        for row in rows:
            cols = row.find_all('td')
            if len(cols) < 3:
                continue
            code = cols[0].get_text(strip=True).split()[0]
            name = cols[2].get_text(strip=True)
            self.data.append({'name': name, 'code': code})

        return self.data
