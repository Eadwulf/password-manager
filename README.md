<h1>A work-in-progress password manager</h1>

<p><strong>Be aware, this is not an open source project</strong></p> <br>

## Installation <br>

### Clone the repository
> git clone https://github.com/Eadwulf/password-manager.git <br>

### Create the virtual environtment and install dependencies
> pipenv install <br>

### Activate the virtual environment
> pipenv shell <br>

### Apply Migrations
> python manage.py migrate <br>

### Run the tests for "passwords" app
> python manage.py test password <br>

### Run the tests for "websites" app
> python manage.py test websites <br>

### If the tests ran without problems, proceed testing the project:
> python manage.py runserver <br>