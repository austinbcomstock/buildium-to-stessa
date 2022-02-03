# Buildium Transactions -> Stessa Transactions
There is currently no third-party integration between Buildium and Stessa to get transactions from Buildium into Stessa, see this [request](https://community.stessa.com/t/import-data-from-buildium/312/39). This repo allows you to transform Buildium transactions into something that is relatively easy to import into Stessa. 

The TLDR here is that `buildium_to_stessa.py` is a python file that takes a "Rental Owner Statement Report" (`Rental_Owner_Statement.csv`) that can be exported from Buildium and transforms the file into other files that Stessa understands and allows us to import. I intentionally designed this to create a separate file for each property to assist with categorizing the transactions to a specific rental in Stessa. That way you only have to categorize the type of transaction.

Open to contributions and fixing problems as several friends and family members use this as well.

## Pre-requisites
* python3
* pip (python3 -m 
* Rental_Owner_Statement.csv file (This file can be exported from Buildium as a "Rental Owner Statement Report exported to Comma-Separated CSV").

## Installation

1. `git clone https://github.com/YGdUy0z741qH/buildiumtostessa.git`

2. `cd ./buildiumtostessa`

3. `pipenv install -r requirements.txt`

OR

3. `pip install -r requirements.txt`

4. Move the the Rental_Owner_Statement.csv is in the `buildiumtostessa` folder

## Run the script

`pipenv run python buildium_to_stessa.py -f Rental_Owner_Statement.csv`

OR

`python buildium_to_stessa.py -f Rental_Owner_Statement.csv`

If its another location, `python buildium_to_stessa.py -f ./full/location/to/the/Rental_Owner_Statement.csv`

## See the created files
See the various files created, one for each address.

## Upload the files into Stessa
Upload each file individually into Stessa. Once logged into Stessa, go to Transactions (left bar) > Import (top right) > Choose one of the csv files that is a specific address > In the drop down for assign all transactions to the same address, select the same address as the filename. 

Rinse and repeat for each property.

