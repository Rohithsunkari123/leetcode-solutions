# Write your MySQL query statement below
select name,bonus from Employee
left join bonus on Employee.empId=bonus.empId
where bonus is null or bonus < 1000
