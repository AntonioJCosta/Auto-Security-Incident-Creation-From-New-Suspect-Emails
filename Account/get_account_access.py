from O365 import Account, FileSystemTokenBackend


def get_account_access(
    acc_to_acess: str,
    app_id: str,
    app_secret: str,
    token_path: str,
    token_filename: str,
    tenant_id: str,
):
    """
    Get an access token for the user's account.

    :param account_to_acess: The account to access.
    :param app_id: The application ID.
    :param app_secret: The application secret.
    :param tenant_id: The tenant ID.
    :return: Account object to acess.
    """

    credentials = (app_id, app_secret)

    token_backend = FileSystemTokenBackend(token_path, token_filename)
    account = Account(
        credentials,
        auth_flow_type="authorization",
        token_backend=token_backend,
        tenant_id=tenant_id,
    )

    if not account.is_authenticated:
        try:
            account.authenticate(scopes=["basic", "message_all"])
            return account
        except Exception as e:
            raise Exception(f"Authentication failed: {e}")
    return account
