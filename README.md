# To-dos

## Create Project Dir and Move to it
Open terminal or CLI and create or move to your project working directory

## Create and activate the virtual environment

### Step 1 - Create Virtual Environment
*For Linux or Mac* - `python3 -m venv **name-of-your-virtual-environment**`

*For Windows* - `py -m venv **name-of-your-virtual-environment*`

### Step 2 - Activate Virtual Environment

*For Linux or Mac* - `source **name-of-your-virtual-environment**/bin/activate`

*For Windows* - `.\**name-of-your-virtual-environment**\Scripts\activate`

Go-to [https://docs.python.org/3/library/venv.html](https://docs.python.org/3/library/venv.html) for more on virtual environment

## Clone the repo

## Install Requirements
Type - `pip install -r requirements.txt`

## Create Database
* *Start python script using `python3` for Linux/Mac or `py` for Windows*
* *Import using `from blog import db, create_app`*
* *And run `db.create_all(app=create_app())`*

```python
from blog import db, create_app
db.create_all(app=create_app())
```

##Run the app from Terminal or CMD

###Linux or Mac
`python3 run.py`

###Windows
`py run.py`
