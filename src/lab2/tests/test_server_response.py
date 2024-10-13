from requests.exceptions import ConnectionError
import src.lab2.client as client
import pytest

from src.lab2.museum.thematic_collection import ThematicCollection

_COLLECTION_TEST_DATA = [
    [ThematicCollection(1, "Искусство", "Основная коллекция искусства", 0)],
    [ThematicCollection(2,"Искусство эпохи Просвещения", "Коллекция искусства, созданного в эпоху Просвещения", 0),
     ThematicCollection(3, "Искусство Ренессанса", "Коллекция произведений искусства Ренессанса", 0),
     ThematicCollection(4, "Искусство Нового времени", "Коллекция искусства нового времени", 0)]
]

@pytest.mark.parametrize("user_id, expected_name", [(1, "denis"), (2, "igor"), (3, "ilya")])
def test_get_user_name(user_id, expected_name):
    try:
        actual_name = client.get_user_name(user_id)
        assert actual_name == expected_name
    except ConnectionError:
        pytest.skip("Сервер недоступен. Тест пропущен")
    except Exception as e:
        pytest.fail(f"Возникла ошибка: {e}")

@pytest.mark.parametrize("user_id, user_name", [(4, "denis"), (5, "alex"), (6, "ivan")])
def test_add_user(user_id, user_name):
    try:
        client.add_user(user_id, user_name)
    except ConnectionError:
        pytest.skip("Сервер недоступен. Тест пропущен")
    except Exception as e:
        pytest.fail(f"Возникла ошибка: {e}")

@pytest.mark.parametrize("collection_id, expected_collection",
                         [(0, _COLLECTION_TEST_DATA[0]),
                          (1, _COLLECTION_TEST_DATA[1])])
def test_get_collection_data(collection_id, expected_collection):
    try:
        actual_collection = client.get_collection_data(collection_id)
        assert actual_collection == expected_collection
    except ConnectionError:
        pytest.skip("Сервер недоступен. Тест пропущен")
    except Exception as e:
        pytest.fail(f"Возникла ошибка: {e}")