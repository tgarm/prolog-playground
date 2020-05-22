# Prolog Playground
A web based Prolog Playground for study (using Tau-Prolog)

## About

To provide an easy way to try Prolog code. 
* Instant edit Prolog code via Web Browser
* Save valid Prolog code to database, and can load later.

tau-prolog is used, including the CodeMirror mode "cm-prolog.js".

## TODO

* Add certain DOM object for Prolog code to operate.
* Button to delete program in database

## Static web usage:

Please try: https://tgarm.github.io/prolog-playground

## Web with database

Prerequests:
* Python3.6+
* Redis
* PM2 (optional)

Install required Python modules:

    pip3 install redis uvicorn fastapi pydantic

Start server(with PM2):
    cd api
    ./start-server.sh
