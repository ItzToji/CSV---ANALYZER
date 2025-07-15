import csv

try:
    # Function to load data from a CSV file
    def load_csv(filename):
        """
        Reads a CSV file and returns all rows as a list of dictionaries.
        Each dictionary maps column names to their values.
        """
        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            records = list(reader)
        return records

    # Function to return the total number of rows
    def data_summary(data):
        """
        Returns the total number of rows in the dataset.
        """
        return len(data)

    # Function to search for rows by column value
    def search_data(data):
        """
        Allows the user to search for rows matching a column value.
        """
        # Show available columns
        print("Available columns:", list(data[0].keys()))

        column_name = input("Enter the column you want to search: ")
        search_value = input("Enter the value you want to search in the column: ")

        if column_name not in data[0]:
            print("Invalid column name. Please check the available columns.")
            return []

        matching_rows = []
        for row in data:
            if row[column_name] == search_value:
                matching_rows.append(row)

        return matching_rows

    # Function to generate and print summary statistics
    def generate_statistics(data):
        """
        Computes and prints summary statistics:
        - Total quantity sold
        - Average price
        - Number of unique products
        """
        total_quantity = 0
        total_price = 0.0
        count_rows = 0
        unique_products = set()

        for row in data:
            quantity = int(row["Quantity"])
            price = float(row["Price"])

            total_quantity += quantity
            total_price += price
            count_rows += 1
            unique_products.add(row["Product"])

        average_price = total_price / count_rows if count_rows > 0 else 0

        print("\n--- Summary Statistics ---")
        print(f"Total Quantity Sold: {total_quantity}")
        print(f"Average Price: {average_price:.2f}")
        print(f"Number of Unique Products: {len(unique_products)}")

    # ------------------ MAIN EXECUTION ------------------

    # Load the CSV data
    csv_data = load_csv("sample_data.csv")

    # Display the first 5 rows
    print("\nPreview of data (first 5 rows):")
    for row in csv_data[:5]:
        print(row)

    # Show total rows
    total_rows = data_summary(csv_data)
    print("\nTotal rows in dataset:", total_rows)

    # Perform search
    search_results = search_data(csv_data)

    if search_results:
        print("\nMatching rows:")
        for r in search_results:
            print("-----")
            for key, value in r.items():
                print(f"{key}: {value}")
    else:
        print("\nNo matches found.")

    # Generate statistics
    generate_statistics(csv_data)

except Exception as e:
    print(f"An error occurred: {e}")
