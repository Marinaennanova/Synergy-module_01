""" Подсчет гласных букв """
import requests
import json
def get_wikipedia_content(url):

     try:
        response = requests.get(url)
        print(response.status_code)
        print(response.json())

     except requests.exceptions.RequestException as e:
            print("Возникла ошибка запроса:", e)

get_wikipedia_content(url= "https://ru.wikipedia.org/wiki/Python")

""" Получение текущего курса доллара """
import requests
try:
    response = requests.get(" https://www.cbr.ru/currency_base/daily")
    print(response.status_code)
    index = response.text.find("Доллар США")
    index = response.text.find("<td>", index)
    index_end = response.text.find("</td>", index)
    dollar_rate = response.text[index + 4:index_end]

    print("Текущий курс доллара", dollar_rate)
except requests.exceptions.RequestException as e:
       print("Возникла ошибка запроса:", e)








