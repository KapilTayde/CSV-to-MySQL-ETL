# CSV to MySQL ETL Project

## Overview
This project demonstrates how to efficiently import large CSV files (50,000+ rows) into MySQL using Python, pandas, and MySQL Connector. It handles batch processing, bulk insertion, and duplicate handling to ensure efficient data loading.

## Project Features
- **CSV Generation**: Generates large CSV files with sample data using the Faker library.
- **Batch Processing**: Reads the CSV file in chunks (5,000 rows) to avoid memory overload.
- **Efficient Insertion**: Uses `executemany()` to insert data in batches.
- **Duplicate Handling**: Prevents duplicate entries using `INSERT IGNORE`.

## Getting Started
1. Clone the repository:  
   ```bash
   git clone https://github.com/KapilTayde/CSV-to-MySQL-ETL.git

