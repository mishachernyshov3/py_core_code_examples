# Створити клас країни для онлайн-гри. Перевизначити магічні методи, додати гетери та сетери,
# статичні методи та методи класу.
import re

countries = []


class IsNotInCountry(Exception):
    pass


class Country:
    def __init__(self, name, population=0, lands=None):
        if lands is None:
            lands = set()

        self.__validate_name(name)
        self.__validate_population(population)

        self.name = name
        self.lands = lands
        self.__population = population

        countries.append(self)

    @staticmethod
    def __validate_population(value):
        if not (isinstance(value, int) and value >= 0):
            raise ValueError

    @staticmethod
    def __validate_name(value):
        if not re.match(r'([a-zA-Z_-]+)', value):
            raise ValueError

    def __iadd__(self, new_land):
        if isinstance(new_land, str) and new_land:
            for country in countries:
                if new_land in country.lands:
                    country -= new_land
            self.lands.add(new_land)
            return self
        raise ValueError

    def __isub__(self, land_to_delete):
        if isinstance(land_to_delete, str) and land_to_delete:
            try:
                self.lands.remove(land_to_delete)
            except KeyError as exc:
                raise IsNotInCountry from exc
            else:
                return self
        raise ValueError

    def __ilshift__(self, people_count):
        if isinstance(people_count, int):
            self.__population += people_count
            return self
        raise ValueError

    def __irshift__(self, people_count):
        if isinstance(people_count, int) and people_count <= self.__population:
            self.__population -= people_count
            return self
        raise ValueError

    def __lt__(self, other):
        return self.__population < other.population

    @property
    def population(self):
        return self.__population

    @population.setter
    def population(self, value):
        self.__validate_population(value)
        self.__population = value

    def __gt__(self, other):
        return self.__population > other.population

    def __str__(self):
        return f'{self.name};{self.population};{",".join(self.lands)}'

    @classmethod
    def from_string(cls, country_string):
        if country_match := re.match(r'([a-zA-Z_-]+);(\d+);(([a-zA-Z-]+,?)+)', country_string):
            name = country_match.group(1)
            population = int(country_match.group(2))
            lands = set(country_match.group(3).split(','))
            return cls(name=name, population=population, lands=lands)
        return ValueError


print(Country.from_string('CountryA;1000;LandA,LandB,LandC'))
