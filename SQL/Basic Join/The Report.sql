SELECT IF(Grades.Grade >7, Students.Name, NULL), Grades.Grade, Students.Marks
FROM Students
Join Grades
ON Students.Marks BETWEEN Grades.Min_Mark AND Grades.Max_Mark 
ORDER BY -Grades.Grade, Students.Name, Students.Marks
