from main import *
from unittest.mock import patch
from Yandex_api import YaUploader


def test_get_doc_owner_name():
    with patch('builtins.input', return_value='2207 876234'):
        assert get_doc_owner_name() == 'Василий Гупкин'


def test_add_new_doc():
    with patch('builtins.input', side_effect=['1234', 'passport', 'Петр Петров', '3']):
        assert [{"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
                {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
                {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
                {"type": "passport", "number": "1234", "name": "Петр Петров"}] == add_new_doc()


def test_delete_doc():
    with patch('builtins.input', return_value='2207 876234'):
        assert [{"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
                {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}] == delete_doc()


def test_create_new():
    token = ...
    ya = YaUploader(token)
    assert ya.create_folder('test') == 201


def test_create_wrong_token():
    token = 'gibberish'
    ya = YaUploader(token)
    assert ya.create_folder('test') == 401  # Тест, использующий некорректный токен


def test_create_existed():
    token = ...
    ya = YaUploader(token)
    assert ya.create_folder('test_exist') == 409  # Тест аналогичен предыдущему, однако теперь папка уже существует
