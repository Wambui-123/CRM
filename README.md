# CRM
## Author
[Yvonne Muthui](https://github.com/wambui-123)
## Description
A CRM(Customer relationship management) system created to confirm that business communication with consumers goes smoothly and efficiently in order to increase the overall profits. The application is to be used by a company to monitor their roles. Leads will be updated and Agents are given the role to the leads listed.
## User Story
* Sign in with the application to start using.
* Create a lead.
* View dashboard to see all leads.
* Add/Upload Agents.
* Assign roles/leads to agents.
* Edit Profile information
* Set catergory.

## [Demo](https://wambo-neighboorhood.herokuapp.com/) click to view

![Image](static/images/Screenshot%20from%202022-06-30%2013-49-36.png)
![Image](static/images/Screenshot%20from%202022-06-30%2013-49-10.png)
![Image](static/images/Screenshot%20from%202022-06-30%2013-51-30.png)

## Technologies Used
* Python
* Django
* SQLite3
* HTML5  
* CSS3
* Tailwind/Tailblocks
* Google Font API

## Requirements
* This program requires python3.+ (and pip) installed, a guide on how to install python on various platforms can be found [here](https://www.python.org/)
* Once python is installed, install the folowing external libraries provided in the requirements.txt file using pip
* Example: * **`pip install django==1.11.23`**
* This project requires you to have a secret key from Uploadcare to facilitate cloud storage of uploaded images.
    * The secret key can be gotten by creating a free uploadcare account, starting a new project and navigating to the dashboard
    * The key should be stored as an environmental variable in an .env file as shown below
        * **`SECRET=<your secret key here>`**
    * More info on how to use the Django pyuploadcare library can be found [here](https://uploadcare.com/docs/guides/django/)

## Installation and Set-up
To view the app, open the live site link provided below on the README.
Here is a run through of how to set up the application:
* **Step 1** : Clone this repository using **`git clone https://github.com/Wambui-123/NeighbourHood.git`**, or downloading a ZIP file of the code.
* **Step 2** : The repository, if downloaded as a .zip file will need to be extracted to your preferred location and opened
* **Step 3** : Go to the project root directory and install the virtualenv library using pip an afterwards create a virtual environment. Run the following commands respectively:
    * **`pip install virtualenv`**
    * **`virtualenv venv`**
    * **`source venv/bin/activate`**
        * Note that you can exit the virtual environment by running the command **`deactivate`**
* **Step 4** : Download the all dependencies in the requirements.txt using **`pip install -r requirements.txt`**
* **Step 5** : You can now launch the application locally by running the command **`python manage.py runserver`** and copying the link given on the termnal on your browser.
    * To post photos, run the command  **`python manage.py createsuperuser`** to create an admin account in order to post. Access to the admin panel is by adding the path /admin to the address bar.    

## Known Bugs
* None at the momment, report any by contacting me

## Support and contact details
If you find a bug on the website or its not working as expected, please feel free so send me an email @yvonnewambui28@gmail.com

## Licence
* MIT License
* Copyright (c) 2022 Yvonne Muthui



