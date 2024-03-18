attach 'data/location.db' as location;
attach 'data/tempr.db' as tempr;
attach 'piping_plover_data/observations.db' as observations
Select b.Observation_Date as "Date", t.temp as "Year's Avg. Temp", l.fips_code as FIPS, b.Latitude, b.Longitude, b.Observation_Count as "Number of Piping Plover Observations"
From location.location_data  l
INNER JOIN 
tempr.temp_data t on l.fips_code = t.fips
INNER JOIN 
observations.Observations b on b.Observation_Count != 'X' and b.county_name=l.name and (b.Latitude BETWEEN l.lat - 0.5 and l.lat+0.5) and (b.Longitude BETWEEN l.lng-0.5 and l.lng+0.5) and (SUBSTRING(b.Observation_Date, 1, 4) = t.year)
ORDER BY b.Observation_Date