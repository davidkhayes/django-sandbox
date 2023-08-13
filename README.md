simple thing to learn the django q2 library.

to run, first clone this repository. then:

```console
cd /where/this/application/lives
python -m venv virtualenv
virtualenv\Scripts\activate.bat   # windows
source virtualenv/bin/activate    # macos/linux
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

open a second console/terminal, and
```console
cd /where/this/application/lives
virtualenv\Scripts\activate.bat   # windows
source virtualenv/bin/activate    # macos/linux
python manage.py qcluster
```

running application lives at http://127.0.0.1:8000


