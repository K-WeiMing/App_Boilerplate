# App_Boilerplate
Boilerplate code for application development using - Flask, React, Postgres

Frontend is created using React, using TypeScript and initialized using Vite

## Flask (Backend)

Sample routes are written in `app.py`

Port: 5000 (Default)

## React / TypeScript / Vite (FrontEnd)

React is used to create the frontend with Nginx used as the webserver

Npm packages:

Path (TypeScript): `npm install --save-dev @types/node`
Google Analytics: `npm i react-ga4`


## Running on Local (Development)

- Frontend

`npm run dev -- --host` or `npm run dev`

to preview production: `npm run build` followed by `npm run preview`

- Backend

`flask run --dev --port 5000 --debug`

- Postgres DB

`docker build -f db.dockerfile -t <name_of_your_image> .`

`docker run -d --name <container_name> -e POSTGRES_DB=db_name -e POSTGRES_USER=<username> -e POSTGRES_PASSWORD=<password> -p 5432:5432 <name of your image>`

- PgAdmin

PgAdmin is used to view your Database and to manually run SQL queries

`docker pull dpage/pgadmin4`

`docker run --name pgadmin-container -p 5050:80 -e PGADMIN_DEFAULT_EMAIL=username@domain.com -e PGADMIN_DEFAULT_PASSWORD=password -d dpage/pgadmin4`

Connecting to DB from PgAdmin, IP Address / Host is the local IP address of your computer on the network

- MacOS, go to Wi-Fi Settings to get IP of your local host
- Windows: `ipconfig/all`
