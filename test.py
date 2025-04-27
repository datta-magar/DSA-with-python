import os
import glob
import pandas as pd
import logging
from datetime import datetime
from Send_Mail import send_email, developer_email
from Utility import init_logs
from Sap_Logon import SapGui
from SFTP import file_to_sftp_server
import share

# Constants and Configurations
LOGGING_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
OUTPUT_FOLDER_TEMPLATE = "Output/{current_date}"
COLUMNS_COA = ['', 'Client', 'Company code', 'Level', 'User mapping id', 'counter',
               'expense type', 'expense type', 'Cost center', 'wbse', 'profit center']
COLUMNS_USER_DETAILS = ['OpenText User Id', 'Last Name', 'First Name', 'SAP User ID', 'Email Address']
DEVELOPER_EMAIL = "developer@example.com"
SHAREPOINT_EMAIL_LIST = "vignesh.r@inter.ikea.com,ramraj.ramraj@inter.ikea.com"

# Logging Setup
def setup_logging():
    """Initializes logging configuration."""
    logging.basicConfig(filename='app.log', level=logging.INFO, format=LOGGING_FORMAT)

# Utility Functions
def handle_exception(func):
    """Decorator for error handling and logging exceptions."""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logging.error(f"Error in {func.__name__}: {e}")
            developer_email(f"Error in {func.__name__}", str(e))
            return None
    return wrapper

@handle_exception
def format_user_data(data, column_mappings, user_type):
    """
    Formats user data into a standardized format for validation.

    Args:
        data (DataFrame): Raw data to be formatted.
        column_mappings (dict): Mapping of old column names to new ones.
        user_type (str): The type of data being formatted (e.g., "Cost Center").

    Returns:
        DataFrame: A formatted DataFrame.
    """
    formatted_rows = []
    data.rename(columns=column_mappings, inplace=True)
    
    for _, row in data.iterrows():
        for level in ['Level1_Userid', 'Level2_Userid', 'Level3_Userid', 'Level4_Userid']:
            if not pd.isna(row.get(level)):
                formatted_rows.append({
                    'Company Code': row['Company Code'],
                    'Cost Object': row['Cost Object'],
                    'WBS_or_CostCenter_ProfitCenter': row.get('WBS', ''),
                    'Requester': row['Requester'],
                    'User': row[level],
                    'Level': int(level[-1]),
                    'Type': user_type
                })
    return pd.DataFrame(formatted_rows)

@handle_exception
def validate_user(data, user):
    """
    Validates whether a user is active and valid.

    Args:
        data (DataFrame): DataFrame containing user validity information.
        user (str): User ID to validate.

    Returns:
        bool: True if the user is valid, False otherwise.
    """
    return not data[(data['User Name'].str.strip().str.lower() == user.lower()) & (data['Status'] == True)].empty

@handle_exception
def validate_cost_center(data_csks, company_code, cost_center):
    """
    Validates the existence of a cost center for a company.

    Args:
        data_csks (DataFrame): DataFrame containing cost center information.
        company_code (str): Company code to validate.
        cost_center (str): Cost center to validate.

    Returns:
        str: Validation status message.
    """
    if pd.isna(company_code) or pd.isna(cost_center):
        return "Error: One of company code or cost center not provided"
    if data_csks[data_csks['Company Code'].str.strip() == company_code].empty:
        return "Error: Company Code not found"
    if data_csks[(data_csks['Company Code'].str.strip() == company_code) &
                 (data_csks['Cost Center'].str.strip().str.contains(cost_center.strip('*')))].empty:
        return "Error: cost center not found"
    return "Company Code and Cost Center Present"

@handle_exception
def process_sharepoint_files(share_obj, folder_path):
    """
    Retrieves and processes files from SharePoint.

    Args:
        share_obj (SharePoint): SharePoint object for file retrieval.
        folder_path (str): Path to store downloaded files.

    Returns:
        list: List of file details retrieved from SharePoint.
    """
    try:
        with open('Previous_time.txt', 'r') as f:
            previous_timestamp = f.read()
        time_stamp = datetime.strptime(previous_timestamp, "%Y-%m-%d %H:%M:%S")
        return share_obj.print_folder_contents(time_stamp, folder_path)
    except Exception as e:
        logging.error(f"Error reading previous timestamp: {e}")
        developer_email("Error at reading previous timestamp", str(e))
        return []

@handle_exception
def validity_df(path):
    """
    Validates user data based on expiration date and lock status.

    Args:
        path (str): Path to the file containing user validity information.

    Returns:
        DataFrame: Validated user information.
    """
    fd = pd.read_excel(path, usecols=['User Name', 'Valid to', 'Lock'], dtype=str)
    fd['new'] = pd.to_datetime(fd['Valid to'], errors='coerce', format="%d.%m.%Y")
    fd['Status'] = fd.apply(
        lambda x: True if (x['new'] > datetime.now()) and (x['Lock'] == '0') else False, axis=1
    )
    fd.to_excel("out.xlsx", index=False)
    return fd

# Main Script Logic
if __name__ == '__main__':
    setup_logging()
    logging.info("Script started")

    # Initialize SharePoint object and create output folder
    share_obj = share.SharePoint()
    current_date = datetime.today().strftime('%d-%m-%Y_%H_%M')
    folder_path = OUTPUT_FOLDER_TEMPLATE.format(current_date=current_date)
    os.makedirs(folder_path, exist_ok=True)

    # Process SharePoint files
    file_details = process_sharepoint_files(share_obj, folder_path)
    if not file_details:
        logging.info("No new files found in SharePoint.")
        developer_email("No new files found", "No new files found in SharePoint after the last timestamp.")
        exit()

    # Further processing logic here...