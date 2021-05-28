#To-dos

##-> Clone the repo
Use ssh <git@github.com:bull-mawat-lang/lang-blog.git> OR
Use https <https https://github.com/bull-mawat-lang/lang-blog.git>

##-> Create and activate the virtual environment

###step 1 - Create Project Dir and Move to it
Open terminal or CLI and create or move to your project working directory

###step 2 - Create Virtual Environment
Type "python3 -m venv <name-of-your-virtual-environment>" For Linux or Mac
Type "py -m venv <name-of-your-virtual-environment>" For Windows

###Step 3
Activate Virtual Environment

Type "source <name-of-your-virtual-environment>"/bin/activate" For Linux or Mac
Type ".\<name-of-your-virtual-environment>\Scripts\activate" For Windows

Go-to[Go-to] (https://docs.python.org/3/library/venv.html) for more on virtual environment

##-> Install Requirements
Type "pip install -r requirements.txt"

##-> Create Database
* *start python3 script*
* *Import db, create_app*
* *And run db.create_all(app=create_app())*

'''python
from blog import db, create_app
db.create_all(app=create_app())
'''
