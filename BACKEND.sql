create database alumniDB;
use alumniDB;
CREATE TABLE Department(
department_id INT PRIMARY KEY AUTO_INCREMENT,
department_name VARCHAR(50) UNIQUE NOT NULL
);
CREATE TABLE Alumni(
alumni_id INT PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(100) NOT NULL,
email VARCHAR(100) UNIQUE NOT NULL,
phone VARCHAR(15) UNIQUE,
passing_year INT,
department_id INT,
job_title VARCHAR(100),
company VARCHAR(100),

FOREIGN KEY(department_id)
REFERENCES Department(department_id)
);
CREATE TABLE Events(
event_id INT PRIMARY KEY AUTO_INCREMENT,
event_name VARCHAR(100),
event_date DATE,
location VARCHAR(100)
);
CREATE TABLE Participation(
participation_id INT PRIMARY KEY AUTO_INCREMENT,
alumni_id INT,
event_id INT,
role VARCHAR(50),

FOREIGN KEY(alumni_id)
REFERENCES Alumni(alumni_id),

FOREIGN KEY(event_id)
REFERENCES Events(event_id)
);
INSERT INTO Department(department_name)
VALUES
('Computer Science'),
('Information Technology'),
('Mechanical'),
('Civil');

INSERT INTO Alumni
(name,email,phone,passing_year,department_id,job_title,company)

VALUES
('Rahul Patil','rahul@gmail.com','9876543210',2020,1,'Software Engineer','TCS'),
('Sneha Kulkarni','sneha@gmail.com','9876543211',2019,2,'Analyst','Infosys'),
('Amit Sharma','amit@gmail.com','9876543212',2018,1,'Developer','Wipro'),
('Priya Singh','priya@gmail.com','9876543213',2021,3,'Designer','L&T');

INSERT INTO Events(event_name,event_date,location)

VALUES
('Alumni Meet','2025-03-10','College Hall'),
('Tech Seminar','2025-05-15','Auditorium');

INSERT INTO Participation(alumni_id,event_id,role)

VALUES
(1,1,'Speaker'),
(2,1,'Guest'),
(3,2,'Organizer'),
(4,2,'Participant');

select * from alumni;

SELECT name, passing_year
FROM Alumni
WHERE passing_year > 2019;

SELECT
A.name,
A.company,
D.department_name
FROM Alumni A
JOIN Department D
ON A.department_id = D.department_id;

SELECT
department_id,
COUNT(*) AS total_alumni
FROM Alumni
GROUP BY department_id;

SELECT
department_id,
COUNT(*) AS alumni_count
FROM Alumni
GROUP BY department_id
HAVING COUNT(*) > 1;

SELECT name
FROM Alumni
WHERE department_id =
(
SELECT department_id
FROM Alumni
WHERE name='Rahul Patil'
);
CREATE VIEW Alumni_Details AS
SELECT
A.alumni_id,
A.name,
A.email,
A.company,
D.department_name
FROM Alumni A
JOIN Department D
ON A.department_id = D.department_id;

SELECT * FROM Alumni_Details;



