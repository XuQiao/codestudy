# MemberMap for Qishi (www.qishicpc.com)
These htmls are interactive maps, for the members geometrical distribution accoss the world. The member are mainly in United States. Some of them studied in U.S, but come back to China for further work.
- companymap.html marks the current company locations. You can zoom-in/zoom-out to see how many members/companys in a certain geometrical area, i.e., for a city, or for a state.
- allcompanysmap.html marks the history company locations. 
- schoolmap.html marks the school locations the member has affifilated with. 

You need to install plugins and python packages to use the jupyter notebook.
- [Folium](https://pypi.org/project/folium/) is a python package used to create the interactive map. It incorpates leaflet's map resources. Since the package finally will be translated to javascript lanaguage, we can modify it to let it more powerful by adding JS script support.
- pandas, numpy are packages to deal with dataframes and input/output csv files.
- [selenium](https://www.seleniumhq.org/) is another super powerful tool to do web scrapping. The current main scrawling site is www.linkedin.com, by auto-filling into the search page of linkedin search box (after logging in), and select the most relevant result, we can get more infomation about the member only with the first, last name. Here I use chrome webdriver to simulate the clicking procedure. It has to be downloaded before use.
- To get the exact location of a place, we need to fetch the latitude and longitude. [googlemaps api](https://github.com/googlemaps/google-maps-services-python) is the tool for generating (lat, lng) pairs for a search place string. 
- [geopy](https://pypi.org/project/geopy/) is the package for calculating distance given (lat, lng) pairs
- Some geo-places needs to be merged, if two places are too close and has similar names, we think these two places are actually the same place (Like The Stony brook and Stony brook University). SequenceMatcher in [difflib](https://docs.python.org/2/library/difflib.html) is the method I choose for calculating the similarity between two corpuses.


