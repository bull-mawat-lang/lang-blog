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

If you have outdated libraries, use `pip-upgrade` to upgrade your `requirements.txt` file
You must install `pip-upgrade` to be able to use it. Go-to this link for more [https://github.com/simion/pip-upgrader](https://github.com/simion/pip-upgrader)

## Create Database
* Start python script using
  * On Linux or Mac `python3`
  * On Windows `py`
* Import db and create_app `from blog import db, create_app`
* Create database and all tables `db.create_all(app=create_app())`

>Code is shown below

```python
from blog import db, create_app
db.create_all(app=create_app())
```

## Run the App from Terminal or CMD

### Linux or Mac
`python3 run.py`

### Windows
`py run.py`


>If you face any issues, it is probably because you need to configure secret key and database uri in the environment variables

## Quick fix is to hard-code them in the `config.py` file

### Change these lines
`SECRET_KEY = os.environ.get('SECRET_KEY')`

`SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')`

### To something like
`SECRET_KEY = "somerandomsecrets"`

`SQLALCHEMY_DATABASE_URI = "sqlite:///yourdatabasename.db"`

## Or just set them on environment variables

### Generating SECRET_KEY
>on Terminal

`python`

`import secrets`

`secrets.token_hex(32)`


> Copy the terminal output and paste it to your `SECRET_KEY` field


### Screenshots

` ##### Landing page `

![](https://github.com/bull-mawat-lang/lang-blog/blob/master/blog/static/app%20screenshots/home-1.png)


` ##### Login page `

![](https://github.com/bull-mawat-lang/lang-blog/blob/master/blog/static/app%20screenshots/login-1.png)


` ##### Logged in page `

![](https://github.com/bull-mawat-lang/lang-blog/blob/master/blog/static/app%20screenshots/Home-2.png)

` ##### Create  new post page `

![](https://github.com/bull-mawat-lang/lang-blog/blob/master/blog/static/app%20screenshots/post-1.png)

` ##### Current selected post page `

![](https://github.com/bull-mawat-lang/lang-blog/blob/master/blog/static/app%20screenshots/post-2-updatedelete.png)


` ##### Delete post page `

![](https://github.com/bull-mawat-lang/lang-blog/blob/master/blog/static/app%20screenshots/post-delete.png)


` ##### Update post page `

![](https://github.com/bull-mawat-lang/lang-blog/blob/master/blog/static/app%20screenshots/post-update.png)