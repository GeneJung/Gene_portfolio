CREATE VIEW DeathRateView AS
select iso_code,location, cast((total_deaths*1.0/cast(total_cases as decimal(10,2)))*100 as decimal(5,2)) as deathrate_percentage from Covid

select * from DeathRateView 