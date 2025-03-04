import chardet

with open(r"C:\Users\JAEYEON\Documents\GitHub\bjprogram\downloaded_files\muscleguards_20250304_324_c1c.csv", 'rb') as file:
    result = chardet.detect(file.read())
    print(result)