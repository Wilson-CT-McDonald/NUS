DROP TABLE IF EXISTS employee;

CREATE TABLE employee (
    employee_id INT AUTO_INCREMENT PRIMARY KEY,
    emp_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone_number VARCHAR(15),
    department VARCHAR(50),
    salary DECIMAL(10, 2)
);

INSERT INTO employee (emp_name, email, phone_number, department, salary) VALUES
('Alice Johnson', 'alice.johnson@example.com', '9876543210', 'HR', 55000.00),
('Bob Smith', 'bob.smith@example.com', '9876543211', 'Engineering', 75000.00),
('Carol Lee', 'carol.lee@example.com', '9876543212', 'Marketing', 60000.00),
('David Brown', 'david.brown@example.com', '9876543213', 'Engineering', 80000.00),
('Eve Davis', 'eve.davis@example.com', '9876543214', 'Sales', 58000.00),
('Frank Miller', 'frank.miller@example.com', '9876543215', 'Finance', 62000.00),
('Grace Wilson', 'grace.wilson@example.com', '9876543216', 'HR', 54000.00),
('Hank Adams', 'hank.adams@example.com', '9876543217', 'Engineering', 77000.00),
('Ivy Clark', 'ivy.clark@example.com', '9876543218', 'Marketing', 61000.00),
('Jack Turner', 'jack.turner@example.com', '9876543219', 'Sales', 59000.00);

SELECT * FROM employee;