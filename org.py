import glob
import pandas as pd
import logging
from datetime import datetime
import pyautogui as pg
from Send_Mail import send_email,developer_email
from Utility import init_logs
import os
import share
from Sap_Logon import SapGui
from SFTP import file_to_sftp_server
user_cs_df = pd.DataFrame(columns=['Company Code', 'Cost Object', 'Requester', 'User', 'Level'])
user_wbs_df = pd.DataFrame(columns=['Company Code', 'Cost Object', 'Requester', 'User', 'Level'])
user_pc_df = pd.DataFrame(columns=['Company Code', 'Cost Object', 'Requester', 'User', 'Level'])

columns_COA = ['', 'Client', 'Company code', 'Level', 'User mapping id', 'counter', 'expense type', 'expense type',
               'Cost center', 'wbse', 'profit center']

cols = ['', 'Client', 'Opentext user id', 'Bulk Approval category', 'Last name', 'First name', '',
        'SAP user id', 'Email ID','','']


def format_cs_file(cs_user_data):
    global user_cs_df
    try:
        for i in cs_user_data.columns:
            if i == 'Requester\nUserid':
                cs_user_data.rename(columns={i: 'Requester'}, inplace=True)
            if i == 'Level1\nUserid\n<10k EUR':
                cs_user_data.rename(columns={i: 'Level1_Userid'}, inplace=True)
            if i == 'Level2\nUserid\n10k EUR - 100k EUR':
                cs_user_data.rename(columns={i: 'Level2_Userid'}, inplace=True)
            if i == 'Level3\nUserid\n100k EUR - 1M EUR':
                cs_user_data.rename(columns={i: 'Level3_Userid'}, inplace=True)
            if i == 'Level4\nUserid\n>1M EUR':
                cs_user_data.rename(columns={i: 'Level4_Userid'}, inplace=True)
        
        for i, row in cs_user_data.iterrows():
            if not pd.isna(row['Level1_Userid']):
                df_temp = pd.DataFrame(columns=['Company Code', 'Cost Object', "WBS_or_CostCenter_ProfitCenter", 'Requester', 'User', 'Level'], data=[
                    [row['Company Code'], row['Cost Object'], row['WBS'],row['Requester'], row['Level1_Userid'], 2]])
                user_cs_df = pd.concat([user_cs_df, df_temp], ignore_index=True)
            if not pd.isna(row['Level2_Userid']):
                df_temp = pd.DataFrame(columns=['Company Code', 'Cost Object',"WBS_or_CostCenter_ProfitCenter", 'Requester', 'User', 'Level'], data=[
                    [row['Company Code'], row['Cost Object'],row['WBS'], row['Requester'], row['Level2_Userid'], 3]])
                user_cs_df = pd.concat([user_cs_df, df_temp], ignore_index=True)
            if not pd.isna(row['Level3_Userid']):
                df_temp = pd.DataFrame(columns=['Company Code', 'Cost Object',"WBS_or_CostCenter_ProfitCenter", 'Requester', 'User', 'Level'], data=[
                    [row['Company Code'], row['Cost Object'], row['WBS'],row['Requester'], row['Level3_Userid'], 4]])
                user_cs_df = pd.concat([user_cs_df, df_temp], ignore_index=True)
            if not pd.isna(row['Level4_Userid']):
                df_temp = pd.DataFrame(columns=['Company Code', 'Cost Object',"WBS_or_CostCenter_ProfitCenter", 'Requester', 'User', 'Level'], data=[
                    [row['Company Code'], row['Cost Object'],row['WBS'], row['Requester'], row['Level4_Userid'], 5]])
                user_cs_df = pd.concat([user_cs_df, df_temp], ignore_index=True)
        user_cs_df['Type'] = "Cost Center"
        return user_cs_df
    except Exception as e:
        logging.info(f"Error at Format Cs File:\n{str(e)}")
        developer_email("Error at Format Cs File",f"Error at Format Cs File:\n{str(e)}")


