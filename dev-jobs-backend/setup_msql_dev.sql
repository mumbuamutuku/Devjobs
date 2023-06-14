-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS devjobs_db;
CREATE USER IF NOT EXISTS 'devadmin'@'localhost' IDENTIFIED BY 'dev_pwd';
GRANT ALL PRIVILEGES ON `devjobs_db`.* TO 'devadmin'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'devadmin'@'localhost';
FLUSH PRIVILEGES;   






