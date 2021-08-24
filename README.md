# Watching storage
It is a service for the employees of the bank 'Shine'.

If you don't work for this company, you are not able to use this service.
But you are able to read the code of service.

If you are from 'Shine', you can connect to the database ang get information 
about colleagues who visited the storage.

### How to install

Python3 should be already installed.

1) clone the repo
2) use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
    ```
    pip install -r requirements.txt
    ```
3) add .env file in the directory of the service:
    ```
    SECRET_KEY=<your secret key for the database>
    DEBUG=<True> if you want to enable DEBUG
    DEBUG=<False> if you want to disable DEBUG

    ```
### How to use
1) Write: 
    ```
    python3 manage.py runserver 
    ```
2) Use the service in your browser 

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).