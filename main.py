from Virgule import addV
#addV()

import time
from scrapping.scrapping import Scrapper2

with Scrapper2() as bot:
    bot.land_first_page()
    #bot.collectTabledata()
    bot.CollectMaquetteData()