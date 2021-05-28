# To-dos
## Create and activate the virtual environment

### step 1 - Create Project Dir and Move to it
Open terminal or CLI and create or move to your project working directory

### step 2 - Create Virtual Environment
*For Linux or Mac* > python3 -m venv <name-of-your-virtual-environment>
*For Windows* > py -m venv <name-of-your-virtual-environment>

### Step 3 - Activate Virtual Environment

*For Linux or Mac* > source <name-of-your-virtual-environment>"/bin/activate
*For Windows* > .\<name-of-your-virtual-environment>\Scripts\activate

[Go-to](https://docs.python.org/3/library/venv.html) for more on virtual environment

## Clone the repo
Use [ssh](git@github.com:bull-mawat-lang/lang-blog.git) OR
Use [https](https https://github.com/bull-mawat-lang/lang-blog.git)

## Install Requirements
Type > pip install -r requirements.txt

## Create Database
* *start python3 script*
* *Import db, create_app*
* *And run db.create_all(app=create_app())*

```python
from blog import db, create_app
db.create_all(app=create_app())
```
