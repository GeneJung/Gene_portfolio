CREATE VIEW aboveAvg AS
SELECT * 
FROM VaccRate
WHERE VaccinationRate > (
	SELECT AVG(VaccinationRate)
	FROM VaccRate);

CREATE VIEW belowAvg AS
SELECT * 
FROM VaccRate
WHERE VaccinationRate < (
	SELECT AVG(VaccinationRate)
	FROM VaccRate);
	
CREATE VIEW belowAvg2 AS	
select * from covid2 where location in (select location from belowAvg) and STRFTIME('%m', "date")  > "09" and STRFTIME('%Y', "date") > "2020"
CREATE VIEW aboveAvg2 AS
select * from covid2 where location in (select location from aboveAvg) and STRFTIME('%m', "date")  > "09" and STRFTIME('%Y', "date") > "2020"




UPDATE covid2
SET "Date" =
substr("date", 6, 4) || '-' ||
       substr("date", 1, 2) || '-' || '0' ||
       substr("date", 4, 1) WHERE "date" LIKE '__/_/____'
UPDATE covid2
SET "Date" =
 substr("date", 6, 4) || '-0' ||
 substr("date", 1, 1) || '-' ||
 substr("date", 3 , 2)
 WHERE "date" LIKE '_/__/____'
 
UPDATE covid2
SET "Date" = substr("date", 5, 4) || '-0' ||
 substr("date", 1, 1) || '-0' ||
 substr("date", 3 , 1) 
 WHERE "date" LIKE '_/_/____'

UPDATE covid2
SET "Date" = substr("date", 7, 4) || '-' ||
 substr("date", 1, 2) || '-' ||
 substr("date", 4 , 2)
 WHERE "date" LIKE '__/__/____'
 
CREATE VIEW Question2AboveAvg AS	 
select *
From aboveAvg2 as A
Join "SimpleHospRate" as B
using("date", "location")

drop view question2aboveavg

create view Question2AboveAvg_2 As
select distinct * 
from question2Aboveavg
join
"vaccrate"
using("location")

drop view Question2AboveAvg_2

CREATE VIEW Question2BelowAvg AS	 
select *
From belowAvg2 as A
Join "SimpleHospRate" as B
using("date", "location")

create view Question2BelowAvg_2 As
select distinct * 
from question2Belowavg
join
"vaccrate"
using("location")

drop view Question2BelowAvg

select distinct * from question2Belowavg_2

select distinct * from question2Aboveavg_2

select * from Question2BelowAvg where location = "germany"

