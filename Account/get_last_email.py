import time
from datetime import datetime


def get_last_email(account) -> dict:
    """
    It checks for new emails, comparing the total_mails_bfr and total_mails_new_check and returns the last email's details as a dictionary

    :param account: The authenticate account
    :return: A dictionary with the last email details
    """

    try:
        mail_box = account.mailbox()
        mails_list = list(mail_box.get_messages())
        last_mail = mails_list[0]
        last_mail_sent_time_bfr = str(
            datetime.strftime(last_mail.sent, "%d/%m/%Y %H:%M:%S")
        )
    except Exception as e:
        raise Exception(f"Failed to get mail box: {e}")
    while True:
        mail_box = account.mailbox()
        mails_list = list(mail_box.get_messages())
        last_mail = mails_list[0]
        last_mail_sent_time_after = str(
            datetime.strftime(last_mail.sent, "%d/%m/%Y %H:%M:%S")
        )
        # Compare both the times and return the last mail details if times are different
        if last_mail_sent_time_bfr == last_mail_sent_time_after:
            time.sleep(0.1)
            continue
        separator = ", "
        mail_ccs = separator.join((str(cc) for cc in last_mail.cc))
        mail_tos = separator.join((str(to) for to in last_mail.to))
        formatted_date_last_email = str(
            datetime.strftime(last_mail.sent, "%d/%m/%Y %H:%M:%S")
        )
        last_mail_details = {
            "To": last_mail.sender,
            "Sent in": formatted_date_last_email,
            "To": mail_tos,
            "CC": mail_ccs,
            "Subject": last_mail.subject,
            "Content": last_mail.body_preview,
        }
        return last_mail_details
