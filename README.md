[Archer]: https://www.archerirm.com/
[Python]: https://www.python.org/
[python-o365]: (https://github.com/O365/python-o365)
[Microsoft Graph API]: (https://docs.microsoft.com/pt-br/graph/overview)
[Antonio Costa]: (https://github.com/Antonio-Costa00)
[portal azure]: (https://portal.azure.com/#home)

# Auto Incidents Creation From Fishing Attacks on Archer Security Incidents Platform 

![](Process_diagram.jpg)

This project aims to automate the process of creating new incidents on [Archer] security incidents platform  by collecting e-mails from fishing attacks and creating a new incident report on the platform, with all required fields covered by the automation*

Solution created using [Python] Language, [Microsoft Graph API], the library [python-o365] to collect the emails from the agency and API from the [Archer] to open our hearts on the platform.

**At the present time, at API [Archer] it is not capable of the PROVISITIVE field of ORIGIN - COMPANY GERENCY CONTEXT because of an improvement in efficiency, not in automated manufacturing. The completion of this field is within the code. According to the developers of the platform, in ⁇  it will be corrected such.*

#### Main Developer

- [Antonio Costa]

## Index

- [Creating an application on Microsoft Azure](#aplication)
- [Access to services](#application_acess)
- [Monitoring of application](#monitoring)

## Creating an application on Microsoft Azure

Creating the application it's necessary to enable the reading permission of theuser's email.

With the creation of the application, it's possible to read any email account within the box, only possessing the application ID, the tenant ID and the secret key ID.*

**Note: Only Azure administrators can create new applications unless the permission of creating new applications has been released to users.*

For app creation, the following steps should be followed:

- [1 - Application creation](#new_application)
- [2 - Generating a Secret Key](#secret_key)
- [3 - Adding new permissions](#new_permissions)

### 1 - Creation of the application
    
For access to email, it's necessary to create an application in Microsoft Azure Directory, with application permission to access the email reading permitions, that is, the user's request in question that permits you.
    
For app creation, the user must follow the following steps:
    
1. Access [portal azure]
    
1. Access Azure Active Directory
    
1. Application registration
    
1. Give a name to the application
    
1. In types of accounts supported, select Accounts in any organizational situation (any member of the Azure AD — Unique balance) 

**Note:**

  - Selecting Accounts in any organizational situation (any Azure AD members — Unique balance) only tenant accounts can access the app 

  - If someone outside the tenant tries to acess the application, the follow error will be generated: "You cannot sign in here with a personal account. Instead, use your school or professional account."

6. Selecting Platform, Web Application

1. Within url redirecting, select the address https://login.microsoftonline.com/common/oauth2/nativeclient

1. Register the app

1. Collect the application ID (client) and the tenant ID (directory).

### 2 - Generating a secret key

1. In Customer Credits, New Customer Partner
1. In return, I found a name for the ⁇ 
1. Expand in 3 months1
1. Add
1. Copy the value of ID2

*1 The ⁇  is that it is generated to secret key with the term of 3 months, however, the deadline can be changed for any date.

*2 The value of the ID is only possible to preview once, so the value of the ID should be collected ⁇  after the creation of it. Both the user and the driver responsible for automation should keep in mind the timelimit of the new vehicle. To do this, in the central Zabbix, an alarm was created in the SOC queue, with a 5-day antedence to perform the ⁇  of the building.

### 3 - Adding new permissions

1. In of API, add a permit
1. Microsoft Graph
1. Deputy ⁇ 
1. Search the third mail, and select all options.
1. Add permits.
1. After the above calculations, it is possible to verify the ⁇  of any account in the tenant of the CIP1

## Access to the Application

After the same steps, the developer should go to the printer server and perform the following procedures:

- [1 - Edit environment file](#edit_env)
- [2 - Archer API](#Archer_API)
- [3 - Access to Microsoft Graph API](#graph_api)
- [4 - Renewal of access token](#renewal_token)

### 1 - Edit environment file

1. Edit the .env environment file
1. Within the file, edit the APPLICATION_ID, SECRET_ID and TENANT_ID values, with the collected values of the creation of the application.
1. Also edit the ACCOUNT_TO_ACESS variable with the email address to be read.

### 2 - Archer credentials

1. The Archer platform relies on 3 environments, being one of development, homologation and one of production.
1. The setting for each environment is in the json_files directorio
1. Within the warden there are 3 .json files, with the necessary tools to protect each environment.
1. To change the environment within the main.py file, simply exchange the value of the JSON_FILES variable with the desired effect of the desired environment.

### 3 - Access to Microsoft Graph API

1. After following the procedures, check if in the token_t it's in the directory
1. If you have a txt file called "o365_token.txt" remove it.
1. Access the file
1. After this, return to the implementation directory, and select the command
1. The first time, a message asking for an access token had emerged.

    https://login.microsoftonline.com/4c907c5b-2c53-4c36-88b1-8620cb591696/oauth2/v2.0/authorize?response_type=code&amp;client_id=335b9f29-8028-4795-ad12-074b47377507&amp;redirect_uri=https%3A%2F%2Flogin.microsoftonline.com%2Fcommon%2Foauth2%2Fnativeclient&amp;scope=https%3A%2F%2Fgraph.microsoft.com%2FMail.ReadWrite+https%3A%2F%2Fgraph.microsoft.com%2FUser.Read+offline_access+https%3A%2F%2Fgraph.microsoft.com%2FMail.Send&amp;state=8aeBu2xHkC5x8fLaVZMUS9keC6CQ3v&amp;access_type=offlinehttps://login.microsoftonline.com/4c907c5b-2c53-4c36-88b1-8620cb591696/oauth2/v2.0/authorize?response_type=code&amp;client_id=335b9f29-8028-4795-ad12-074b47377507&amp;redirect_uri=https%3A%2F%2Flogin.microsoftonline.com%2Fcommon%2Foauth2%2Fnativeclient&amp;scope=https%3A%2F%2Fgraph.microsoft.com%2FMail.ReadWrite+https%3A%2F%2Fgraph.microsoft.com%2FUser.Read+offline_access+https%3A%2F%2Fgraph.microsoft.com%2FMail.Send&amp;state=8aeBu2xHkC5x8fLaVZMUS9keC6CQ3v&amp;access_type=offline
    Paste the authenticated url here:


1. To add this token, the analyst must add the token generated on the terminal screen and paste the token into a questao into a browser. This will allow the application to be allowed to read the user's email ⁇ .
1. If it is the first time accessing the application, it will be asked about what the app wants to do, and in our case, perform the reading of the mailbox.
1. If the analyst is repeating the process, nothing will be erased.
1. In both cases, a new url will be generated in the browser.
1. Collect the URL and paste the terminal.
1. If all happened well, the following message would appear in the terminal.

    Authentication Flow Completed. Oauth Access Token Stored. You can now use the API.


1. After this, the application is ready to perform the read-out of the selected account email ⁇  and ⁇  new events on Archer's platform.
1. With each new email ⁇  in the box, the ⁇  will print on the screen the email content and a log, with the number of the event opened on the Archer1 platform.

*1 It is important to remember that Microsoft access token only lasts for 60 minutes, however, the application has a refresh token, which has a duration of 90 days. Every time the 60-minute access token expires, the ⁇  ⁇  will create a new token for 90 days.
### 4 - Access token functionality
After the 90 days, a new access token must be generated, repeating the errors of the previous session.
