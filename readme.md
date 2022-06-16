
# Flask website
## Structure description

- CVproject<br>
  Folder which stores project

  - main.py<br>
    Main __exectuable file__ - webserver app

  - website<br>
    Folder which stores
    - \_\_init\_\_.py <br>
      makes website directory a __python package__<br>
      when __website__ is imported, everything in this folder will run automatically

    - auth.py<br>
      stores __authentication routes__ and their logic

    - models.py<br>
      __database models__ are created here

    - views.py<br>
      stores __routes__ which can be accessed in navigation menu or bar __except authentication__
  - template<br>
    In flask you can render html files - they are called templates and use special template language(JINJA) which substitutes javascript to some extent
    - home.html
    - register.html
    - signin.html


  - static<br>
    stores images or javascript, which do not require internet to run

## Linux Packages (Ubuntu)

```sh
sudo apt install python3, python3-pip
sudo apt install mysql-server
```

## Modules

```sh
pip install flask
pip install flask-login
pip install flask-sqlalchemy
pip install mysql-connector-python
pip install pymysql
pip install cryptography
pip install geocoder
```

## Goodies
- Flask basics<br>
https://www.youtube.com/watch?v=dam0GPOAvVI

- MYSQL USAGE ON LINUX:<br>
https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-20-04

- FANCY ICONS:<br>
  https://feathericons.com/<br>
  https://icons.getbootstrap.com/

- CSS Overlay:<br>
  https://www.youtube.com/watch?v=exb2ab72Xhs

- Weather api
  https://openweathermap.org/api
