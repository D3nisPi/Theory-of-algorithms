import base64
import json
import requests
from src.lab2.museum.article import Article
from src.lab2.museum.exhibit import Exhibit
from src.lab2.museum.thematic_collection import ThematicCollection
from src.lab2.museum.virtual_museum_object import VirtualMuseumObject
from typing import List, Dict, Any

host = "localhost"
port = "8080"
server_uri = f"http://{host}:{port}/api"

def get_collection_data(collection_id: int) -> List[VirtualMuseumObject]:
    params = {
        'action': 'get_collection',
        'collection_id': collection_id
    }

    response = requests.get(server_uri, params=params)
    if response.status_code != 200:
        raise requests.HTTPError(f"Ошибка: {response.status_code} - {response.json().get('error', 'No information')}")

    json_data = response.json()

    collection_items = []
    for json_item in json_data:
        item_id, item_title, descr, item_type, views, data = (
            json_item.get('id', None), json_item.get('title', None), json_item.get('descr', None),
            json_item.get('type', None), json_item.get('views', None), json_item.get('data', None)
        )

        match item_type:
            case 0:
                collection_items.append(ThematicCollection(item_id, item_title, descr, views))
            case 1:
                collection_items.append(Article(item_id, item_title, descr, views, data))
            case 2:
                image_data = base64.b64decode(data)
                collection_items.append(Exhibit(item_id, item_title, descr, views, image_data))
            case _:
                raise ValueError(f"Invalid item type: {item_type}")

    return collection_items

def update_user_views(user_id: int, item_id: int, views: int) -> None:
    params = {
        'action': 'update_user_views'
    }
    data = {
        'user_id': user_id,
        'item_id': item_id,
        'views': views
    }

    response = requests.patch(server_uri, params=params, data=json.dumps(data))
    if response.status_code != 201:
        raise requests.HTTPError(f"Ошибка: {response.status_code} - {response.json().get('error', 'No information')}")

def add_user(user_id: int, name: str) -> None:
    params = {
        'action': 'add_user'
    }
    data = {
        'id': user_id,
        'name': name
    }

    response = requests.post(server_uri, params=params, data=json.dumps(data))
    if response.status_code != 201:
        raise requests.HTTPError(f"Ошибка: {response.status_code} - {response.json().get('error', 'No information')}")

def get_user_name(user_id: int) -> str | None:
    params = {
        'action': 'get_user_name',
        'id': user_id,
    }

    response = requests.get(server_uri, params=params)
    if response.status_code != 200:
        raise requests.HTTPError(f"Ошибка: {response.status_code} - {response.json().get('error', 'No information')}")

    json_data = response.json()

    return json_data.get('name', None)

def get_user_info(user_id: int) -> List[Dict[Any, Any]]:
    params = {
        'action': 'get_user_info',
        'id': user_id,
    }

    response = requests.get(server_uri, params=params)
    if response.status_code != 200:
        raise requests.HTTPError(f"Ошибка: {response.status_code} - {response.json().get('error', 'No information')}")

    json_data = response.json()

    return json_data