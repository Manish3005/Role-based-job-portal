CREATE DATABASE IF NOT EXISTS resume_db;
USE resume_db;
CREATE TABLE IF NOT EXISTS user(id int, name1 varchar(30), passwd varchar(30));
CREATE TABLE IF NOT EXISTS signin(name1 varchar(30), age int, qual varchar(30),  passwd varchar(30))