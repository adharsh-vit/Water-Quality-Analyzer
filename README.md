 Water Quality Analyzer

 Project Overview

A Python-based application that analyzes water-test results and manages water-quality records.

The application allows the user to enter water-test results like pH, TDS, turbidity, hardness, nitrate, sulphate, chlorine, and temperature. The application then analyzes the values and generates a water-quality report for the sample.

The application offers record management through a CSV file that acts as the data storage system for storing water-quality records. The application also offers a statistics module that analyzes the stored records and generates statistics.

---

 Objectives

To offer a simple system for analyzing water-test results

To generate a readable water-quality report from the entered test values.

To store and manage water-quality records using a CSV file

To offer search and analysis facilities for stored records.

To compute basic statistics from stored water-quality data

Demonstrate Python programming concepts in a practical way

---

 Features

 1. Water Test Report Generator

Allows the user to enter freshly tested water parameters and generates a water-quality report.

Parameters include:

pH

TDS

Turbidity

Hardness

Nitrate

Sulphate

Chlorine

Temperature

 2. Add Record

Saves water-test information into the CSV data file

 3. View Records

Displays the stored water-quality records.

 4. Search by Location

Looks up stored records by location

 5. Analyze Record

Analyzes an existing record by selecting the record ID and generating an analysis report

 6. Delete Record

Deletes a water-quality from the CSV file by selecting the record ID

 7. Statistics

Calculates basic statistics from stored records.

Statistics include:

Total number of records

Average pH

Highest and lowest pH

Average TDS

Highest and lowest TDS

Average turbidity

Highest and lowest turbidity

 8. Input Validation

Validates key inputs, including:

pH values

Dates

Locations

Numerical values

---

 Project Structure

text

Water-Quality-Analyzer/

│

├── main.py

├── analyzer.py

├── validator.py

├── report.py

├── statistics.py

├── test_analyzer.py

│

├── water_quality_samples.csv

│

├── README.md

└── statement.md



 Module Description

| File            | Purpose                          |

| --------------------------- | ---------------------------------------------------------- |

| main.py          | Controls menu and connects all modules          |

| analyzer.py        | Analyzes water parameters and calculates the quality score |

| validator.py       | Validates user input                   |

| report.py         | Generates the water-quality report            |

| statistics.py       | Computes statistics from stored records         |

| test_analyzer.py     | Tests the water-analysis functionality          |

| water_quality_samples.csv | Stores water-quality records               |

---

 Technologies Used

Python

CSV

Python Functions

Python Modules

Dictionaries

Lists

File Handling

Input Validation

Basic Statistical Calculations

No external libraries are used in the current version.

---

 Requirements

Python 3.x

A code editor (e.g., VS Code)

Command Prompt / PowerShell / Terminal

---

 Installation and Setup

 1. Clone the repository

bash

git clone



 2. Open the project folder

bash

cd Water-Quality-Analyzer



 3. Run the application

bash

python main.py



---

 Main Menu

text

========================================

WATER QUALITY ANALYZER

========================================

1. Water Test Report Generator

2. Add Record

3. View Records

4. Search by Location

5. Analyze Record

6. Delete Record

7. Statistics

8. Exit



---

 How to Use

 Water Test Report Generator

Select 1 and provide the results of a sample water test at a specified location

Sample input:

text

Enter Location: College Canteen

Enter Date (YYYY-MM-DD): 2026-09-30

Enter pH: 7.2

Enter TDS (mg/L): 420

Enter Turbidity (NTU): 2.4

Enter Hardness (mg/L): 180

Enter Nitrate (mg/L): 15

Enter Sulphate (mg/L): 100

Enter Chlorine (mg/L): 0.5

Enter Temperature (°C): 26



The program analyzes the values and produces a report indicating the overall water-quality status and parameters of concern

 Add Record

Select 2 to store record in:

text

water_quality_samples.csv



 View Records

Select 3 to view stored records.

 Search by Location

Select 4 and enter a location to view any stored records.

 Analyze Record

Select 5 and enter the ID of a record to analyze that record and produce its report

 Delete Record

Select 6 and enter the ID of a record to delete that record

 Statistics

Select 7 to view basic statistics about stored records.

---

 Testing

The project has included:

text

test_analyzer.py



To run the test:

bash

python test_analyzer.py



The test program runs the analyzer on:

A sample with expected good values

A sample with values out-of-reference

The results display the calculated quality score, status, and parameters of concern.

---

 Data Storage

The project uses:

text

water_quality_samples.csv



as its data-storage file.

Each record stores:

text

id

location

date

pH

tds

turbidity

hardness

nitrate

sulphate

chlorine

temperature



The included sample data is used for testing and demonstration purposes.

---

 Input Validation

The application validates inputs before processing.

Examples:

Reject pH values outside the acceptable pH range

Reject blank or invalid location entries

Reject non-numeric values for numeric parameters

Reject negative values for parameters that should not be negative

Validate date input is in the format YYYY-MM-DD

---

 Non-Functional Requirements

 Usability

The application is menu-driven and is designed to be intuitive and easy to use.

 Reliability

The same analysis procedure is applied to the data entered or read from the file

 Error Handling

Invalid values are not accepted and the user is prompted to re-enter values

 Maintainability

The application is modular with separated functions for distinct sections of the program

---

 Future Enhancements

Potential future enhancements include:

Adding more water-quality parameters

Adding graphical visualization of water-quality data

Adding a database (e.g., SQLite)

Adding downloadable PDF reports

Adding user authentication

Adding more statistical analysis

---

 Project Purpose

This project was created as part of the VITyarthi – Build Your Own Project evaluation to demonstrate the application of Python programming concepts to a practical problem.

