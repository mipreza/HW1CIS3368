select * from contacts;

create table contacts(
id INT(4) unsigned auto_increment primary key,
contactDetails varchar(30) NOT NULL,
creationDate date);

insert into contacts(contactDetails, creationDate) values 
('John', str_to_date('19-10-2009', '%d-%m-%Y')), 
('Michelle', str_to_date('03-12-2019', '%d-%m-%Y')),
('Eli', str_to_date('24-03-2020', '%d-%m-%Y')),
('Francisco', str_to_date('08-08-2011', '%d-%m-%Y')),
('Raul', str_to_date('14-12-2017', '%d-%m-%Y')),
('Emily', str_to_date('16-09-2006', '%d-%m-%Y')),
('Mary', str_to_date('13-07-2016', '%d-%m-%Y')),
('Daisy', str_to_date('26-01-2021', '%d-%m-%Y')),
('Alice', str_to_date('07-02-2013', '%d-%m-%Y')),
('Robert', str_to_date('11-01-2018', '%d-%m-%Y')),
('Alex', str_to_date('22-12-2019', '%d-%m-%Y')),
('Morgan', str_to_date('07-06-2020', '%d-%m-%Y')),
('Cody', str_to_date('14-08-2021', '%d-%m-%Y')),
('Steven', str_to_date('28-05-2020', '%d-%m-%Y')),
('Kim', str_to_date('17-05-2015', '%d-%m-%Y'));