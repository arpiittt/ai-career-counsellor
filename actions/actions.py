from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionRecommendCareer(Action):
    def name(self) -> Text:
        return "action_recommend_career"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        latest_intent = tracker.latest_message['intent'].get('name')

        if latest_intent == "inquire_tech_interest":
            dispatcher.utter_message(response="utter_recommend_tech")
        elif latest_intent == "inquire_arts_interest":
            dispatcher.utter_message(response="utter_recommend_arts")
        elif latest_intent == "inquire_commerce_interest":
            dispatcher.utter_message(response="utter_recommend_commerce")
        else:
            dispatcher.utter_message(response="utter_default")

        return []
