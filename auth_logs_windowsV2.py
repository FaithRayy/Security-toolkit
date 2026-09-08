import subprocess
import os
import sys
import re

# Returns PowerShell command for a given quanitiy of logs
def log_num(numLogs, path):
    ps_command = (
        f"Get-WinEvent -FilterHashtable @{{"
        f"LogName='Security'; Id=4624,4625"
        f"}} -MaxEvents {numLogs} | Select-Object TimeCreated, Id, Message "
        f"| Out-GridView -Title 'Security Logs (Last {numLogs} logs)' -PassThru "
        f"| Export-Csv -Path '{path}' -NoTypeInformation"
    )
    return ps_command

# Returns PowerShell command for logs within the last given hours
def log_hours(hours, path):
    ps_command = (
        f"Get-WinEvent -FilterHashtable @{{ "
        f"LogName='Security'; StartTime=(Get-Date).AddHours(-{hours[:-1]}); Id=4624,4625"
        f"}} | Select-Object TimeCreated, Id, Message "
        f"| Out-GridView -Title 'Security Logs (Last {hours[:-1]} hours(s))' -PassThru "
        f"| Export-Csv -Path '{path}' -NoTypeInformation"
    )
    return ps_command

# Returns PowerShell command for logs within the given timeframe
def log_date(timeframe, path):
    fromDate, toDate = timeframe.split("-")

    # Adjust formatting to align with Get-WinEvent
    fromDate = fromDate.replace("/", "-")
    fromDate += " 00:00:00"
    toDate = toDate.replace("/", "-")
    toDate += " 23:59:59"

    ps_command = (
         f"Get-WinEvent -FilterHashtable @{{ "
         f"LogName='Security'; StartTime=[datetime]'{fromDate}'; EndTime=[datetime]'{toDate}'; Id=4624,4625"
         f"}} | Select-Object TimeCreated, Id, Message "
         f"| Out-GridView -Title 'Security Logs (From {fromDate} to {toDate})' -PassThru "
         f"| Export-Csv -Path '{path}' -NoTypeInformation"     
    )

    return ps_command

def main(log_parem, type):
    # Create csv file in the same directory as program
    cwd = os.getcwd()
    file_name = f"Security_Logs_{log_parem.replace("/", "")}.csv"
    path = os.path.join(cwd, file_name)

    # Powershell command
    ps_command = None

    # if given <num> or <num>h or <YYYY/MM/DD>-<YYYY/MM/DD>
    if type == 1:
        ps_command = log_num(log_parem, path)
    if type == 2:
        ps_command = log_hours(log_parem, path)
    if type == 3:
        ps_command = log_date(log_parem, path)

    # Nest the call using Start-Process and  -Verb RunAs to trigger the UAC prompt
    elevation_command = f'Start-process powershell -ArgumentList "-NoProfile -Command {ps_command}" -Verb RunAs'

    try :
        # Execute the command via Python's subprocess
        subprocess.run(["powershell", "-NoProfile", "-Command", elevation_command], check=True, capture_output=True, text=True)
        print("Successful!")
    except subprocess.CalledProcessError as e:
        print(f"Failed to exceute command or user denied UAC prompt: {e}")

if __name__ == "__main__":
    args = sys.argv
    log_type = None

    # Can only pass 1 argument
    if(len(args) != 2):
        raise Exception("Error: Can only pass one input. No spaces.")

    log_parem = args[1]

    # if num or [num]h or YYYY/MM/DD-YYYY/MM/DD
    if re.match(r"\d{1,3}$", log_parem):
        log_type = 1
    elif re.match(r"\d{1,3}h$", log_parem):
            log_type = 2
    elif re.match(r"\d{4}/\d{2}/\d{2}-\d{4}/\d{2}/\d{2}$", log_parem):
            log_type = 3
    else:
        raise Exception("Error: You need to pass number of logs<num>, or recent hours <num>h , or two dates of 'from' and 'to' seperated by '-' <YYYY/MM/DD>-<YYYY/MM/DD>")

    main(log_parem, log_type)

