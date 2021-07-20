\set db_name `echo "$DB_NAME"_test`
\set db_user `echo $DB_USER`
DROP DATABASE IF EXISTS :db_name;
CREATE DATABASE :db_name WITH OWNER :db_user;