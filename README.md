# Dashboard Project

## References

* [Bootswatch theme](https://bootswatch.com/lumen/)
* [Reference Project](https://github.com/fiakoenjiniring/rainfall/tree/main)
* [Reference site - 1](http://ramwheatdb.com/headtohead.php)
* [Reference site - 2](https://www.myfields.info/crop-data)
* [Reference app](https://analytics.iasoybeans.com/cool-apps/ISOFAST/)
* [Geo Data](https://public.opendatasoft.com/explore/dataset/us-county-boundaries)

## Restart
* Scrape almost every vis.
* Focus on genotypes.
  * genotype yield by year.
  * compare yield from 2 genotypes.
  * check data from counties and try something. 

## To-do
### Data Engineering
- [x] Add new datasets.
- [x] Collect Kansas geo data.
- [x] Pre-process the datasets.
- [x] Pre-pre-process the datasets outside the main app to maintain high performance. 
- [x] Process corn and wheat dataset to deleted metrics in genotype NAME.
- [x] Drop duplicate rows in the datasets.
- [x] Make this combination unique [YEAR, NAME, COUNTY, WATER_REGIME].
- [x] Fix new datasets.
- [x] Fix, LOC, WATER_REGIME and COUNTY fields.
- [x] Fix harvest_date unit.
- [x] Figure site/loc acronyms: The location "code" is the 2-letter county abbreviation and "D" for dryland or "I" for irrigated for all crops. A "S" in wheat or corn is a soft test or a short season test and "C" and "O" are confectionary and oilseed respectively for sunflower. 
- [ ] Store only a fixed set of columns. Setup this columns in config.

### Front-end
- [x] Create home, compare, about and data pages.
- [x] Create pages layout for home, compare, about and data.
- [x] Change pages layout using dbc 
- [x] Data page functionality: Download filtered datasets by year.
- [ ] Leave home page to introduce the app.
- [ ] Leave about page to display infos and paper.
- [ ] Make compare into main view page.
- [ ] Change header to a sidebar?.
- [ ] Front-end.

### Data Analysis
- [ ] make it in a pop up window?
- [x] fix hovers, round hovers and add units in titles and hovers.
- [x] Add units (see in the xlsx files) (add to graph title).
- [x] Add option to change units.
- [x] Fix unit selector not clearing options store and list.
- [x] US customary units: bu/ac and lb/ac --- Metric: Mg/ha, kg/ha --- [Conversion Rates](https://www.extension.iastate.edu/agdm/wholefarm/html/c6-80.html).
- [x] add a max amount that the user can input.
- [x] change clear genotypes btn, input year dropdown, crops dropdown to clear the graphs
- [x] fix bar and box vis, the analysis and display of information is not matching and something is going on there.
* Add county filter in compare?
  - [x] I was thinking in making a separate view for the counties, leave 1 for the avg of all of them, another representing them in a box plot so the user can check by themselves, and lastly one to show each county individually.
- [x] add a filter for genotype with diff years.
  * Should the user input the years or just throw all of them?


* fix errors
  - [x] Genotyopes string in selected list
  - [x] Change map to avg instead of sum. Change title
  - [x] Remove counties without data in the map
  - [x] Convert units and keep selected list. dont clear it
  - [ ] data already added bug.
  - [ ] check data filtering process if is still right with newer version of pandas.
  - [ ] filter by county later
- [x] remove 2 units
- [ ] better front
- [ ] cleanup
- [ ] launch a little prototype
