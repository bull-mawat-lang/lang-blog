# To-dos

## Create Project Dir and Move to it
Open terminal or CLI and create or move to your project working directory

## Create and Activate the Virtual Environment

### Step 1 - Create Virtual Environment
*On Linux or Mac* `python3 -m venv <name-of-your-virtual-environment>`

*On Windows* `py -m venv <name-of-your-virtual-environment>`

### Step 2 - Activate Virtual Environment

*On Linux or Mac* `source <name-of-your-virtual-environment>/bin/activate`

*On Windows* `.\<name-of-your-virtual-environment>\Scripts\activate`

Go-to [https://docs.python.org/3/library/venv.html](https://docs.python.org/3/library/venv.html) for more on virtual environment

## Clone the Repo

## Install Requirements
Type `pip install -r requirements.txt`

## Create Database
* *Start python script using
  * On Linux or Mac `python3`
  * On Windows `py`
* *Import db and create_app `from blog import db, create_app`*
* *Create database and all tables `db.create_all(app=create_app())`*

* >Code is shown below

```python
from blog import db, create_app
db.create_all(app=create_app())
```

## Run the App from Terminal or CMD

### Linux or Mac
`python3 run.py`

### Windows
`py run.py`
