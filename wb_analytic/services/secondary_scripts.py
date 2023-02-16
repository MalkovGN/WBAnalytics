import os
import json

from wb_analytic_app import models
from .json_parser import JsonParser


def clear_static_directory():
    """
    Delete old downloaded
    json files
    """
    directory = f'{os.getcwd()}/services/static/services/'
    for f in os.listdir(directory):
        os.remove(os.path.join(directory, f))


def collect_main_info():
    """
    Parse a JSON file with categories
    Getting necessary info
    :return: A list of unique subcategories subcategory_info
    """
    with open(f'{os.getcwd()}/wb_analytic_app/static/wb_analytic_app/categories_info.json', 'r', encoding='utf-8') as file:
        data_json = json.load(file)

    all_urls = []

    for elem in data_json:
        test_json = JsonParser(elem)
        test_json.start()
        all_urls += test_json.subcategory_info

    return all_urls


def get_full_info_categories(subcategories_info):
    """
    :param subcategories_info: JSON with all subcategories
    :return: The list only with shard and query params
    """
    full_info_subcategories = []

    for subcategory in subcategories_info:
        if 'shard' not in subcategory.keys():
            continue
        else:
            full_info_subcategories.append(subcategory)

    return full_info_subcategories


def get_categories_without_shard(subcategories_info):
    """
    :param subcategories_info: JSON with all subcategories
    :return: The list with subcategories which has not
    shard and query params
    """
    categories_without_shard = []

    for subcategory in subcategories_info:
        if 'shard' not in subcategory.keys():
            categories_without_shard.append(subcategory)

    return categories_without_shard
