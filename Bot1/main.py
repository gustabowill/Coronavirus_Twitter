from twitter_api import api
from scrapping import Scrapping

from datetime import datetime
from operator import attrgetter
import time

from pytz import timezone
from googletrans import Translator
from threader import Threader


date = datetime.now()
timezone = timezone("America/Sao_Paulo")
full_date = date.astimezone(timezone)
formatted_date = full_date.strftime("Data: %d/%m/%Y às %H:%M")

continents = ['Ásia', 'Austrália / Oceania', 'África', 'Europa', 'América do Norte', 'América do Sul', 'Mundo' ]

for continent in continents:

    objects = Scrapping.get_continent_info(continent)
    objects.sort(key=attrgetter("total_cases"), reverse=True)

    thread = [obj.data_text for obj in objects[:15]]

    thread_thumb = f"""     Atualizações do #Coronavírus - {objects[0].continent}\n\n
                    {formatted_date}\n\n
                    \u26A0\uFE0FDetalhes na thread\u26A0\uFE0F"""

    thread.insert(0, thread_thumb)

    thread_maker = Threader(thread, api, wait=5, end_string=False)
    thread_maker.send_tweets()
    time.sleep(60)
