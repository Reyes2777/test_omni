# README
This is a test to omnilatam, the app is built according to the requested requirements with framework Starlette.

#Requirements
  - Python 3.9
  - Docker 20.10.7
#Installation
* Clone repo: 
  > git clone git@github.com:Reyes2777/test_omni.git

* Create enviroment with virtualenv(optional)

* Create .env file with the following variables:
  ~~~
    DEFAULT_DB_NAME=postgrest
    DEFAULT_DB_HOST=db
    DEFAULT_DB_HOST_PORT=5432
    DEFAULT_DB_USER=postgrest
    DEFAULT_DB_PASSWORD=postgrest
  
#Run Application

* Execute:
  >  docker-compose up

#Testing
Run all tests with pytest -s -vvvv. For more uses of pytest, check this <https://docs.pytest.org/en/latest/usage.html>_.
