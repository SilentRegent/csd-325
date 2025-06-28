def city_country(city, country, population=None, language=None):
    """Return a formatted string of city, country, optional population, and language."""
    result = f"{city.title()}, {country.title()}"
    if population:
        result += f" - population {population}"
    if language:
        result += f", {language.title()}"
    return result

# Call the function at least three times with increasing arguments

# City and Country only
print(city_country("santiago", "chile"))

# City, Country, and Population
print(city_country("tokyo", "japan", 13929286))

# City, Country, Population, and Language
print(city_country("paris", "france", 2148327, "french"))
