import argparse
import csv
from collections import defaultdict

def parse_args():
    parser = argparse.ArgumentParser(description='Calculate statistics on unemployment rates.')
    parser.add_argument('input_file', help='Path to the input CSV file')
    parser.add_argument('--country', required=True, help='Country to perform operation for (country name)')
    parser.add_argument('-o', choices=['avg', 'min', 'max'], default='avg', help='Operation to perform on unemployment rates (default: avg)')
    parser.add_argument('--from', dest='from_year', type=int, help='Starting year (inclusive)')
    parser.add_argument('--to', dest='to_year', type=int, help='Ending year (inclusive)')
    return parser.parse_args()

def calculate_statistics(data, operation):
    if operation == 'avg':
        return sum(data) / len(data)
    elif operation == 'min':
        return min(data)
    elif operation == 'max':
        return max(data)

def filter_data(rows, country, operation, from_year, to_year):
    filtered_data = [float(row[3]) for row in rows if row[0] == country and (from_year is None or int(row[2]) >= from_year) and (to_year is None or int(row[2]) <= to_year)]
    if not filtered_data:
        return None  # No data found for the specified criteria
    return calculate_statistics(filtered_data, operation)

def main():
    args = parse_args()

    with open(args.input_file, 'r', newline='') as file:
        reader = csv.reader(file)
        header = next(reader)  # Skip the header row
        rows = list(reader)

    result = filter_data(rows, args.country, args.o, args.from_year, args.to_year)

    if result is not None:
        print(f"Unemployment rate {args.o} for {args.country} from {args.from_year if args.from_year else 'start'} to {args.to_year if args.to_year else 'end'}: {result}")
    else:
        print(f"No data found for the specified criteria.")

if __name__ == '__main__':
    main()