def format_WBS_file(wbs_user_data):
    try:
        for i in wbs_user_data.columns:
            if i == 'Requester\nUserid':
                wbs_user_data.rename(columns={i: 'Requester'}, inplace=True)
            if i == 'Level1\nUserid\n<200k EUR':
                wbs_user_data.rename(columns={i: 'Level1_Userid'}, inplace=True)
            if i == 'Level2\nUserid\n>200k EUR':
                wbs_user_data.rename(columns={i: 'Level2_Userid'}, inplace=True)
        global user_wbs_df
        for i, row in wbs_user_data.iterrows():
            if not pd.isna(row['Level1_Userid']):
                df_temp = pd.DataFrame(columns=['Company Code', 'Cost Object','WBS_or_CostCenter_ProfitCenter', 'Requester', 'User', 'Level'], data=[
                    [row['Company Code'], row['WBS'],row['COST OBJECT'], row['Requester'], row['Level1_Userid'], 4]])
                user_wbs_df = pd.concat([user_wbs_df, df_temp], ignore_index=True)
            if not pd.isna(row['Level2_Userid']):
                df_temp = pd.DataFrame(columns=['Company Code', 'Cost Object','WBS_or_CostCenter_ProfitCenter', 'Requester', 'User', 'Level'], data=[
                    [row['Company Code'], row['WBS'], row['COST OBJECT'],row['Requester'], row['Level2_Userid'], 6]])
                user_wbs_df = pd.concat([user_wbs_df, df_temp], ignore_index=True)
        user_wbs_df['Type'] = "WBS Element"
        return user_wbs_df
    except Exception as e:
        logging.info(f"Error at Format WBS File:\n{str(e)}")
        developer_email("Error at Format WBS File",f"Error at Format WBS File:\n{str(e)}")


def format_pc_file(pc_user_data):
    try:
        for i in pc_user_data.columns:
            if i == 'Requester\nUserid':
                pc_user_data.rename(columns={i: 'Requester'}, inplace=True)
            if i == 'Level1\nUserid\n<10k EUR':
                pc_user_data.rename(columns={i: 'Level1_Userid'}, inplace=True)
            if i == 'Level2\nUserid\n10k EUR - 100k EUR':
                pc_user_data.rename(columns={i: 'Level2_Userid'}, inplace=True)
            if i == 'Level3\nUserid\n100k EUR - 1M EUR':
                pc_user_data.rename(columns={i: 'Level3_Userid'}, inplace=True)
            if i == 'Level4\nUserid\n>1M EUR':
                pc_user_data.rename(columns={i: 'Level4_Userid'}, inplace=True)
        pc_user_data = pc_user_data.filter(items=['Action', 'Company Code', 'Cost Object type', 'Cost Object',
                                                  'Requester', 'Level1_Userid', 'Level2_Userid', 'Level3_Userid',
                                                  'Level4_Userid', 'Remarks'])
        print(pc_user_data.columns)
        global user_pc_df
        for i, row in pc_user_data.iterrows():
            if not pd.isna(row['Level1_Userid']):
                df_temp = pd.DataFrame(columns=['Company Code', 'Cost Object','WBS_or_CostCenter_ProfitCenter', 'Requester', 'User', 'Level'], data=[
                    [row['Company Code'], row['Cost Object'],'', row['Requester'], row['Level1_Userid'], 2]])
                user_pc_df = pd.concat([user_pc_df, df_temp], ignore_index=True)
            if not pd.isna(row['Level2_Userid']):
                df_temp = pd.DataFrame(columns=['Company Code', 'Cost Object','WBS_or_CostCenter_ProfitCenter', 'Requester', 'User', 'Level'], data=[
                    [row['Company Code'], row['Cost Object'],'', row['Requester'], row['Level2_Userid'], 3]])
                user_pc_df = pd.concat([user_pc_df, df_temp], ignore_index=True)
            if not pd.isna(row['Level3_Userid']):
                df_temp = pd.DataFrame(columns=['Company Code', 'Cost Object','WBS_or_CostCenter_ProfitCenter', 'Requester', 'User', 'Level'], data=[
                    [row['Company Code'], row['Cost Object'],'', row['Requester'], row['Level3_Userid'], 4]])
                user_pc_df = pd.concat([user_pc_df, df_temp], ignore_index=True)
            if not pd.isna(row['Level4_Userid']):
                df_temp = pd.DataFrame(columns=['Company Code', 'Cost Object','WBS_or_CostCenter_ProfitCenter', 'Requester', 'User', 'Level'], data=[
                    [row['Company Code'], row['Cost Object'],'', row['Requester'], row['Level4_Userid'], 5]])
                user_pc_df = pd.concat([user_pc_df, df_temp], ignore_index=True)
        user_pc_df['Type'] = "Profit Center"
        return user_pc_df
    except Exception as e:
        logging.info(f"Error at Format PC File:\n{str(e)}")
        developer_email("Error at Format PC File",f"Error at Format PC File:\n{str(e)}")


