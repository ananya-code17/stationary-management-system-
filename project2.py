print("This is project-2 on: STATIONARY MANAGEMENT SYSTEM \n\n")

import pandas as pd
import numpy as np

def create_stationary_data():
    stationary_data = {}
    while True:
        item_name = input("Enter Item Name (or 'q' to quit): ")
        if item_name.lower() == 'q':
            break
        try:                 #The try block lets you test a block of code for errors. The except block lets you handle the error
            price = float(input("Enter Price (INR): "))
            stock = int(input("Enter Stock (Units): "))
        except ValueError:  #If the input for price or stock is not a number (ValueError
            print("Invalid input. Please enter numbers for price and stock.")
            continue
        stationary_data[item_name] = {'Price (INR)': price, 'Stock (Units)': stock}
    return pd.DataFrame(stationary_data).transpose()  #DataFrame function is used to oraganise the data in a tabular format
                                                                               #.transpose() function is used to swap the rows and columns.


def main():
    stationary_df = create_stationary_data()
    
    def identify_low_stock(threshold):  #function to identify items with low stock
        low_stock_df = stationary_df[stationary_df['Stock (Units)'] <= threshold]
        if low_stock_df.empty:  # .empty returns True if the DataFrame has no rows of data (i.e., it's empty), and False otherwise.
            print("\nNo items are currently low on stock.")
        else:
            print("\nFollowing items have low stock (", threshold, " units or less):")
            print(low_stock_df.to_string())
    identify_low_stock(5)

    def update_item(item_name):   #function to update the item
        if item_name in stationary_df.index:
            new_price = float(input("Enter new price (INR): "))
            new_stock = int(input("Enter new stock (Units): "))
            stationary_df.loc[item_name] = {'Price (INR)': new_price, 'Stock (Units)': new_stock}
            print("Item details updated successfully!")
        else:
            print("Item not found in inventory.")
    update_choice = input("\nDo you want to update item details (y/n)?: ")
    if update_choice.lower() == 'y':
        update_item_name = input("Enter item name to update: ")
        update_item(update_item_name)

    def add_item(stationary_df):  #function to add an item
        item_name = input("Enter Item Name: ")
        if item_name in stationary_df.index:
            print("Item already exists in inventory.")
            return
        try:
           price = float(input("Enter Price (INR): "))
           stock = int(input("Enter Stock (Units): "))
        except ValueError:
            print("Invalid input. Please enter numbers for price and stock.")
            return
        stationary_df.loc[item_name] = {'Price (INR)': price, 'Stock (Units)': stock}
        print("Item added successfully!")
    add_choice = input("\nDo you want to add item details (y/n)?: ")
    if add_choice.lower() == 'y':
        add_item(stationary_df)

    def remove_item(stationary_df, item_name):  #function to remove an item
        if item_name in stationary_df.index:
            stationary_df.drop(item_name, inplace=True)  #drop() function is used to remove a row from the DataFrame.
                                                                               # inplace parameter, when set to True, removes the row directly from the original DataFrame
            print("Item removed successfully!")
        else:
            print("Item not found in inventory.")
    remove_choice = input("\nDo you want to remove an item (y/n)?: ")
    if remove_choice.lower() == 'y':
        remove_item_name = input("Enter item name to remove: ")
        remove_item(stationary_df, remove_item_name)
    
        
    stationary_df['Total Value (INR)'] = stationary_df['Price (INR)'] * stationary_df['Stock (Units)']
    print("\n======Stationary Shop Inventory====:")
    print(stationary_df.to_string())  #to_string displays the data in string representation making it easier to print the data.
    total_stock_value = np.sum(stationary_df['Total Value (INR)'])
    print("\n\nTotal Stock Value (INR):", total_stock_value)  
    most_expensive_item = stationary_df.loc[stationary_df['Price (INR)'].idxmax()]   #.loc[] function is used to retrieve the corresponding row of most expensive item
                                                                                                                        #idxmax() function is used to find the item name of the most expensive item
    print("\n\nMost Expensive Item:")
    print(most_expensive_item)


if __name__ == "__main__":
    main()

