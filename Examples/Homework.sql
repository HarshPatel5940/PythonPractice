-- ! This is HW for sql to be submitted for 22 JAN 2022

-- ? q1) Query to create table

CREATE TABLE Empl(
    emp_no INT PRIMARY KEY, 
    name VARCHAR(20) NOT NULL, 
    job VARCHAR(20) NOT NULL, 
    hired_date DATE NOT NULL, 
    salary INT NOT NULL, 
    department_name VARCHAR(20) NOT NULL, 
    department_number INT NOT NULL
);

-- ? q2) Display all columns from the table
SELECT * FROM Empl;

-- ? q3) emp_no and name
SELECT emp_no,name FROM Empl;

-- ? q4) SHOW name, salary and department - where 5000 must be added to salary for all emps
SELECT name, salary + 5000, department_name, department_number FROM Empl;

-- ? q5) Display name, emp_no, salary and annual salary (from any particular department)
SELECT name,emp_no,salary, salary*12 from Empl WHERE department_number=1;

-- ? q6) List all unique departments
SELECT DISTINCT department_name FROM Empl;

-- ? q7) Display the emp details whose salary is >= 35000
SELECT * FROM Empl WHERE salary>=35000;

-- ? q8) Display the emp whose name has 'A' as the third alphabet
SELECT Empl WHERE name LIKE '__A%';

-- ? q9) Display the emp whose name ends with 'T'
SELECT * FROM Empl WHERE name LIKE '%T';

-- ? q10) Display the emp whose name contains 'L'
SELECT * FROM Empl WHERE name CONTAINS 'L';


-- ! This Practice Done By sir in class

-- i. To display the details of those customers city is 'Delhi'
SELECT * FROM CUSTOMER WHERE CITY = "Delhi";

-- ii. To increase the price of all things 100 in the table ITEM
UPDATE ITEM SET PRICE = PRICE + 1000;

-- iii. To display the ITEMNAME, Max(PRICE).count(*) from ITEM
SELECT NAME, DEPT, BASIC FROM DOCTOR, SALARY WHERE DEPT="ENT" AND DOCTOR.ID = SALARY.ID;

-- iv. To display the ITEMNAME, PRICE * 100 from ITEM where MANUFACTURER = 'ABC'
SELECT ITEMNAME, PRICE * 100 FROM ITEM WHERE MANUFACTURER = "ABC";

-- v. To display the Distinct city from CUSTOMER
SELECT DISTINCT CITY FROM CUSTOMER;
