import csv
import os

def load_csv(filename):
    """
    Reads a CSV file and returns all rows as a list of dictionaries.
    Each dictionary maps column names to their values.
    """
    if not os.path.isfile(filename):
        print(f"File '{filename}' does not exist.")
        return []

    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        records = list(reader)

    if not records:
        print("CSV file is empty.")
    return records

def data_summary(data):
    """
    Returns the total number of rows in the dataset.
    """
    return len(data)

def search_data(data):
    """
    Allows the user to search for rows matching a column value.
    """
    if not data:
        print("No data to search.")
        return []

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

def generate_statistics(data):
    """
    Computes summary statistics and saves them to a text file.
    """
    if not data:
        print("No data available to generate statistics.")
        return

    total_quantity = 0
    total_price = 0.0
    count_rows = 0
    unique_products = set()
    skipped_rows = 0

    for row in data:
        try:
            quantity = int(row["Quantity"])
            price = float(row["Price"])
        except (ValueError, KeyError):
            skipped_rows += 1
            continue

        total_quantity += quantity
        total_price += price
        count_rows += 1
        unique_products.add(row.get("Product", "Unknown"))

    average_price = total_price / count_rows if count_rows > 0 else 0

    report = (
        "\n--- Summary Statistics ---\n"
        f"Total Quantity Sold: {total_quantity}\n"
        f"Average Price: {average_price:.2f}\n"
        f"Number of Unique Products: {len(unique_products)}\n"
        f"Rows Skipped Due to Invalid Data: {skipped_rows}\n"
    )

    print(report)

    with open("summary_report.txt", "w") as report_file:
        report_file.write(report)

    print("Summary statistics saved to 'summary_report.txt'.")

def preview_data(data, num_rows=5):
    """
    Prints the first N rows of the data.
    """
    if not data:
        print("No data to preview.")
        return

    print(f"\nPreview of data (first {num_rows} rows):")
    for i, row in enumerate(data[:num_rows], start=1):
        print(f"\nRow {i}:")
        for key, value in row.items():
            print(f"{key}: {value}")

def main():
    try:
        filename = input("Enter the CSV filename to load: ")
        csv_data = load_csv(filename)

        if not csv_data:
            print("Exiting due to missing or empty data.")
            return

        while True:
            print("\n--- Menu ---")
            print("1. Preview Data")
            print("2. Show Total Rows")
            print("3. Search Data")
            print("4. Generate Statistics")
            print("5. Exit")

            choice = input("Enter your choice (1-5): ")

            if choice == "1":
                preview_data(csv_data)
            elif choice == "2":
                total_rows = data_summary(csv_data)
                print(f"\nTotal rows in dataset: {total_rows}")
            elif choice == "3":
                search_results = search_data(csv_data)
                if search_results:
                    print("\nMatching rows:")
                    for r in search_results:
                        print("-----")
                        for key, value in r.items():
                            print(f"{key}: {value}")
                else:
                    print("\nNo matches found.")
            elif choice == "4":
                generate_statistics(csv_data)
            elif choice == "5":
                print("Exiting program. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 5.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
