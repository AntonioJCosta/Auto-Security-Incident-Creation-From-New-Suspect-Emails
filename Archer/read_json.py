import json


def read_json(json_file: str) -> dict:
    """
    "Read a JSON file and return a dictionary."

    :param json_file: The file path to the JSON file you want to read
    :type json_file: str
    :return: A dictionary
    """

    with open(json_file, "r") as data:
        return json.load(data)