def validity_df(path):
    try:
        fd = pd.read_excel(path, usecols=['User Name', 'Valid to', 'Lock'], dtype=str)
        for i in fd.index:
            try:
                fd.loc[i,'new']= datetime.strptime(fd.loc[i,'Valid to'], "%d.%m.%Y")
            except Exception as e:
                fd.loc[i,'new']=fd.loc[i,'Valid to']
        for i in fd.index:
            try:
                if (fd.loc[i,'new'] > datetime.now()) and (fd.loc[i,'Lock'] == '0'):
                    fd.loc[i, 'Status'] = True
                else:
                    fd.loc[i, 'Status'] = False
            except Exception as e:
                fd.loc[i,'Status'] = fd.loc[i,'new']
        fd.to_excel("out.xlsx",index=False)
        return fd
    except Exception as e:
        logging.info(str(e))
        developer_email("Error while validity step",f"Error while validity step:\n{str(e)}")


def user_df(path):
    try:
        user_file = pd.read_excel(path, dtype=str)
        print(user_file.head(4).to_string())
        user_file = user_file.filter(
            items=['OpenText User Id', 'Last Name', 'First Name', 'SAP User ID', 'Email Address'])
        return user_file
    except Exception as e:
        logging.info(str(e))
        print(e)


def check_user_validity(data, user):
    if not data[(data['User Name'].str.strip().str.lower() == str(user).lower()) & (data['Status'] == True)].empty:
        return True
    else:
        return False


def find_user_id(data_user, name):
    if not data_user[data_user['SAP User ID'].str.strip().str.lower() == name].empty:
        return "User Present"
    else:
        return "User Not Present"


# def validating_company_CostCenter(data_csks, company_code, cost_center):
#     try:
#         if (not pd.isna(company_code)) and (not pd.isna(cost_center)):
#             if not (data_csks[data_csks['Company Code'].str.strip() == company_code]).empty:
#                 dat = data_csks.loc[(data_csks['Company Code'].str.strip() == company_code) & (
#                         data_csks['Cost Center'].str.strip() == cost_center)]
#                 if not dat.empty:
#                     return "Company Code and Cost Center Present"
#                 else:
#                     return "Error: cost center not found"
#             else:
#                 return "Error: Company Code not found"
#         else:
#             return "Error:One of company code or cost center not provided"
#     except Exception as e:
#         print(e)


def fetch_user_maping_name(id,pat):
    user = pd.read_excel(pat)
    # print('id',id)
    # print(user[user['SAP User ID'].str.strip().str.upper() == id.upper()])
    # map_id = user[user['SAP User ID'].str.strip().str.lower() == id]
    # print(map_id)
    # pg.alert('ll')
    map_id = user[user['SAP User ID'].str.strip().str.lower() == id]['OpenText User Id'].values
    if len(map_id) > 0:
        return map_id[0]
    else:
        return ""





def validating_company_CostCenter(data_csks, data_prps, data_cepc, company_code, cost_center, val):
    logging.info(f"{data_csks, data_prps, data_cepc, company_code, cost_center, val}")
    # cost center part
    cost_center=str(cost_center)
    if val == "Cost Center":
        try:
            if (not pd.isna(company_code)) and (not pd.isna(cost_center)):
                if not (data_csks[data_csks['Company Code'].str.strip() == str(company_code).strip()]).empty:
                    dat = data_csks.loc[(data_csks['Company Code'].str.strip() == str(company_code).strip()) & (
                            data_csks['Cost Center'].str.strip().str.contains(f"{cost_center.strip('*')}"))]
                    if not dat.empty:
                        return "Company Code and Cost Center Present"
                    else:
                        return "Error: cost center not found"
                else:
                    return "Error: Company Code not found"
            else:
                return "Error:One of company code or cost center not provided"
        except Exception as e:
            print(e)
    elif val == "WBS Element":
        try:
            cost_center = ''.join(cost_center.strip().split('-'))
            logging.info(f"{cost_center}")
            logging.info(f"\n{data_prps.head(5).to_string()}")
            if (not pd.isna(company_code)) and (not pd.isna(cost_center)):
                print("checking\n",data_prps[(data_prps['Company Code'].str.strip() == str(company_code).strip())])
                if not data_prps[(data_prps['Company Code'].str.strip() == str(company_code).strip())].empty:
                    dat = data_prps.loc[(data_prps['Company Code'].str.strip() == str(company_code).strip()) & (
                            data_prps['WBS_Element_Without_'].str.strip().str.contains(f"{cost_center.strip('*')}"))]
                    if not dat.empty:
                        return "Company Code and WBS Element Present"
                    else:
                        return "Error: WBS Element not found"
                else:
                    return "Error: Company Code not found"
            else:
                return "Error:One of company code or WBS Element not provided"
        except Exception as e:
            print(e)
    elif val == "Profit Center":
        try:
            if (not pd.isna(company_code)) and (not pd.isna(cost_center)):
                if not data_cepc[(data_cepc['Company Code'].str.strip() == str(company_code).strip())].empty:
                    dat = data_cepc.loc[(data_cepc['Company Code'].str.strip() == str(company_code).strip()) & (
                            data_cepc['Profit Center'].str.strip().str.contains(f"{cost_center.strip('*')}"))]
                    if not dat.empty:
                        return "Company Code and Profit Present"
                    else:
                        return "Error: Profit center not found"
                else:
                    return "Error: Company Code not found"
            else:
                return "Error:One of company code or Profit Center not provided"
        except Exception as e:
            print(e)


