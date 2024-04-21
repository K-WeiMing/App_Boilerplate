FROM postgres:16.2

ENV POSTGRES_PASSWORD <include password here>
ENV POSTGRES_DB <include DB name here>

WORKDIR /db_app

COPY ./database/init_db/init_db.sql /docker-entrypoint-initdb.d/

# Copy csv files to initialize DB
RUN mkdir /data

COPY ./database/init_csv/ .

EXPOSE 5432