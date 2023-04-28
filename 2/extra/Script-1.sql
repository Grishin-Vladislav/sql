create database company;

create table department (
	department_id serial primary key,
	title varchar(100)
);

create table employee (
	employee_id serial primary key,
	first_name varchar(20),
	last_name varchar(20),
	department_id integer 
		references department (department_id) on delete set null,
	supervisor_id integer
		references employee (employee_id) on delete set null
);

alter table employee 
	alter column supervisor_id set default null;
