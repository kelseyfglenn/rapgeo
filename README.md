Objective:

* Categorize hip-hop songs and artists by lyrical content and prosodic style. 

Notebook Order:

* data_collection -> preprocessing -> topic_modeling -> clustering
* webapp folder contains files for flask deployment including Tableau dashboard embedding

Data Sources:

* **Artist List:** “List of hip hop musicians”, Wikipedia https://en.wikipedia.org/wiki/List_of_hip_hop_musicians

* **Artist and Song Metadata:** Genius API https://api.genius.com/ 

* **Song Lyrics:** Genius.com web scrape (API doesn’t support lyric requests)

Methodology:

* **Data Collection**
  * Scrape wikipedia for artist names
  * Genius API requests for top N songs by each artist
  * Genius.com scrape for lyrics to each song
* **Preprocessing**
    * Clean and tokenize text
    * Generate TF-IDF matrix
    * Calclating unique word proportions and syllable rates
* **Analysis**
      * Topic Modeling
      * NMF Topic Modeling to create semantic categories
      * Combine with unique word and syllabic information and apply KMeans clustering
      * Aggregate artists’ song categorizations to characterize their style
  * **Deployment**
    * Recommender flask application
    * Tableau visualization

Link to Tableau Public Workbook:

https://public.tableau.com/views/Metis_Proj4_Viz/Dashboard1?:language=en&:display_count=y&publish=yes&:origin=viz_share_link