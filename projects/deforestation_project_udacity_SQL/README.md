# ForestQuery into Global Deforestation, 1990 to 2016

This repository contains the ForestQuery project, which aims to combat deforestation around the world and raise awareness about its impact on the environment. The project analyzes data obtained from the World Bank, including forest area and total land area by country and year from 1990 to 2016, as well as a table of countries and their respective regions.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)

## Installation
To install and run the ForestQuery project locally, follow these steps:
1. Clone the repository to your local machine.
   ```
   git clone https://github.com/CharuKes/finalCapstone.git
   ```
2. Set up a database system (I used PostgreSQL) and import the provided [data tables](https://github.com/CharuKes/finalCapstone/tree/main/other_projects/deforestation_project_udacity_SQL/data).
3. The relationship between 3 tables can be seen [here](https://github.com/CharuKes/finalCapstone/blob/main/other_projects/deforestation_project_udacity_SQL/table_relationship/Deforestation%20DB.PNG).
4. To create ```view``` use SQL statement from §5 of [Deforestation Exploration Project](https://github.com/CharuKes/finalCapstone/blob/main/other_projects/deforestation_project_udacity_SQL/Deforestation%20Exploration%20Project.pdf).
5. This view will be used to run all SQL queries to produce the result for a given scenario in [Deforestation Exploration Project](https://github.com/CharuKes/finalCapstone/blob/main/other_projects/deforestation_project_udacity_SQL/Deforestation%20Exploration%20Project.pdf).

## Usage
After installing the ForestQuery project, you can use it to explore and analyze global deforestation data. The following sections provide an overview of the project's findings and recommendations.

### Global Situation
The world's total forest area in 1990 was 41,282,694.90 km<sup>2</sup>. By 2016, this number had decreased to 39,958,245.90 km<sup>2</sup>, resulting in a loss of 1,324,449.00 km<sup>2</sup> or 3.23%. The forest area lost during this time period is slightly larger than the entire land area of Peru listed for 2016 (1,279,999.99 km<sup>2</sup>).

### Regional Outlook
In 2016, the percentage of the world's total land area designated as forest was 31.38%. The region with the highest relative forestation was Latin America & Caribbean, with 46.16%, while the region with the lowest relative forestation was Middle East & North Africa, with 2.07% forestation. In 1990, Latin America & Caribbean also had the highest relative forestation with 51.03%, while Middle East & North Africa had the lowest with 1.78% forestation.

#### Table 2.1: Percent Forest Area by Region, 1990 & 2016
| Region              | 1990 Forest Percentage | 2016 Forest Percentage | Difference between 1990 and 2016 Forest Percentage |
|---------------------|-----------------------|-----------------------|--------------------------------------------------|
| Latin America & Caribbean   | 51.03%                | 46.16%                | -4.87%                                           |
| Sub-Saharan Africa         | 30.67%                | 28.79%                | -1.88%                                           |
| World               | 32.42%                | 31.38%                | -1.04%                                           |
| Europe & Central Asia  | 37.28%                | 38.04%                | 0.76%                                            |
| East Asia & Pacific    | 25.78%                | 26.36%                | 0.58%                                            |
| North America         | 35.65%                | 36.04%                | 0.39%                                            |
| South Asia            | 16.51%                | 17.51%                | 1.00%                                            |
| Middle East & North Africa  | 1.78%                 | 2.07%                 | 0.29%                                            |

### Country-Level Detail
#### Success Stories
One particularly bright spot in the data is China, which increased its forest area from 1990 to 2016 by a significant amount. In 1990, China had a forest area of 1,737,399.97 km<sup>2</sup>, which accounted for 16.55% of its total land area. However, by 2016, China's forest area had expanded to 2,022,800.00 km<sup>2</sup>, representing an increase of 285,400.03 km<sup>2</sup>. This growth in forest area was accompanied by an increase in the percentage of China's land area designated as forest, reaching 21.18% in 2016.

Another notable success story is Brazil, despite facing significant deforestation challenges. In 1990, Brazil had a forest area of 5,134,000.00 km<sup>2</sup>, which accounted for 63.98% of its total land area. Although Brazil experienced a decrease in forest area by 2016, with a recorded value of 4,935,758.80 km<sup>2</sup>, it managed to maintain a relatively high percentage of forestation, with 59.08% of its land area still covered by forests.

Chile is another country worth mentioning. With an initial forest area of 15,477.98 km<sup>2</sup> in 1990, it managed to increase its forested area to 19,488.49 km<sup>2</sup> by 2016. This expansion of 4,010.51 km<sup>2</sup> represents a growth rate of 25.91% over the 26-year period.

It is essential to acknowledge these success stories as they demonstrate that positive changes can occur even in the face of global deforestation challenges. These countries have implemented various measures and initiatives to promote reforestation, sustainable forestry practices, and conservation efforts.

However, it is crucial to continue these efforts and replicate their success in other regions and countries. Deforestation remains a significant issue globally, and concerted action is necessary to mitigate its adverse effects on biodiversity, climate change, and ecosystem stability.

### Areas of Concern
Despite the success stories, several countries experienced significant deforestation during the analyzed period. Some of the countries with notable forest area losses include:

1. Indonesia: From 1990 to 2016, Indonesia's forest area decreased by a staggering 595,063.64 km<sup>2</sup>. This loss represents a decline of 24.16% in the country's forested land area. Deforestation in Indonesia is primarily driven by factors such as palm oil plantations, illegal logging, and land conversion for agriculture.

2. Russia: Russia witnessed a substantial reduction in its forest area, declining by 364,510.99 km<sup>2</sup> between 1990 and 2016. This decrease corresponds to a 3.75% decline in Russia's forested land. Deforestation in Russia can be attributed to factors such as unsustainable logging practices, infrastructure development, and natural disturbances.

3. Democratic Republic of the Congo (DRC): The DRC experienced a forest area loss of 176,720.22 km<sup>2</sup> during the analyzed period. This reduction accounts for 5.89% of the country's forested land area. Deforestation in the DRC is driven by activities such as commercial logging, agricultural expansion, and illegal mining.

These countries serve as examples of the urgent need for targeted interventions and sustainable land management practices to combat deforestation and promote forest conservation.



### Recommendations
To address the global issue of deforestation and promote sustainable forest management, the following recommendations can be considered:

1. Strengthen Forest Protection Measures: Governments and international organizations should prioritize the enforcement of robust regulations and policies to protect forests. This includes implementing stricter penalties for illegal logging and land encroachment, as well as supporting initiatives that promote sustainable forestry practices.

2. Encourage Reforestation and Afforestation Efforts: Efforts should be made to restore and expand forest areas through reforestation and afforestation initiatives. Governments can incentivize and support tree planting programs, restoration projects, and agroforestry systems. Collaborative efforts between public and private sectors, local communities, and NGOs can facilitate the establishment of new forests and the restoration of degraded lands.

### Conclusion

The ForestQuery project provides valuable insights into global deforestation trends from 1990 to 2016. It highlights both success stories and areas of concern, emphasizing the need for sustainable forest management and conservation efforts.

While countries like China, Brazil, and Chile have made significant progress in increasing their forest areas, others, such as Indonesia, Russia, and the Democratic Republic of the Congo, have experienced alarming levels of deforestation. These findings underscore the urgency of implementing effective measures to combat deforestation worldwide.

The recommendations put forward in this report aim to address the issue of deforestation and promote sustainable forest management. Strengthening forest protection measures, encouraging reforestation and afforestation efforts, promoting sustainable land use practices, supporting indigenous and local communities, enhancing monitoring and enforcement, promoting sustainable consumption and trade, and fostering international cooperation are key strategies to combat deforestation effectively.

It is crucial for governments, organizations, and individuals to recognize the urgency of this issue and take collective action to safeguard our forests and ensure a sustainable future for generations to come. By implementing these recommendations, we can make significant progress in combating deforestation and promoting sustainable forest management. Together, we can preserve the vital ecosystems provided by forests and mitigate the environmental impacts of deforestation.

For more information and access to the ForestQuery project, please refer to the repository and documentation provided.
