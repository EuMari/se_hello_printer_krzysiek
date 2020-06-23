.. image:: https://travis-ci.com/kbalko/se_hello_printer_app.svg?branch=master
    :target: https://travis-ci.com/kbalko/se_hello_printer_app

.. image:: https://coveralls.io/repos/github/kbalko/se_hello_printer_app/badge.svg
    :target: https://coveralls.io/github/kbalko/se_hello_printer_app

.. image:: https://app.statuscake.com/button/index.php?Track=mjo6Vaaxoz&Days=1&Design=1
    :target: https://www.statuscake.com



Simple Flask App
================

Informacje ogólne
-----------------

Prosta aplikacja wyświetlająca imię i wiadomość w różnych formatach (podstrona '/formaty') z zajęć o Continuous Integration, Continuous Delivery i Continuous Deployment.:heavy_check_mark:

Na potrzeby zaliczenia projektu rozbudowana do formy mikrobloga na podstawie 'The Flask Mega-Tutorial' (miguelgrinberg.com). 
Aplikacja pozwala na rejestrację, zalogowanie, dodanie treści, przeglądanie treści innych użytkowników, zaobserwowanie innych użytkowników, zresetowanie hasła via e-mail. 
W razie awarii administrator dostaje informację na adres e-mail wraz z logami błędu.

Aplikacja jest zintegrowana z:

- `TravisCI <https://travis-ci.com/github/kbalko/se_hello_printer_app>`_

- Docker

- Jenkins

- Heroku

- `Statuscake <https://www.statuscake.com>`_

- `coveralls.io <https://coveralls.io/github/kbalko/se_hello_printer_app>`_

Linter tool:

- Flake8

Główne technologie
------------------
- Python 2.7
- Flask 1.1.2
- SQLAlchemy 2.4.3
- Bootstrap 3

Wszystkie zależności dostępne w pliku requirements.txt i test_requirements.txt

Uruchomienie
------------

- Rozpoczynając pracę z projektem wykorzystujemy virtualenv. Hermetyczne środowisko dla pojedyńczej aplikacji w pythonie:

  ::

    # ubuntu, add to ~/.bashrc
    $ source /usr/local/bin/virtualenvwrapper.sh

    # tworzymy hermetyczne środowisko dla bibliotek aplikacji:
    $ mkvirtualenv wsb-simple-flask-app
    $ pip install -r requirements.txt
    $ pip install -r test_requirements.txt

  lub wykorzystując target z Makefile:

  ::

    # instalacja dependencies
    $ make deps

  Sprawdź: `documentację virtualenvwrappera <https://virtualenvwrapper.readthedocs.io/en/latest/command_ref.html>`_ oraz `biblioteki flask <http://flask.pocoo.org>`_.

- Uruchamianie applikacji:

  ::

    # jako zwykły program
    $ python main.py

    # albo:
    $ PYTHONPATH=. FLASK_APP=hello_world flask run

- Uruchamianie testów (see: http://doc.pytest.org/en/latest/capture.html):

  ::

    $ PYTHONPATH=. py.test
    $ PYTHONPATH=. py.test  --verbose -s

  lub za pośrednictwem pliku Makefile zgodnie z zasadą:
  ::

    target: dependencies
      system command(s)

  na przykład:
  ::

    test:
      PYTHONPATH=. py.test --verbose -s

  ::

    # uruchomienie testu
    $ make test

- Kontynuując pracę z projektem aktywujemy hermetyczne środowisko dla aplikacji py:

  ::

    $ source /usr/local/bin/virtualenvwrapper.sh # nie trzeba, jeśli już w .bashrc
    $ workon wsb-simple-flask-app

    ...

    # deaktywacja virtualenv
    $ deactivate


Pomocnicze
==========

Ubuntu
------

- Instalacja python virtualenv i virtualenvwrapper:

  ::

    $ sudo pip install virtualenv
    $ sudo pip install virtualenvwrapper

- Instalacja dockera: `dockerce howto <https://docs.docker.com/install/linux/docker-ce/ubuntu/>`_

SQLAlchemy
----------
- Instalacja odbywa się automatycznie w ramach tergetu 'make deps' w Makefile. 
  Instalacja manualna:

  ::
  
   $ pip install flask-sqlalchemy
   
   # database migrations
   $ pip install flask-migrate

- Kilka pomocnych podstawowych komend do obsługi bazy danych:

  ::
  
    # inicjalizacja
    $ flask db init 
    
    # skrypt migracji
    $ flask db migrate -m"comment"
    
    # zapis zmian
    $ flask upgrade

`Dokumentacja SQLAlchemy <https://flask-sqlalchemy.palletsprojects.com/en/2.x/>`_

