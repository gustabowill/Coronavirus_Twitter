from classe import Country
import json
import requests
from bs4 import BeautifulSoup
from google_trans_new import google_translator


class Scrapping:

    # Retorna a tabela da página com as informações
    @staticmethod
    def get_page_content():

        url = "https://www.worldometers.info/coronavirus/"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        table = soup.find("table", class_="main_table_countries").find_all("tr")
        table_rows = [row.text.split("\n") for row in table[9:230]]

        return table_rows

    # Faz o tratamento dos dados
    @staticmethod
    def process_data(table_rows):
        translator = google_translator()
        with open("emojis.json", "r", encoding="utf-8") as emojis:
            json_emojis = json.loads(emojis.read())

        for row in table_rows:

            for i in range(len(row)):
                # Remove espaços em branco
                row[i] = row[i].strip()

                # Remove. Este não é um país
                if row[i] == "Diamon Princess":
                    table_rows.remove(row)
                # Substitui valores inexistentes por 0
                elif row[i] == "":
                    row[i] = 0

                # Altera os nomes que se encontram de forma diferente
                elif row[i] == "USA":
                    row[i] = "United States"
                elif row[i] == "S. Korea":
                    row[i] = "South Korea"
                elif row[i] == "UK":
                    row[i] = "United Kingdom"
                elif row[i] == "UAE":
                    row[i] = "United Arab Emirates"
                elif row[i] == "Ivory Coast":
                    row[i] = "Côte d'Ivoire (Ivory Coast)"

                # Converte todos as strings numéricas para integer
                try:
                    row[i] = int(row[i].replace(",", ""))
                except:
                    pass
           
            # Adiciona os emojis de cada país
            for emoji in json_emojis:
                if emoji["name"] == row[2]:
                    row.append(emoji["emoji"])
                    break
            
            # Traduz os nomes dos países e continentes // leva alguns segundos
            try:                
                name = translator.translate(text=row[2], lang_src='en', lang_tgt="pt")
                if type(name) == list:
                    row[2] = name[1]
                else:
                    row[2] = name
                row[16] = translator.translate(text=row[16], lang_src='en', lang_tgt="pt").strip()
            except:
                print("Não foi possível fazer a tradução")


            if row[16] == "Austrália / Oceania.":
                row[16] = "Austrália / Oceania"

        return table_rows

    # Cria os objetos
    @staticmethod
    def create_objects(table_rows):

        objects_list = []

        for row in table_rows:

            country_object = Country(
                name=row[2],
                continent=row[16],
                emoji=row[-1],
                total_cases=row[3],
                total_deaths=row[5],
                total_recovered=row[7],
                total_tests=row[13],
            )

            objects_list.append(country_object)

        return objects_list

    # Pega as informações levando em conta o mundo inteiro
    @staticmethod
    def get_world_total():

        url = "https://www.worldometers.info/coronavirus/"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        table = soup.find("table", class_="main_table_countries").find_all("tr")
        row = table[8].text.split("\n")

        world_total = Country(
            name="Mundo",
            continent="Mundo",
            emoji="U+1F30E",
            total_cases=row[3],
            total_deaths=row[5],
            total_recovered=row[7],
            total_tests=row[13],
        )

        return world_total

    #Filtra os objetos por continente
    @staticmethod
    def get_continent_info(name):
        data = Scrapping.get_page_content()
        formatted_data = Scrapping.process_data(data)
        objects = Scrapping.create_objects(formatted_data)

        if name == 'Mundo':
            return objects
        continent_objects = [obj for obj in objects if obj.continent == name]
        return continent_objects
