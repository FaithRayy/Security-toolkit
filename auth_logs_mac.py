import subprocess
import os
import sys
import re
from datetime import date
import json
import pandas as pd


def main(log_parem):

    # Command to receive the logs within the last {log_parem} hours
    getLogCommand = subprocess.run(
        ["log", "show", 
        "--predicate", 'eventMessage contains "Failed to authenticate user" OR eventMessage contains "authSuccess"',
        "--last", log_parem,
        "--style", "json"
        ], 
        capture_output=True, text=True
    )

    # Create an xlsx file with a path to the same directory as the script
    cwd = os.getcwd()
    file = f"log_sheet({date.today()})({log_parem}).xlsx"
    file_path = os.path.join(cwd, file)

    try:
        log_entries = json.loads(getLogCommand.stdout)

        # Retrieve data sheet
        df1 = pd.DataFrame(log_entries)
        # Remove certain redundant columns from excel sheet
        df_cleaned = df1.drop(columns=["timezoneName", "source", "formatString", "backtrace"])

        df_cleaned.to_excel(file_path)

    except json.JSONDecodeError:
        print("Failed to parse log output. Ensure you are running this on macOS.")

if __name__ == "__main__":
    args = sys.argv

    # Can only pass 1 argument
    if (len(args) != 2):
        raise Exception("Error: Needs a time window(hour): <num>h")

    log_parem = args[1]

    # You can only pass an hour windows of 1 to 3 digits
    if not re.match("\\d{1,3}h", log_parem):
        raise Exception("Error: You can only filter an hour time window of 3 digits at most: <num>h")                                    
            
    main(log_parem)
