SELECT A.name as Employee 
FROM Employee A, Employee B
Where A.managerId = B.id and A.salary > B.salary