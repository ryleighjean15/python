import csv


def read_dictionary(filename, key_column_index=None):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.
    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """

    dictionary = {}

    with open('products.csv','rt') as csv_file:
        
        reader = csv.reader(csv_file)

        next(reader)

        for row in reader:
            key = row[key_column_index]
            dictionary[key] = row

    return dictionary


import csv

def read_dictionary(filename, key_column_index=None):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    dictionary = {}

    with open(filename, 'rt') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  

        for row in reader:
            key = row[key_column_index]
            dictionary[key] = row

    return dictionary

def main():
    products_dict = read_dictionary('products.csv', 0)  

    print(products_dict)
    # for key, value in products_dict.items():
    #     print(f"{key}: {value}")
    
    with open('request.csv','r') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  


        for row in reader:
            product_number = row[0]
            requested_quantity = int(row[1])

            product_info = products_dict.get(product_number)

            if product_info:
                product_name = product_info[1]  
                product_price = float(product_info[2])  

                print(f"Product Name: {product_name}, Requested Quantity: {requested_quantity}, Product Price: ${product_price:.2f}")
            else:
                print(f"Product number {product_number} not found in products dictionary.")



if __name__ == "__main__":
    main()

from datetime import datetime
current_date_and_time = datetime.now()
print(f"{current_date_and_time: %A %I %M %p}")