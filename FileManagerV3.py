import os
import shutil
import string

src_path = r'C:\Users\chris\Downloads'
dstPDF_path = r'C:\Users\chris\Downloads\PDF-folder'
dstFILES_path = r'C:\Users\chris\Downloads\FILES-folder'
dstIMAGE_path = r'C:\Users\chris\Downloads\IMAGE-folder'
dstMUSIC_path = r'C:\Users\chris\Downloads\MUSIC-folder'
dstVIDEO_path = r'C:\Users\chris\Downloads\VIDEO-folder'
dstEXE_path = r'C:\Users\chris\Downloads\EXE-folder'
dstFOLDER_path = r'C:\Users\chris\Downloads\FOLDER-folder'


counterPDF = 0
counterFILES = 0
counterIMAGE = 0
counterMUSIC = 0
counterVIDEO = 0
counterEXE = 0
counterFOLDER = 0
counterTOTAL = 0

for file in os.listdir(src_path):
    counterTOTAL += 1
    if file.endswith(".pdf"):
        counterPDF += 1
        shutil.move(src_path + str("/" + os.path.basename(file)), dstPDF_path)
    elif    file.endswith(".pptx") or \
            file.endswith(".doc") or \
            file.endswith(".docx") or \
            file.endswith(".xls") or \
            file.endswith(".xlsx"):
        counterFILES += 1
        shutil.move(src_path + str("/" + os.path.basename(file)), dstFILES_path)
    elif file.endswith(".jpg") or file.endswith(".png"):
        counterIMAGE += 1
        shutil.move(src_path + str("/" + os.path.basename(file)), dstIMAGE_path)
    elif file.endswith(".mp3"):
        counterMUSIC += 1
        shutil.move(src_path + str("/" + os.path.basename(file)), dstMUSIC_path)
    elif file.endswith(".webm"):
        counterVIDEO
        shutil.move(src_path + str("/" + os.path.basename(file)), dstVIDEO_path)
    elif file.endswith(".exe"):
        counterEXE += 1
        shutil.move(src_path + str("/" + os.path.basename(file)), dstEXE_path)
    elif file.endswith(".zip"):
        counterFOLDER
        shutil.move(src_path + str("/" + os.path.basename(file)), dstFOLDER_path)


print("RESULTS 101")

print(f"We have {counterPDF} PDF-files in this list")
print(f"We have {counterFILES} PPTX-files in this list")
print(f"We have {counterIMAGE} JPG-files in this list")
print(f"We have {counterMUSIC} PNG-files in this list")
print(f"We have {counterVIDEO} PNG-files in this list")
print(f"We have {counterEXE} PNG-files in this list")
print(f"We have {counterFOLDER} PNG-files in this list")


print(f"We have {counterTOTAL} files in this list")

















# Hieronder probeer ik een specifieke file (met file name + fily type) te moven naar andere folder en dit werkt. Hierboven probeer ik dus in mijn Shutil.move-method de string variable van elke filename over te nemen.
print("")
print("Let's try to move a specific item with name:")

#try:
#   shutil.move(src_path + "/1-converted.pdf", dstPDF_path)
#xcept:
#   print("No file available")




# copy
# src_path = r'C:\Users\chris\Downloads\folder_tester'
# dstPDF_path = r'C:\Users\chris\Downloads\folder_tester\PDF-folder'
# dstPPTX_path = r'C:\Users\chris\Downloads\folder_tester\PPTX-folder'
# dstJPG_path = r'C:\Users\chris\Downloads\folder_tester\JPG-folder'


# How to open files in Pyhton: Import OS --> os.system(r, ""file path"")
# os.system(r'C:\Users\chris\PycharmProjects\File_Automation_Manager\Aanslagbiljet.pdf')
# os.system(r'C:\Users\chris\Downloads\drankjeeen.jpg')


# download_folder = os.system('C:\Users\chris\Downloads\folder_tester', 'r')
# download_folder = "folder_tester"


# folder_Image = "C:\Users\chris\Downloads\folder_Image"
# folder_File = "C:\Users\chris\Downloads\folder_File"
# folder_Video = "C:\Users\chris\Downloads\folder_Video"
# folder_Music = "C:\Users\chris\Downloads\folder_Music"
# folder_Folder = "C:\Users\chris\Downloads\folder_Folder"
