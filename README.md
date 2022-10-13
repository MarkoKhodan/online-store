![Logo of the project](https://www.stylefactoryproductions.com/wp-content/uploads/2022/04/how-to-make-an-online-store.png)

# Online Store

Simple Online store website implementation

### You can check functionality with testing user:

* login: admin
* password: admin

## Installation 

```shell
git clone git@github.com:MarkoKhodan/online-store.git
cd online-store
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

python manage.py runmigtarions
python manage.py loaddata initial_data.json
python manage.py loaddata employee.json
python manage.py loaddata item.json
python manage.py loaddata sale.json
python manage.py loaddata price_changes.json
python manage.py runserver
```

Windows:
```shell
git clone git@github.com:MarkoKhodan/online-store.git
cd online-store.git
python3 -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
python manage.py runmigtarions
python manage.py loaddata initial_data.json
python manage.py loaddata employee.json
python manage.py loaddata item.json
python manage.py loaddata sale.json
python manage.py loaddata price_changes.json
python manage.py runserver
 
```
## Features

* Authentication functionality
* Price changing monitoring
* Powerful admin panel for advance managing