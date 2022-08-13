def format_mail(mail_details: dict) -> str:
    """
    It takes a mail_details dict as argument, formats the mail_details dict and returns a str

    :param mail_details: a dictionary containing the subject and body of the email
    :type mail_details: dict
    :return: A str mail format
    """

    formatted_mail = "".join(
        (f"<b>{key}:</b> {value}<br>\n" for key, value in mail_details.items())
    )
    print(formatted_mail)
    return formatted_mail
