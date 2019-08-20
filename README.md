[![CircleCI](https://circleci.com/gh/teamsempo/SempoBlockchain.svg?style=svg&circle-token=6b52b66ec99befc82f2182eddc0e117f7bba9005)](https://circleci.com/gh/teamsempo/SempoBlockchain)

# Sempo

Sempo Admin Dashboard, SMS/WhatsApp API and crypto payments infrastructure

Includes:
- Generic spreadsheet upload
- SMS API via Twilio
- ERC20 (Dai) token mirroring
- Vendor android app API

## To run locally machine:

### Install Front-End Requirements
```
cd app
```
```
npm install
```

### Run the web app in a Virtual Env
```
run.py
```

```
npm run dev
```

### To use SMS API
- Go to root dir
```
cd ..
```
- Run ngrok
```
./ngrok http 9000
```

- Login to Twilio:
https://www.twilio.com/login

- Navigate to the phone number section of Twilio and find the below number
```
+61 428 639 172
```
- Click to edit, scroll to `Messaging` and find `A MESSAGE COMES IN` box
- Add your ngrok server (e.g. `https://a833f3af.ngrok.io/api/sms/`) and save

### Blockchain
In terminal run:
```
redis-server
```

Start celery:
```
celery -A worker worker --loglevel=INFO --concurrency=500 --pool=eventlet
```

### Database Migration: Alembic

First, setup your database `sempo_blockchain_local`, using the username and password from the local config file.

Next, to update your database to the latest migration file:

```
python manage.py db upgrade
```

To create a migrations file (remember to commit the file!):

```
python manage.py db migrate
```

Sometimes, branches split and you will have multiple heads:

```
python manage.py db merge heads
```

For more commands, see Alembic documentation: https://alembic.sqlalchemy.org/en/latest/

### Vendor App
- Pull the below repo and follow steps
https://github.com/enjeyw/SempoVendorMobile

(if you have installed the prod vendor app, ensure you clear data and uninstall before installing from dev)

## To setup a production deployment
Follow this guide
https://docs.google.com/document/d/1PLJgCwRvHDdb_goWl0fMy8eFBfNUk2F3GzLHIiPzV0A/edit
