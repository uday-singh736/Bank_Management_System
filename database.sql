create database if not exists Bank;
USE Bank;
create table if not exists account (
 name varchar(20),
 ac_no int primary key,
 dob date
 add_ss varchar(34),
 open_amount INT 
);
create table if not exists balance (
 name varchar(20),
 ac_no int(100) primary key,
 balance INT
);
