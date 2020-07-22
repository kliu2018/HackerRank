SELECT IF(Grades.Grade >8, Students.Name, NULL), Grades.Grade, Students.Marks
FROM Students
Inner Join Grades
ON Students.Marks >Grades.Min_Mark AND Students.Marks < Grades.Max_Mark 
ORDER BY CASE Grades.Grade
             WHEN  >8 THEN Grades.Grade END DESC, 
             WHEN  >8 THEN Students.Name END,
             WHEN <8 THEN Students.Marks END ASC, 
             WHEN <8 THEN Students.Name END
