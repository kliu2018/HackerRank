SELECT [Doctor], [Professor], [Singer], [Actor]
FROM (SELECT *,
      ROW_NUMBER() OVER (PARTITION BY Occupation ORDER BY (Name)) RN
      FROM OCCUPATIONS) AS SourceTable  

PIVOT (Max(Name) FOR Occupation in ([Doctor], [Professor], [Singer], [Actor])) AS PivotTable
