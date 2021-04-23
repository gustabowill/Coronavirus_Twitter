import json

class Country:
    def __init__(self, name, continent, emoji, total_cases, total_deaths, total_recovered, total_tests):
        self.name = name
        self.continent = continent
        self.emoji = emoji
        self.total_cases = total_cases
        self.total_deaths = total_deaths
        self.total_recovered = total_recovered
        self.total_tests = total_tests

        if self.total_tests == 0:
            self.total_tests = "Indisponível"

    @property
    def fatality(self):
        fatality_n = (self.total_deaths / self.total_cases) * 100
        fatality = f"{'%.1f' % fatality_n}%"

        return fatality

    @property
    def data_text(self):
        total_tests = self.total_tests
        if total_tests != 'Indisponível':
            total_tests = f'{total_tests:,}'

        text = f"{self.emoji}{self.name}{self.emoji}\n\n\U0001F637Casos: {self.total_cases:,}\n\u2620\uFE0FMortes: {self.total_deaths:,}\n\U0001F340Recuperados: {self.total_recovered:,}\n\u203C\uFE0FMortalidade: {self.fatality}\n\U0001F9EATestes feitos: {total_tests}\n\n#Coronavírus".replace(',', '.')

        return text

    def __str__(self):
        return f"{self.name}"
