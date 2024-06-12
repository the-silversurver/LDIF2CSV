import ldif

def read_ldif(ldif_file_path):
    try:
        with open(ldif_file_path, 'rb') as ldif_file:
            parser = ldif.LDIFRecordList(ldif_file)
            parser.parse()

            attributes = set()
            records = []

            for dn, entry in parser.all_records:
                if dn is None or entry is None:
                    print(f"UInvalid entry in the LDIF file: dn={dn}, entry={entry}")
                    continue

                records.append((dn, entry))
                attributes.update(entry.keys())

            return sorted(attributes), records
    except Exception as e:
        print(f"Error reading the LDIF file: {e}")
        return [], []