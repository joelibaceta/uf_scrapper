import requests
import re


class UFScrapper:
    """This class is in charge of scrapping the UF value from the SII website"""

    def __init__(self) -> None:
        self.base_url = "https://www.sii.cl/valores_y_fechas/uf"

    def get_uf_value(self, year: int, month: int, day: int) -> float:
        """Returns the UF value for the given date"""

        self.__validate_requested_date(year, month, day)

        url = f"{self.base_url}/uf{year}.htm"
        response = requests.get(url)

        if response.status_code == 200:
            raw_html = response.text
            match_pattern = re.compile(
                r'<table.+table_export"[^>]+>(.*?)<\/table>', re.DOTALL
            )
            match = match_pattern.findall(raw_html)[0]
            return self.__parse_table_section(match, month, day)
        else:
            raise Exception("Error while scrapping the UF value")

    def __validate_requested_date(self, year: int, month: int, day: int) -> None:
        if year < 2013:
            raise Exception("Year must be equal or greater than 2013")

        if month < 1 or month > 12:
            raise Exception("Month must be between 1 and 12")

        if day < 1 or day > 31:
            raise Exception("Day must be between 1 and 31")

    def __parse_table_section(self, section_raw: str, month: int, day: int) -> float:
        row_pattern = re.compile(r"<tr[^>]*>(.*?)<\/tr>", re.DOTALL)
        row_matchs = row_pattern.findall(section_raw)

        if day > len(row_matchs):  # The day is not in the table
            raise Exception("Expected day has not been found in SII website")

        return self.__parse_row(row_matchs[day], month, day)

    def __parse_row(self, row_raw: str, month: int, day: int) -> float:
        montly_values_pattern = re.compile(r"[^<]*<td[^>]*>([\d,.]+)<\/td>", re.DOTALL)
        day_number_pattern = re.compile(r"<th[^>]*>(.*)<\/th>", re.DOTALL)

        day_number = day_number_pattern.search(row_raw).group(1)

        if int(day_number) != day:  # Check if the day is the expected one
            raise Exception(
                "Ups!, something went wrong during parsing"
            )  # Something went wrong

        monthly_values = montly_values_pattern.findall(row_raw)

        if month > len(monthly_values):  # The month is not in the table
            raise Exception("Expected month has not been found in SII website")

        expected_value = monthly_values[month - 1]
        return float(expected_value.replace(".", "").replace(",", "."))
