from datetime import date 
import shutil 

def backup(src_file, bkp_file = None, src_file_loc = '', bkp_file_loc = ''):

    #source file name (concat the location of the files) 
    src_file = src_file_loc + src_file

    #fetching today's current day fate
    today = date.today()
    date_format = today.strftime("%d_%b_%Y_")

    #Modified name of the backup File, si no se le da nombre al archivo de seguridad
    if bkp_file is None: 
        bkp_file = src_file
        bkp_file = bkp_file_loc + date_format + bkp_file
    else:
        bkp_file = bkp_file_loc + date_format + bkp_file

    #Create the backup Copy of the src file 
    shutil.copy2(src_file, bkp_file)

    #Success Message 
    print("Backup Successful")
