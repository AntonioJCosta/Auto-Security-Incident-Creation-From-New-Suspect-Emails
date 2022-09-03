import time

import requests
from flatten_dict import flatten, unflatten

from .format_mail import format_mail


def create_incident(json_data: dict, mail_details: dict, session_token: str, url: str):
    """
    It takes a json_data dict, a mail_details dict and a session_token string as arguments, open a ArcherEvent with mail_details returns
    a json response

    :param json_data: dict = The json data that is returned from the get_json_data function
    :type json_data: dict
    :param mail_details: a dictionary containing the subject and body of the email
    :type mail_details: dict
    :param session_token: The session token that you get from the login function
    :type session_token: str
    :param url: The url of the Archer Endpoint
    :type url: str
    :return: A dict json format response
    """

    incident_desc_formatted = format_mail(mail_details)
    url = f"{url}/platformapi/core/content"
    # Flatten function necessary to update the dict request with correct parameters from json_file
    flatten_json_data = flatten(json_data)
    # Set session token in the request header
    flatten_json_data[
        ("OpenEventHeaders", "Authorization")
    ] = f"Archer session-id={session_token}"
    title_id = list(json_data["OpenEventParameters"]["Content"]["FieldContents"])[0]
    incident_desc_id = list(
        json_data["OpenEventParameters"]["Content"]["FieldContents"]
    )[1]
    # Incident title
    mail_subject = mail_details["Subject"]
    flatten_json_data[
        ("OpenEventParameters", "Content", "FieldContents", title_id, "Value")
    ] = {mail_subject}
    # Incident description
    flatten_json_data[
        (
            "OpenEventParameters",
            "Content",
            "FieldContents",
            incident_desc_id,
            "Value",
        )
    ] = incident_desc_formatted
    json_data = unflatten(flatten_json_data)
    body = json_data["OpenEventParameters"]
    headers = json_data["OpenEventHeaders"]
    is_incident_created = False
    # While block necessary to fix Archer API bug for some requests
    while not is_incident_created:
        try:
            request = requests.post(url, json=body, headers=headers)
            response = request.json()
            try:
                event_id = response["RequestedObject"]["Id"]
                with open("application_log.log", "a") as f:
                    f.write(
                        f"New incident created - {event_id} \n time of creation: {time.strftime('%Y-%m-%d %H:%M:%S')}"
                    )
                is_incident_created = True
                return response
            except KeyError:
                time.sleep(1)
                pass
        except requests.exceptions.ConnectionError as e:
            with open("application_log.log", "a") as f:
                f.write(
                    f"Request error: {e} \n time of error: {time.strftime('%Y-%m-%d %H:%M:%S')}"
                )
            raise ValueError(f"Request Error: {e}")
