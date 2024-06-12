import csv

def safe_decode(value):
    try:
        return value.decode('utf-8')
    except UnicodeDecodeError:
        return value.hex()

def write_csv(csv_file_path, attributes, records):
    with open(csv_file_path, mode='w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["dn"] + attributes)
        for dn, entry in records:
            row = [dn]
            for attr in attributes:
                value = entry.get(attr, [''])
                value = [safe_decode(v) if isinstance(v, bytes) else v for v in value]
                row.append(','.join(value))
            writer.writerow(row)
    print(f"Data was successfully exported to the CSV file {csv_file_path}.")
