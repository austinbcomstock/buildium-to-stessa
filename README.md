# Buildium Transactions -> Stessa Transactions
There is no third-party integration between Buildium and Stessa to get transactions from Buildium into Stessa; see this [request](https://community.stessa.com/t/import-data-from-buildium/312/39). This repo allows you to transform Buildium transactions into something relatively easy to import into Stessa.

# TLDR
`buildium_to_stessa.py` takes a "Rental Owner Statement Report," `Rental_Owner_Statement.csv`, from Buildium. It outputs one file per property with all transactions for that property. The output file is ready to be manually uploaded into Stessa and can be tagged for a specific property upon upload. Having a separate output file for each property and using that tag on the upload feature makes it relatively painless to tag transactions to a particular rental. That way, you only have to categorize the transaction type.

Open to contributions and fixing problems as several friends and family members use this.

## Pre-requisites
* python3
* pip / pipenv
* Rental_Owner_Statement.csv file (This file can be exported from Buildium as a "Rental Owner Statement Report exported to Comma-Separated CSV").

## Installation

1. `git clone https://github.com/austinbcomstock/buildium-to-stessa.git`

2. `cd ./buildium-to-stessa`

3. `pipenv install -r requirements.txt`

OR

3. `pip install -r requirements.txt`

4. Move the Rental_Owner_Statement.csv is in the `buildium-to-stessa` folder

## Run the script

`pipenv run python buildium_to_stessa.py -f Rental_Owner_Statement.csv`

OR

`python buildium_to_stessa.py -f Rental_Owner_Statement.csv`

## See the created files
See the various files created, one for each address.

## Upload the files into Stessa
Upload each file individually into Stessa. Once logged into Stessa, go to Transactions (left bar) > Import (top right) > Choose one of the CSV files that is a specific address > In the drop-down for assigning all transactions to the same address, select the same address as the filename. Rinse and repeat for each property file.
