# VTT to Excel Converter

This Python application reads two VTT (WebVTT) files, combines their entries based on specific logic, and writes the combined entries to an Excel file. The application uses the [`openpyxl`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Ffatenhealy%2FDesktop%2FCSharpCombinationApp%2FVttToExcel%2Fconvertionvtt.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A1%2C%22character%22%3A5%7D%7D%5D%2C%22afc657e3-ebeb-4477-9cea-9b32cd5fda62%22%5D "Go to definition") library to create and manipulate the Excel file.

## Features

- Parses VTT files to extract timestamps and values.
- Combines entries from two VTT files based on their timestamps.
- Writes the combined entries to an Excel file with columns for source and translated timestamps and values.
- Adds an additional "Notes" column in the Excel file.

## Requirements

- Python 3.x
- [`openpyxl`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Ffatenhealy%2FDesktop%2FCSharpCombinationApp%2FVttToExcel%2Fconvertionvtt.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A1%2C%22character%22%3A5%7D%7D%5D%2C%22afc657e3-ebeb-4477-9cea-9b32cd5fda62%22%5D "Go to definition") library

## Installation

1. **Clone the repository or download the script:**
   ```sh
   git clone https://github.com/yourusername/vtt-to-excel.git
   cd vtt-to-excel
   ```

2. **Install the required library:**
   ```sh
   pip install openpyxl
   ```

   Or, if using `pip3` for Python 3:
   ```sh
   pip3 install openpyxl
   ```

## Usage

1. **Prepare your VTT files:**
   - Ensure you have two VTT files: `source.vtt` and `translated.vtt`.

2. **Run the Python script:**
   ```sh
   python convertionvtt.py
   ```

   Or, if using Python 3:
   ```sh
   python3 convertionvtt.py
   ```

3. **Check the output:**
   - The script will generate an Excel file named `TheOutput.xlsx` in the same directory.

## Explanation of the Code

### [`parse_vtt_file(file_path)`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Ffatenhealy%2FDesktop%2FCSharpCombinationApp%2FVttToExcel%2Fconvertionvtt.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A3%2C%22character%22%3A4%7D%7D%5D%2C%22afc657e3-ebeb-4477-9cea-9b32cd5fda62%22%5D "Go to definition")

This function reads a VTT file and parses the entries to extract timestamps and values.

### [`combine_entries(source_entries, translated_entries)`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Ffatenhealy%2FDesktop%2FCSharpCombinationApp%2FVttToExcel%2Fconvertionvtt.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A24%2C%22character%22%3A4%7D%7D%5D%2C%22afc657e3-ebeb-4477-9cea-9b32cd5fda62%22%5D "Go to definition")

This function combines the source and translated entries based on the following logic:
- When `Source Timestamp` equals `Translated Timestamp`, they are placed on the same row.
- When `Source Timestamp` is greater than `Translated Timestamp`, the translated timestamp values are kept, and the source timestamp and source value are left empty/blank for that row.
- When `Source Timestamp` is less than `Translated Timestamp`, the source timestamp values are kept, and the translated timestamp and translated value are left empty/blank for that row.

### [`write_to_excel(combined_entries, file_path)`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Ffatenhealy%2FDesktop%2FCSharpCombinationApp%2FVttToExcel%2Fconvertionvtt.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A61%2C%22character%22%3A4%7D%7D%5D%2C%22afc657e3-ebeb-4477-9cea-9b32cd5fda62%22%5D "Go to definition")

This function writes the combined entries to an Excel file using the [`openpyxl`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Ffatenhealy%2FDesktop%2FCSharpCombinationApp%2FVttToExcel%2Fconvertionvtt.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A1%2C%22character%22%3A5%7D%7D%5D%2C%22afc657e3-ebeb-4477-9cea-9b32cd5fda62%22%5D "Go to definition") library. It creates a new Excel file with columns for source and translated timestamps and values, and an additional "Notes" column.

### [`main()`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Ffatenhealy%2FDesktop%2FCSharpCombinationApp%2FVttToExcel%2Fconvertionvtt.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A79%2C%22character%22%3A4%7D%7D%5D%2C%22afc657e3-ebeb-4477-9cea-9b32cd5fda62%22%5D "Go to definition")

This function orchestrates the process by calling the above functions and printing a success message.

## Example

1. **Sample `source.vtt`:**
   ```
   00:00:01.000 --> 00:00:05.000
   Hello, world!

   00:00:06.000 --> 00:00:10.000
   This is a test.
   ```

2. **Sample `translated.vtt`:**
   ```
   00:00:01.000 --> 00:00:05.000
   Hola, mundo!

   00:00:07.000 --> 00:00:11.000
   Esto es una prueba.
   ```

3. **Generated `TheOutput.xlsx`:**
   | Source Timestamp | Source Value   | Translated Timestamp | Translated Value     | Notes |
   |------------------|----------------|----------------------|----------------------|-------|
   | 00:00:01.000     | Hello, world!  | 00:00:01.000         | Hola, mundo!         |       |
   | 00:00:06.000     | This is a test.|                      |                      |       |
   |                  |                | 00:00:07.000         | Esto es una prueba.  |       |

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Contact

For any questions or suggestions, please contact @fatenhealy fatenhealy@github.com.
