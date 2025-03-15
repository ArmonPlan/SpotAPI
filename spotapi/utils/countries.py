from typing import NamedTuple, Optional

class CountryCode(NamedTuple):
    name: str
    code: str

class Country:
    # Major European Countries
    FRANCE = CountryCode("France", "fr")
    UK = CountryCode("United Kingdom", "uk")
    GERMANY = CountryCode("Deutschland", "de")
    ITALY = CountryCode("Italia", "it")
    SPAIN = CountryCode("España", "es")
    NETHERLANDS = CountryCode("Nederland", "nl")
    BELGIUM_FR = CountryCode("Belgique (français)", "be-fr")
    BELGIUM_NL = CountryCode("België (Nederlands)", "be-nl")
    SWEDEN = CountryCode("Sverige", "se")
    NORWAY = CountryCode("Norge", "no-nb")
    DENMARK = CountryCode("Danmark", "dk-da")
    SWITZERLAND_DE = CountryCode("Schweiz (Deutsch)", "ch-de")
    SWITZERLAND_FR = CountryCode("Suisse (français)", "ch-fr")
    PORTUGAL = CountryCode("Portugal", "pt-pt")
    IRELAND = CountryCode("Ireland", "ie")

    # North America
    USA = CountryCode("USA", "us")
    CANADA_EN = CountryCode("Canada (English)", "ca-en")
    CANADA_FR = CountryCode("Canada (Français)", "ca-fr")
    MEXICO = CountryCode("México", "mx")

    # South America
    BRAZIL = CountryCode("Brasil", "br-pt")
    ARGENTINA = CountryCode("Argentina", "ar")
    COLOMBIA = CountryCode("Colombia", "co-es")
    CHILE = CountryCode("Chile", "cl")

    # Asia Pacific
    JAPAN = CountryCode("日本", "jp")
    KOREA = CountryCode("대한민국", "kr-ko")
    CHINA_HK = CountryCode("香港", "hk-zh")
    SINGAPORE = CountryCode("Singapore", "sg-en")
    AUSTRALIA = CountryCode("Australia", "au")
    NEW_ZEALAND = CountryCode("New Zealand", "nz")
    INDIA = CountryCode("India", "in-en")
    TAIWAN = CountryCode("台灣", "tw")

    # Middle East
    UAE_EN = CountryCode("United Arab Emirates", "ae-en")
    UAE_AR = CountryCode("الإمارات العربية المتحدة", "ae-ar")
    SAUDI_ARABIA = CountryCode("Saudi Arabia", "sa-en")
    ISRAEL = CountryCode("Israel", "il-en")

    # Major African Markets
    SOUTH_AFRICA = CountryCode("South Africa", "za-en")
    NIGERIA = CountryCode("Nigeria", "ng")
    EGYPT = CountryCode("Egypt", "eg-en")
    MOROCCO = CountryCode("Maroc", "ma-fr")
	
	#Could add the whole list but not sure if it's useful

    @classmethod
    def get_code(cls, country_code: CountryCode) -> str:
        """Returns just the country code from a CountryCode object"""
        return country_code.code

    @classmethod
    def get_name(cls, country_code: CountryCode) -> str:
        """Returns just the name from a CountryCode object"""
        return country_code.name

    @classmethod
    def from_code(cls, code: str) -> Optional[CountryCode]:
        """Finds a CountryCode object by its code."""
        for attr in dir(cls):
            if not attr.startswith("_"):  # Ignore private attributes
                country = getattr(cls, attr)
                if isinstance(country, CountryCode) and country.code == code:
                    return country
        return None

    @classmethod
    def from_name(cls, name: str) -> Optional[CountryCode]:
        """Finds a CountryCode object by its name."""
        for attr in dir(cls):
            if not attr.startswith("_"):  # Ignore private attributes
                country = getattr(cls, attr)
                if isinstance(country, CountryCode) and country.name == name:
                    return country
        return None