Getting Started
---------------

Prerequisites
~~~~~~~~~~~~~

You will need to have the following installed:

- Python 3.1+ - https://python.org
- Git - https://git-scm.com/


~~~~~~~~~~~~~

**Step - 1. Download The Project.**
~~~~~~~~~~~~~

   .. code:: sh

        git clone https://github.com/otuozeAhmed/hdvapp.git
***

**Step - 2.**
~~~~~~~~~~~~~

   .. code:: sh

       cd hdvapp

***

**Step 3.**
~~~~~~~~~~~~~

   .. code:: sh

       python -m venv venv
***
 
**Step 4a - Activate Virtual Environment - (Git Bash Terminal)**
~~~~~~~~~~~~~
   .. code:: sh

       source venv/Scripts/activate
***

**Step 4b - Activate Virtual Environment - (Command Prompt).**
~~~~~~~~~~~~~

   .. code:: sh

       .\venv\Scripts\activate
***


**Step 5 - Install The Requirements**
~~~~~~~~~~~~~
   .. code:: sh

       pip install -r requirements.txt
***

**Step 6a - Setup Migrations.**
~~~~~~~~~~~~~

   .. code:: sh

       Python manage.py makemigrations
***

**Step 6b - Migrate Data Model.**
~~~~~~~~~~~~~

   .. code:: sh

       python manage.py migrate

***

**Step 7 - Run Development Server.**
~~~~~~~~~~~~~

   .. code:: sh

       python manage.py runserver
***

