# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/
# This is a simple example for a custom action which utters "Hello World!"
import json
import logging
import random
from token import AT
from typing import Dict, Text, Any, List, Union, Optional
from rasa_sdk.types import DomainDict
import psycopg2
from rasa_sdk import Action, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, FollowupAction, AllSlotsReset, EventType, ConversationPaused, UserUtteranceReverted
import requests
from rasa_sdk import Tracker


class ActionGetProduct(Action):
    def name(self):
        return 'action_product'

    def run(self, dispatcher, tracker, domain):
        user = tracker.get_slot('user')
        url = 'https://fakestoreapi.com/products'
        print(url)
        headers = {'Content-Type': 'application/json'}
        request = requests.get(url,  headers=headers)
        if request.status_code == 200:
            response = request.content
            response = response.decode('utf-8')
            response = json.loads(response)
            dispatcher.utter_message(json_message=response)
            return []
        else:
            dispatcher.utter_message(text='I am facing some issues, please try again later!!!')


class ActionGetCategories(Action):
    def name(self):
        return 'action_categories_list'

    def run(self, dispatcher, tracker, domain):
        url = 'https://fakestoreapi.com/products/categories'
        print(url)
        headers = {'Content-Type': 'application/json'}
        request = requests.get(url,  headers=headers)
        if request.status_code == 200:
            response = request.content
            response = response.decode('utf-8')
            response = json.loads(response)
            dispatcher.utter_message(json_message=response)
            return []
        else:
            dispatcher.utter_message(text='I am facing some issues, please try again later!!!')


class ActionShopCategory(Action):
    def name(self):
        return 'action_shop_by_category'

    def run(self, dispatcher, tracker, domain):

        cate = tracker.get_slot('category')
        cate= cate.lower()
        url = 'https://fakestoreapi.com/products/category/'+cate
        print(url)
        headers = {'Content-Type': 'application/json'}
        request = requests.get(url,  headers=headers)
        if request.status_code == 200:
            response = request.content
            response = response.decode('utf-8')
            response = json.loads(response)
            dispatcher.utter_message(json_message=response)
            return []
        else:
            dispatcher.utter_message(text='I am facing some issues, please try again later!!!')