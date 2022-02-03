#!/usr/bin/python3
import argparse
import re

import pandas as pd


def load_buildium_file(file):
    return pd.read_csv(file)


def get_all_properties(df):
    return df.buildingName.unique()


def convert_buildium_to_stessa(df):

    # Remove bogus data
    # Remove transactions that are zero dollars
    df = df[df.amount != 0]

    # # Remove owner contributions because these will be accounted for
    # df = df[df.glAccountName != 'Owner Contribution']

    # Buildium doesn't give a shit about their customers - lets make expenses actually negative and rents positive
    df.amount = df.amount.multiply(-1)

    # Strip the clock times to only leave the dates
    df.entryDate = pd.to_datetime(df['entryDate']).apply(lambda x: x.date())

    # Filter on only the columns we care about for Stessa
    df = df[['entryDate', 'amount', 'payeeName', 'postingMemo', 'glAccountName']]

    # Change the column names to what Stessa wants
    df.columns = ['Date', 'Amount', 'Payee', 'Description', 'Category']

    return df


def export_csv_by_property(df, filename):
    df.to_csv(filename)


def main(args):

    # Ignoring deprecated feature warning
    pd.set_option('mode.chained_assignment', None)

    df = load_buildium_file(args.file)
    properties = get_all_properties(df)

    for prop in properties:
        property_filename = re.sub(' ', '_', prop) + '.csv'
        df_one_prop = df[df.buildingName.eq(prop)]
        stessa_dataframe = convert_buildium_to_stessa(df_one_prop)
        export_csv_by_property(stessa_dataframe, property_filename)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description=f'Make buildium export better than hell on earth.')
    # Positional
    parser.add_argument('-f', '--file', type=str, metavar='', default='./Rental_Owner_Statement.csv', help="the file location of the buildium export csv file")
    args = parser.parse_args()
    main(args)
