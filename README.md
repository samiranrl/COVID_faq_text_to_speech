# Corona FAQ

This is the source code behind https://www.virusbhagao.com/.

The web app reads aloud basic coronavirus information in Indian languages. The goal is to convey the basics of coronavirus to most regional language users in small cities/villages of India. Literacy is not a barrier, the app uses a text to speech interface to read the content aloud.

There is an abundance of misinformation and superstition regarding coronavirus, and surprisingly few sources which give out verified facts. Our only source of information is a subset of: https://www.who.int/news-room/q-a-detail/q-a-coronaviruses, which we translate to Indian languages.

Please help us spread the word, especially to people who need this.

# Contributors

- **Sanjay Kumar Rai**
- **Sweda Nair**
- **Sanjay Tippanavar**
- **Jash Dave**
- **Shibsankar Das**
- **Umashankar Nagarajan**
- **Soumen Khatua**
- **Lalitha Krishnamurthy**
- **Vidhya Krishnamurthy**
- **Kiran Sukhavasi**


# Stack
Django, sqlite3, gtts, googletrans, spectre css


# Instructions to run

- pip3 install Django==2.2.10
- pip3 install pandas
- pip3 install gtts
- pip3 install googletrans
- python3 manage.py makemigrations
- python3 manage.py migrate
- python3 bootstrap.py (this takes some time for automatic translation and text to speech)
- python3 manage.py runserver

- open http://localhost:8000/
