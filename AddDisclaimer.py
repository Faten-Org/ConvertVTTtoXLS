import re

def add_seconds_to_timestamp(timestamp, seconds):
    """Add seconds to a VTT timestamp."""
    hours, minutes, secs = map(float, timestamp.split(':'))
    total_seconds = hours * 3600 + minutes * 60 + secs + seconds
    new_hours = int(total_seconds // 3600)
    new_minutes = int((total_seconds % 3600) // 60)
    new_seconds = total_seconds % 60
    return f'{new_hours:02}:{new_minutes:02}:{new_seconds:06.3f}'

def add_disclaimer_to_vtt(input_file, output_file, seconds_to_add):
    timestamp_pattern = re.compile(r'(\d{2}:\d{2}:\d{2}\.\d{3}) --> (\d{2}:\d{2}:\d{2}\.\d{3})')
    
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            match = timestamp_pattern.search(line)
            if match:
                start_time, end_time = match.groups()
                new_start_time = add_seconds_to_timestamp(start_time, seconds_to_add)
                new_end_time = add_seconds_to_timestamp(end_time, seconds_to_add)
                outfile.write(f'{new_start_time} --> {new_end_time}\n')
            else:
                outfile.write(line)

def main():
    input_file = 'translated.vtt'
    output_file = 'translatedPlusDisclaimer.vtt'
    seconds_to_add = 3

    add_disclaimer_to_vtt(input_file, output_file, seconds_to_add)
    print(f'New VTT file created: {output_file}')

if __name__ == "__main__":
    main()