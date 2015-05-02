# Summary
Campaign finance data is an important part of keeping our democracy accountable. This project aims on checking the integrity of that data. "OFEC check" attacks this problem in two ways. It keeps track of FEC data over time and it tests the soon to be released FEC API against the bulk data. 

Tracing the data overtime can surface possible data issues and keep track of how data is amended over time. Testing the new API against the current, canonical data will identify potential data quality issues in the new data infrastructure that can then be fixed before release. 

Historically there have been [reports of inconsistencies](http://ethics.harvard.edu/blog/researchers-find-inconsistencies-fec-data) between the FEC bulk data and the FEC individual records. In transferring from one database to another, or going from individual records to bulk data releases, data can be lost or corrupted. Our project helps ensure that data coming from the government is sound and can be used for accurate reporting. 


# Stay in Touch!
Leave us your name and email address. No spam, only important updates, we promise!

http://goo.gl/qjbWDO

# Getting Started

1. Create new database

2. Edit `keys.example.json` to include database parameters and rename it to `keys.json`
```
createdb campaigncon
```

3. Seed the database and ingest some new data
```
python main.py reset
python main.py ingest
```

4. Navigate to the website
```
open http://localhost:5000/?before=04-05-2015&after=05-01-2015
```

# Download New Data

1. Download data
```
# Download the data only if there is a new version on the FEC website
python download.py

# Ingest into database
python main.py ingest
```

# Hack4Cogress
https://hackpad.com/Hack4Congress-DC-9oz0P32pSCa

# iCorruptionHack
http://ethics.harvard.edu/event/ending-institutional-corruption-hackathon
