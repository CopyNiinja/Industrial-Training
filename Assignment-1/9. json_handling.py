# Assignment 1: Write a script that reads a CSV file containing product information and converts it into a JSON file.
import csv
import json

def csv_to_json(csv_filepath, json_filepath):
    products = []
    with open(csv_filepath, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            products.append(row)

    with open(json_filepath, 'w') as json_file:
        json.dump(products, json_file, indent=4)

# Example usage:
csv_to_json('data/products.csv', 'data/products.json')
