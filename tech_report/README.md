# Tech Report

Location Data:

- The location CSV data comprises approximately 3,200 data points representing various cities and counties.
  While this data isn’t directly used for analysis, it aids in understanding the findings.
  It’s important to note that this data isn’t fixed; additional data can be sourced online.

Piping Plover Data:

- The piping plover dataset contains thousands of rows.
  Each row corresponds to a sighting of a piping plover by a bird observer.
  Notably, each row refers to a specific bird and includes an “observation count”, making these bird sightings somewhat “weighted”.

Temperature Data:

- The temperature dataset also contains thousands of entries.
  These entries represent temperatures for specific years.
  However, there’s a limitation: much of this data may be outdated since the years covered are not very recent.
  To compensate, we can retrieve historical temperature data for a specific city using the Visual Crossing website here.

Reasonable Data:

The amount of data available for analysis is ample, especially considering that factors such as location and temperature do not necessarily require a fixed amount of data, given that these variables can often be sourced online. However, it's crucial to highlight that the key focus lies in the observation and sighting records of the piping plover, as these serve as the dependent variables for conducting any meaningful analysis. While location and temperature data provide contextual background, it is the monitoring and documentation of the piping plover's presence and behavior that form the core of our study. Therefore, while we have a sufficient quantity of data overall, it is essential to prioritize the accuracy and completeness of our piping plover observations to ensure the robustness and reliability of our analysis.

Identifying Attributes:

The identity attributes all possess distinct entries assigned to them, ensuring a comprehensive dataset. For temperature, data points are associated with named cities and counties, providing a diverse range of environmental conditions for analysis. Similarly, the piping plover observations are meticulously cataloged, each tagged with unique identifiers such as observation ID and piping plover ID, facilitating precise tracking and analysis of individual birds and their behaviors over time. Additionally, location data is structured around named cities and counties, offering granularity in spatial information for correlational insights. This meticulous organization ensures that each aspect of the dataset is appropriately delineated, allowing for thorough investigation and interpretation of the relationships between temperature, location, and piping plover observations.

Data Collection:

The piping plover data stems from the reputable source of eBird, managed by the Cornell Lab of Ornithology. Leveraging eBird's extensive database not only ensures the credibility and reliability of the observations but also provides access to a vast network of citizen scientists and researchers contributing to the collection of bird sighting data. The collaboration with eBird underscores the scientific rigor and collaborative spirit behind our analysis, as we draw upon a wealth of meticulously recorded observations to deepen our understanding of piping plover behavior and habitat preferences.
