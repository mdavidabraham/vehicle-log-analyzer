# Vehicle Log Analyzer

A Python command-line tool that reads simulated vehicle logs, displays errors
and warnings with line numbers, and summarizes their counts.

## Features

- Finds ERROR and WARNING entries regardless of capitalization.
- Displays matching entries with their line numbers.
- Prints a count for each category.
- Handles missing files with a readable message.

## How to run

Requires Python 3. No additional packages are needed.

Open a terminal in the "Log analyzer" folder, then run:

```bash
python log_analyzer.py vehicles.log
```

If no filename is provided, the script uses vehicles.log by default.

## Sample data

The included vehicles.log contains 100 simulated entries.

Expected summary:

```text
Summary:
ERROR lines: 20
WARNING lines: 15
```

All sample data is synthetic and contains no employer or customer information.

## Current limitations

Only the first ERROR or WARNING match on each line is counted.
These words are matched anywhere in the line, rather than in a dedicated
log-level field.

## About this project

Built with AI assistance as part of my Python learning.
I am practicing file handling, regular expressions, command-line arguments,
and Git version control.