### Data Spec

The database comprises three key components: piping plover, temperature, and location. The overarching objective is to employ a multidisciplinary approach to analyze and map piping plover migration and observation patterns across different locations. This analysis takes into account both global temperature and local temperature factors.
Here are the key details about each component:

Piping Plover:

- Provides the number of observed piping plovers, along with their corresponding IDs, longitude, and latitude.
- The piping plover entries include various details, such as the global unique identifier, common and scientific names, breeding codes, behavior codes, and more.
- Similar to the location data, where counties are also mapped using longitude and latitude coordinates.
- Data format: CSV with SQL queries for cleaner and more readable information.

Temperature:

- Recorded in both Fahrenheit and Celsius.
- Associated with named counties.
- Additional data may suggest an API for further temperature analysis.
- No default values; each entry is unique.
- Temperature values range from 50 to 70 (Fahrenheit) and 15 to 20 (Celsius).

Location:

- Expressed in decimal degrees.
- Latitude ranges from -90 to 90, and longitude ranges from -180 to 180.

Uniqueness and Distribution:

- Each of the three components—piping plover, temperature, and location—is unique and exhibits a reasonable distribution.
- However, it’s important to acknowledge that the observed number of piping plovers may be less certain in certain regions due to the inherent nature of their migration patterns.

Data Values and Requirements:

- None of these components have mandatory values, but they all contribute to our data analysis.
- Entries for piping plovers with unknown locations will be excluded from our final findings and conclusions.

Final Analysis Approach:

- Our analysis can take the form of statistical analysis or general statements.
- Regardless of the method, our overarching goal is to uncover correlations and weave a compelling narrative among these data points.

Ethical Considerations:

- All of the data in the database was volunteered by bird observers or paid and wasn't unethically collected.

### Link

Full Piping Plover Data:
Full Temperature Data:
Full Location Data:

Sample of Piping Plover Data:
Sample of Temperature Data:
Sample of Location Data:
