import os
from openpyxl import Workbook

def parse_vtt_file(file_path):
    entries = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        current_entry = None

        for line in lines:
            line = line.strip()
            if '-->' in line:
                if current_entry:
                    entries.append(current_entry)
                current_entry = {'timestamp': line, 'value': ''}
            elif line:
                if current_entry:
                    current_entry['value'] += line + ' '

        if current_entry:
            entries.append(current_entry)

    return entries

def combine_entries(source_entries, translated_entries):
    combined_entries = []
    source_index, translated_index = 0, 0

    while source_index < len(source_entries) or translated_index < len(translated_entries):
        source_entry = source_entries[source_index] if source_index < len(source_entries) else {'timestamp': '', 'value': ''}
        translated_entry = translated_entries[translated_index] if translated_index < len(translated_entries) else {'timestamp': '', 'value': ''}

        if source_entry['timestamp'] == translated_entry['timestamp']:
            combined_entries.append({
                'source_timestamp': source_entry['timestamp'],
                'source_value': source_entry['value'],
                'translated_timestamp': translated_entry['timestamp'],
                'translated_value': translated_entry['value']
            })
            source_index += 1
            translated_index += 1
        elif not source_entry['timestamp'] or source_entry['timestamp'] > translated_entry['timestamp']:
            combined_entries.append({
                'source_timestamp': '',
                'source_value': '',
                'translated_timestamp': translated_entry['timestamp'],
                'translated_value': translated_entry['value']
            })
            translated_index += 1
        else:
            combined_entries.append({
                'source_timestamp': source_entry['timestamp'],
                'source_value': source_entry['value'],
                'translated_timestamp': '',
                'translated_value': ''
            })
            source_index += 1

    combined_entries.sort(key=lambda e: (e['source_timestamp'] or e['translated_timestamp'], e['translated_timestamp'] or e['source_timestamp']))
    return combined_entries

def write_to_excel(combined_entries, file_path):
    workbook = Workbook()
    worksheet = workbook.active
    worksheet.title = "Sheet1"

    worksheet.append(["Source Timestamp", "Source Value", "Translated Timestamp", "Translated Value", "Notes"])

    for entry in combined_entries:
        worksheet.append([
            entry['source_timestamp'],
            entry['source_value'],
            entry['translated_timestamp'],
            entry['translated_value'],
            ""
        ])

    workbook.save(file_path)

def main():
    source_file_path = "source.vtt"
    translated_file_path = "translated.vtt"
    output_file_path = "TheOutput.xlsx"

    source_entries = parse_vtt_file(source_file_path)
    translated_entries = parse_vtt_file(translated_file_path)

    combined_entries = combine_entries(source_entries, translated_entries)

    write_to_excel(combined_entries, output_file_path)

    print("Excel file created successfully.")

if __name__ == "__main__":
    main()