# Este arquivo contém uma custom action que utiliza código python
# para executar ações no diálogo.
#
# Veja o guia na documentação do RASA em:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/

import requests

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/auto-complete"

querystring = {"q":"tesla","region":"BR"}

headers = {
    'x-rapidapi-key': "00265dacebmsh5806171a71a7de1p1c9fa8jsnf5940c6fd9fc",
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

class ActionStock(Action):
    def name(self) -> Text:
        return "action_stocks"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        try:
            dispatcher.utter_message(print(response.text))
        except ValueError:
            dispatcher.utter_message(ValueError)
        return []