def notification_Mail(data, colu):
    unique_mail = data['Requester'].unique()
    for mail in unique_mail:
        if pd.isna(mail):
            df_mail = data[pd.isna(data['Requester'])]
        else:
            df_mail = data[data['Requester'] == mail]
        html_table = df_mail.filter(items=colu).fillna('')
        logging.info(f"html data\n{html_table.to_string()}")
        htmlstyle = "<style>table{border: 1px solid black;border-collapse: collapse;}th{ background-color: " \
                    "cyan;}</style> "
        body1 = "<html>" + htmlstyle + "Hi All, <br><br>Please find the below Table.<br><br>" + "{}".format(
            html_table.to_html(index=False))
        if pd.isna(mail):
            mail_id = "vignesh.r@inter.ikea.com,ramraj.ramraj@inter.ikea.com"
            print('done')
            status = send_email("Test-Error Mail", body1, mail_id)
        else:
            status = send_email("Test-Error Mail", body1, mail)
            print('done1')

def make_df_requester(df_cs_req,df_wbs_req,df_pc_req):
    logging.info(f"df_cs_req data\n{df_cs_req.to_string()}")
    logging.info(f"df_wbs_req data\n{df_wbs_req.to_string()}")
    logging.info(f"df_pc_req data\n{df_pc_req.to_string()}")
    df_requester=pd.DataFrame(columns=columns_COA)
    try:
        for value ,row_req in df_cs_req.iterrows():
            df_concat=pd.DataFrame(columns=columns_COA, data=[['COA', '100', row_req['Company Code'], 1, row_req['Requester\nUserid'], '', 'ST','ST','*','*','*']])
            df_requester=pd.concat([df_requester,df_concat],ignore_index=True)
        for value ,row_req in df_wbs_req.iterrows():
            df_concat=pd.DataFrame(columns=columns_COA, data=[['COA', '100', row_req['Company Code'], 1, row_req['Requester\nUserid'], '', 'ST','ST','*','*','*']])
            df_requester=pd.concat([df_requester,df_concat],ignore_index=True)
        for value ,row_req in df_pc_req.iterrows():
            df_concat=pd.DataFrame(columns=columns_COA, data=[['COA', '100', row_req['Company Code'], 1, row_req['Requester\nUserid'], '', 'ST','ST','*','*','*']])
            df_requester=pd.concat([df_requester,df_concat],ignore_index=True)
        return df_requester,True
    except Exception as e:
        print(e)
        return pd.DataFrame(),False

