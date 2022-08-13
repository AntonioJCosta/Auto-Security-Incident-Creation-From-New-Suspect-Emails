import json

import requests
from flatten_dict import flatten, unflatten


def auth_request(json_data: dict, url: str, username: str, passw: str) -> str:
    """
    It receives a dictionary with the body and headers of the request, a url from Archer and returns a SessionToken str response
    from the request

    :param json_data: dict = {
    :type json_data: dict
    :return: A string format SessionToken
    """
    url = f"{url}/platformapi/core/security/login"
    # Flatten function necessary to update the dict request with correct parameters from Archer API
    flatten_json_data = flatten(json_data)
    flatten_json_data[("AuthBody", "username")] = username
    flatten_json_data[("AuthBody", "password")] = passw
    json_data = unflatten(flatten_json_data)
    body = json_data["AuthBody"]
    headers = json_data["AuthHeaders"]
    try:
        request = requests.post(
            url,
            json=json.dumps(body),
            headers=headers,
        )
        try:
            return request.json()["RequestedObject"]["SessionToken"]
        except Exception:
            return request.json()
    except requests.exceptions.ConnectionError as e:
        raise ValueError(f"Failed Request: {e}")
