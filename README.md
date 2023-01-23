<h1>A work-in-progress password manager</h1>

<p><strong>Be aware, this is not an open source project</strong></p>


# Installation

> Clone the repository
>> git clone https://github.com/Eadwulf/password-manager.git

> Create the virtual environtment and install dependencies
>> pipenv install

> Activate the virtual environment
>> pipenv shell

> Apply Migrations
>> python manage.py migrate

> Run the tests for "passwords" app
>> python manage.py test password

> Run the tests for "websites" app
>> python manage.py test websites

> If the tests ran without problems, proceed testing the project:
>> python manage.py runserver