if __name__ == '__main__':
    init_logs()
    share_obj = share.SharePoint()
    current_date = datetime.today().strftime('%d-%m-%Y %H_%M')
    folder_path_Output = f"Output\\{current_date}"
    os.makedirs(folder_path_Output, exist_ok=True)
    user_data_wbs = pd.DataFrame()
    user_data_cs = pd.DataFrame()
    user_data_pc = pd.DataFrame()
    df_COA = pd.DataFrame(columns=cols)
    df_User_details = pd.DataFrame(columns=columns_COA)
    try:
        with open('Previous_time.txt', 'r') as f:
            time = f.read()
        time_stamp = datetime.strptime(time, "%Y-%m-%d %H:%M:%S")
        print(time_stamp)
        details = share_obj.print_folder_contents(time_stamp, folder_path_Output)
        print(details)
        print(len(details))
    except Exception as e:
        print(e)
        developer_email("Error at reading previous timestamp",f"Error at reading previous timestamp:{str(e)}")
        details = []
    #pg.alert('1')
    try:
        if len(details) > 0:
            sap_Object = SapGui()
            print("after SAPGUI print this")
            sap_Object.get_files(folder_path_Output)
            print("after get files print")
            files = glob.glob(f"{os.getcwd()}\\{folder_path_Output}" + '\\*')
            # files=['C:\\Users\\ANGUP24\\Desktop\\Automations\\VIM\\Output\\25-09-2024 07_21\\File_CEPC_BUKRS.xlsx', 'C:\\Users\\ANGUP24\\Desktop\\Automations\\VIM\\Output\\25-09-2024 07_21\\File_CSKS.xlsx', 'C:\\Users\\ANGUP24\\Desktop\\Automations\\VIM\\Output\\25-09-2024 07_21\\File_PRPS.xlsx', 'C:\\Users\\ANGUP24\\Desktop\\Automations\\VIM\\Output\\25-09-2024 07_21\\File_User.xlsx', 'C:\\Users\\ANGUP24\\Desktop\\Automations\\VIM\\Output\\25-09-2024 07_21\\File_USR02.xlsx', 'C:\\Users\\ANGUP24\\Desktop\\Automations\\VIM\\Output\\25-09-2024 07_21\\Report_CEPC_BUKRS.txt', 'C:\\Users\\ANGUP24\\Desktop\\Automations\\VIM\\Output\\25-09-2024 07_21\\Report_CSKS.txt', 'C:\\Users\\ANGUP24\\Desktop\\Automations\\VIM\\Output\\25-09-2024 07_21\\Report_PRPS.txt', 'C:\\Users\\ANGUP24\\Desktop\\Automations\\VIM\\Output\\25-09-2024 07_21\\Report_User.txt', 'C:\\Users\\ANGUP24\\Desktop\\Automations\\VIM\\Output\\25-09-2024 07_21\\Report_USR02.txt', 'C:\\Users\\ANGUP24\\Desktop\\Automations\\VIM\\Output\\25-09-2024 07_21\\TOA Update Request -new format sample 1 ADD.xlsx']
            logging.info(f"Files:\n{files}")
            path_CSKS = [i for i in files if "File_CSKS.xlsx" in i][0]
            logging.info(f"cost_center_path:{path_CSKS}")
            path_PRPS = [i for i in files if "File_PRPS.xlsx" in i][0]
            logging.info(f"wbs_path:{path_PRPS}")
            path_CEPC = [i for i in files if "File_CEPC_BUKRS.xlsx" in i][0]
            logging.info(f"profit_center_path:{path_CEPC}")
            path_USR02 = [i for i in files if "File_USR02.xlsx" in i][0]
            logging.info(f"USR02:{path_USR02}")
            path_USER = [i for i in files if "File_User.xlsx" in i][0]
            logging.info(f"USER:{path_USER}")
            
            for index, row in details.iterrows():
                print(row['Path'])
                #pg.alert("check path")
                data_wbs = pd.read_excel(row['Path'], sheet_name='WBS TOA', skiprows=[0])
                print(data_wbs)
                #pg.alert('kkk')
                data_cs = pd.read_excel(row['Path'], sheet_name='Cost Center TOA', skiprows=[0])
                data_pc = pd.read_excel(row['Path'], sheet_name='Profit Center TOA', skiprows=[0])
                user_data_wbs = pd.concat([data_wbs, user_data_wbs]).reset_index(drop=True)
                user_data_cs = pd.concat([data_cs, user_data_cs]).reset_index(drop=True)
                user_data_pc = pd.concat(([data_pc, user_data_pc])).reset_index(drop=True)
            logging.info(f"The data of wbs\n{user_data_wbs.to_string()}")
            logging.info(f"The data of Cs\n{user_data_cs.to_string()}")
            logging.info(f"The data of PC\n{user_data_pc.to_string()}")
            #pg.alert("Check user files")

            # sepearting nan and without nan values in requester
            df_user_cs_requester=user_data_cs[~user_data_cs['Requester\nUserid'].isna()]
            user_data_cs=user_data_cs[user_data_cs['Requester\nUserid'].isna()]

            df_user_wbs_requester=user_data_wbs[~user_data_wbs['Requester\nUserid'].isna()]
            user_data_wbs=user_data_wbs[user_data_wbs['Requester\nUserid'].isna()]

            df_user_pc_requester=user_data_pc[~user_data_pc['Requester\nUserid'].isna()]
            user_data_pc=user_data_pc[user_data_pc['Requester\nUserid'].isna()]

            # calling format function for making df in standard form
            df_user_cs = format_cs_file(user_data_cs)
            logging.info(f"The Modified format data of Cs\n{df_user_cs}")
            df_user_wbs = format_WBS_file(user_data_wbs)
            logging.info(f"The Modified format data of wbs\n{df_user_wbs.to_string()}")
            df_user_pc = format_pc_file(user_data_pc)
            logging.info(f"The Modified format data of pc\n{df_user_pc.to_string()}")
            df_Final_User = pd.concat([df_user_cs, df_user_wbs, df_user_pc], ignore_index=True)
            df_Final_User['Company Code']=df_Final_User['Company Code'].apply(lambda x: int(x))
            df_Final_User['Cost Object']=df_Final_User['Cost Object'].apply(lambda x: int(x) if isinstance(x,float) else x)
            logging.info(f"\n{df_Final_User.to_string()}")

            #pg.alert("waiting for final df")
            df_validity = validity_df(path_USR02)
            logging.info(f"The USR02 data\n{df_validity.head(4)}")
            data_user_sap = user_df(path_USER)
            data_csks_ = pd.read_excel(path_CSKS, usecols=['CoCd','Cost Ctr'], dtype=str)
            data_csks_ = data_csks_.rename(columns={'CoCd': 'Company Code', 'Cost Ctr': 'Cost Center'})
            print(data_csks_.head(4))
            data_prps_ = pd.read_excel(path_PRPS, usecols=['CoCd', 'WBS Element'], dtype=str)
            data_prps_=data_prps_.rename(columns={'CoCd': 'Company Code', 'WBS Element': 'WBS Element'})
            print(data_prps_.head(4))
            data_prps_['WBS_Element_Without_'] = data_prps_['WBS Element'].apply(
                lambda a: ''.join(a.split('-')).strip() if not pd.isna(a) else a)
            
            print(data_csks_.head(4))
            data_cepc_ = pd.read_excel(path_CEPC, usecols=['CoCd', 'Profit Ctr'], dtype=str)
            data_cepc_=data_cepc_.rename(columns={'CoCd': 'Company Code', 'Profit Ctr': 'Profit Center'})
            print(data_cepc_.head(4))
            try:
                if not df_Final_User.empty:
                    df_Final_User['Status_User_Validity'] = df_Final_User['User'].str.strip().apply(
                        lambda a: check_user_validity(df_validity, a))
                    logging.info(f"After 1st validation:\n{df_Final_User.to_string()}")
                    #pg.alert("After 1st validation")
                    df_Final_User['Check_User'] = df_Final_User['User'].str.strip().apply(lambda a: find_user_id(data_user_sap, str(a).lower()))
                    logging.info(f"After 2st validation:\n{df_Final_User.to_string()}")
                    #pg.alert("After 2st validation")
                    for id_final, row_final in df_Final_User.iterrows():
                        com_code, cost_code, val_type = row_final['Company Code'], row_final['Cost Object'], row_final[
                            'Type']
                        status1 = validating_company_CostCenter(data_csks_, data_prps_, data_cepc_, com_code, cost_code,
                                                                val_type)
                        df_Final_User.loc[id_final, "Validating_table_data"] = status1
                    logging.info(f"After 3st validation:\n{df_Final_User.to_string()}")
                    #pg.alert("After 3st validation")
                    # sep
                    df_false = df_Final_User[df_Final_User['Status_User_Validity'] == False]
                    logging.info(f"data false for sending mail \n {df_false.to_string()}")
                    notification_Mail(df_false,
                                      ['Company Code', 'Cost Object', 'Requester', 'User', 'Level',
                                       'Status_User_Validity'])
                    ids_false = df_false.index.tolist()
                    df_Final_User.loc[ids_false, ['Validation_Status', 'Mail_Status']] = ['Validation Error',
                                                                                          'Sent Mail']
                    logging.info(f"checking final\n{df_Final_User.to_string()}")
                    #pg.alert("final")
                    df_not_found = df_Final_User[(df_Final_User['Status_User_Validity'] == True) &
                                                 (df_Final_User['Check_User'] == "User Not Present")]
                    logging.info(f"df_not_found\n{df_not_found.to_string()}")
                    df_found = df_Final_User[(df_Final_User['Status_User_Validity'] == True) &
                                             (df_Final_User['Check_User'] == "User Present")]
                    logging.info(f"df_found\n{df_found.to_string()}")
                    #pg.alert('check1')
                    if not df_not_found.empty:
                        df_add_cs = user_data_cs.filter(items=['Userid', 'Email', '1st name', 'last name'])
                        df_add_wbs = user_data_wbs.filter(items=['Userid', 'Email', '1st name', 'last name'])
                        df_add_pc = user_data_pc.filter(items=['Userid', 'Email', '1st name', 'last name'])
                        ls_stat_not_found = []
                        for id_not_found, row_not_found in df_not_found.iterrows():
                            type_value = row_not_found['Type']
                            user_value = row_not_found['User']
                            if type_value == "Cost Center":
                                data_list = df_add_cs[df_add_cs['Userid'] == user_value].values
                            elif type_value == "WBS Element":
                                data_list = df_add_wbs[df_add_wbs['Userid'] == user_value].values
                            elif type_value == "Profit Center":
                                data_list = df_add_pc[df_add_pc['Userid'] == user_value].values
                            else:
                                data_list = []
                            if len(data_list) > 0:
                                user_id, mail_, first_name, last_name = data_list[0][0], data_list[0][1], data_list[0][
                                    2], \
                                    data_list[0][3]
                                if (not pd.isna(user_id) and
                                        not pd.isna(first_name) and
                                        not pd.isna(last_name) and
                                        not pd.isna(mail_)):
                                    df_temp_coa = pd.DataFrame(columns=cols, data=[
                                        ["USR", 100, '', "B", last_name, first_name, '', user_id, mail_,'','']])
                                    logging.info(f"The new data\n{df_temp_coa.to_string()}")
                                    df_COA = pd.concat([df_COA, df_temp_coa], ignore_index=True)
                                    ls_stat_not_found.append(f"User:{user_value} added in User Details")
                                    df_not_found.loc[
                                        id_not_found, 'Validation_Status'] = f"User:{user_value} added in User Details"
                                    logging.info(f"Added in User Details")
                                else:
                                    ls_stat_not_found.append(
                                        f"Details not provide for this user: {user_value} in {type_value} Sheet")
                                    df_not_found.loc[
                                        id_not_found, 'Validation_Status'] = f"Details not provide for this user: {user_value} in {type_value} Sheet"
                                    logging.info(
                                        f"Details not provide for this user: {user_value} in {type_value} Sheet")
                            else:
                                df_not_found.loc[
                                    id_not_found, 'Validation_Status'] = f"User not find {user_value} in {type_value} Sheet"
                                ls_stat_not_found.append(f"User not find {user_value} in {type_value} Sheet")
                                logging.info(f"User not find {user_value} in {type_value} Sheet")

                        index_not_found = df_not_found.index.tolist()
                        print(index_not_found)
                        df_Final_User.loc[index_not_found, 'Validation_Status'] = ls_stat_not_found
                        logging.info(f"df_found\n{df_found.to_string()}")
                        notification_Mail(df_not_found,
                                          ['Company Code', 'Cost Object', 'Requester', 'User', 'Level',
                                           'Check_User', 'Validation_Status'])
                        df_Final_User.loc[index_not_found, 'Mail_Status'] = 'Sent Mail'
                        logging.info(f"checking final\n{df_Final_User.to_string()}")
                        df_requester,status_req=make_df_requester(df_user_cs_requester,df_user_wbs_requester,df_user_pc_requester)
                        if status_req:
                            for idx_no_error, row_x in df_requester.iterrows():
                                    print(row_x['User mapping id'].lower())
                                    df_requester.loc[idx_no_error,'User mapping id'] = fetch_user_maping_name(row_x['User mapping id'].lower(),path_USER)
                            df_COA=pd.concat([df_COA,df_requester],ignore_index=True)
                        else:
                            pass
                            # send mail
                        df_COA.to_excel(f"{folder_path_Output}\\User Details.xlsx", index=False)
                        #pg.alert("after adding in new df")
                    if not df_found.empty:
                        df_found_without_error = df_found[~df_found['Validating_table_data'].str.contains('Error')]
                        df_found_with_error = df_found[df_found['Validating_table_data'].str.contains('Error')]
                        if not df_found_with_error.empty:
                            notification_Mail(df_found_with_error,
                                              ['Company Code', 'Cost Object', 'Requester', 'User', 'Level',
                                               'Check_User', 'Validating_table_data'])
                            df_Final_User.loc[df_found_with_error.index.tolist(), 'Mail_Status'] = 'Sent Mail'
                        if not df_found_without_error.empty:
                            logging.info(f"df_found_without_error\n{df_found_without_error.to_string()}")
                            #pg.alert('fdff')
                            for idx_no_error, row_x in df_found_without_error.iterrows():
                                map_id = fetch_user_maping_name(row_x['User'].lower(),path_USER)
                                print(row_x['Cost Object'])
                                if row_x['Type'] == "Cost Center":
                                    df_User_details = pd.concat(
                                        [df_User_details, pd.DataFrame(columns=columns_COA, data=[
                                            ['COA', '100', row_x['Company Code'], row_x['Level'], map_id, '', 'ST',
                                             'ST',
                                             row_x['Cost Object'],
                                             row_x['WBS_or_CostCenter_ProfitCenter'],
                                             '']])], ignore_index=True)

                                    df_found_without_error.loc[idx_no_error, 'Validation_Status'] = "Added in COA file"
                                elif row_x['Type'] == "WBS Element":
                                    df_User_details = pd.concat(
                                        [df_User_details, pd.DataFrame(columns=columns_COA, data=[
                                            ['COA', '100', row_x['Company Code'], row_x['Level'], map_id, '', 'ST',
                                             'ST',
                                             row_x['WBS_or_CostCenter_ProfitCenter'],
                                             row_x['Cost Object'],
                                             '']])], ignore_index=True)
                                    df_found_without_error.loc[idx_no_error, 'Validation_Status'] = "Added in COA file"

                                elif row_x['Type'] == "Profit Center":
                                    df_User_details = pd.concat(
                                        [df_User_details, pd.DataFrame(columns=columns_COA, data=[
                                            ['COA', '100', row_x['Company Code'], row_x['Level'], map_id, '', 'ST',
                                             'ST',
                                             '',
                                             '',
                                             row_x['Cost Object']]])], ignore_index=True)
                                    df_found_without_error.loc[idx_no_error, 'Validation_Status'] = "Added in COA file"

                            notification_Mail(df_found_without_error,
                                              ['Company Code', 'Cost Object', 'Requester', 'User', 'Level',
                                               'Check_User', 'Validating_table_data', 'Validation_Status'])
                            df_requester,status_req=make_df_requester(df_user_cs_requester,df_user_wbs_requester,df_user_pc_requester)
                            print(df_requester)
                            #pg.alert('at df_req')
                            if status_req:
                                for idx_no_error, row_x in df_requester.iterrows():
                                    print(row_x['User mapping id'])
                                    df_requester.loc[idx_no_error,'User mapping id'] = fetch_user_maping_name(row_x['User mapping id'].lower(),path_USER)
                                print("before line 564")
                                df_User_details=pd.concat([df_User_details,df_requester],ignore_index=True)
                                print("after line 565")
                            else:
                                pass
                                # send mail
                            html_table1 = df_User_details.copy()
                            html_table1 = html_table1.fillna('')
                            htmlstyle = "<style>table{border: 1px solid black;border-collapse: collapse;}th{ background-color: " \
                                        "cyan;}</style> "     
                            body2 = "<html>" + htmlstyle + "Hi All, <br><br>Please find the below Table.<br><br>" + "{}".format(
                                    html_table1.to_html(index=False))   

                            mail_id = "vignesh.r@inter.ikea.com,ramraj.ramraj@inter.ikea.com"
                            status = send_email("Output COA file data", body2, mail_id)
                            df_User_details.to_csv(f"{folder_path_Output}\\OutPut_COA.csv", index=False)
                            df_Final_User.loc[
                                df_found_without_error.index.tolist(), ['Validation_Status', 'Mail_Status']] = [
                                "Added in COA file", 'Sent Mail']
                    df_Final_User.fillna('', inplace=True)
                    df_Final_User.to_excel(f"{folder_path_Output}\\Final_Status.xlsx", index=False)
                    logging.info("Done at making Final_Status file ")
                else:
                    print("No data")
                # pg.alert("Check files")
                current_date = datetime.now().strftime('%m%d%Y')
                file_name=f"{folder_path_Output}\\OPT_COA_FILE{current_date}.csv"
                if (not df_COA.empty ) and (not df_User_details.empty):
                    df_User_details.columns=df_COA.columns
                    df_COA.loc[len(df_COA)-1]=''
                    df_COA=pd.concat([df_COA,df_User_details],ignore_index=True)
                    df_COA.fillna('',inplace=True)
                    df_COA.to_csv(file_name,index=False,header=False)
                    file_to_sftp_server(file_name)
                elif not df_User_details.empty:
                    df_User_details.fillna('',inplace=True)
                    df_User_details.to_csv(file_name,index=False,header=False)
                    
                    file_to_sftp_server(file_name)
                elif not df_COA.empty:
                    df_COA.fillna('',inplace=True)
                    df_COA.to_csv(file_name,index=False,header=False)
                    file_to_sftp_server(file_name)
                with open('Previous_time.txt','w') as f:
                    f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            except Exception as e:
                print(e)
                logging.info(str(e))
                developer_email("Error while performing different validation levels",f"Error while performing different validation levels:\n{str(e)}")
        else:
            developer_email("VIM TOA : No new files found in sharepoint",f"No new files found in sharepoint with insertion date after previous timestamp:{str(time_stamp)}")
    except Exception as e:
        print(e)
        logging.info(str(e))
        developer_email("Error while performing main",f"Error while performing main:\n{str(e)}")

    