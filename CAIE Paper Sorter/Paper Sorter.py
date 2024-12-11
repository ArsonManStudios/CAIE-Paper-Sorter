import os
import shutil

pdf_filenames = []
code_pdfs = []
syll_codes = []
years = []
p_files = {'P1' : [],
           'P2' : [],
           'P3' : [],
           'P4' : [],
           'P5' : [],
           'P6' : [],
           'P7' : [],
           'P8' : [],
           'P9' : []}

# Syllabus Code: [:4]
# Summer/Winter: [5]
#          Year: [6:8]
#    Paper Type: [9:11]
#         Paper: [12]

# Input Path
orig_dir = input('Enter path to folder (Use / instead of \\): ')
if not os.path.isdir(orig_dir):
    raise Exception('Path not found')

escape_chars = ['\'','\"','\\','\n','\r','\t','\b','\f']
for char in escape_chars:
    if char in orig_dir:
        raise Exception('Path contains \\ character')

# Search for PDF's
for file in os.listdir(orig_dir):
    try:
        if (file[-4:] == '.pdf') and (file[:4].isnumeric()) and (file[5] in 'sw')  and (file[6:8].isnumeric()):
            pdf_filenames.append(file)
    except:
        pass

# Syllabus Codes
for file in pdf_filenames:
    code = file[:4]
    if code not in syll_codes:
        syll_codes.append(code)

# Syllabus Codes:
#   Make Directory for Code:
#       Check what Paper Types exist
#       Paper Type Sorting:
#           Create Year Directories
#           Year Sorting

for code in syll_codes:
    code_pdfs = []
    years = []
    new_dir = orig_dir+'/'+code
    p_files = {'P1' : [],
               'P2' : [],
               'P3' : [],
               'P4' : [],
               'P5' : [],
               'P6' : [],
               'P7' : [],
               'P8' : [],
               'P9' : []}
    paper_type = 1
    os.mkdir(new_dir)
    for file in pdf_filenames:
        if file[:4] == code:
            shutil.move(orig_dir+'/'+file, new_dir)
            code_pdfs.append(file)
    for file in code_pdfs:
        paper_type = file[12]
        if paper_type == '0':
            paper_type = file[13]
        p_files['P'+paper_type].append(file)
    for paper in p_files:
        if p_files[paper] != []:
            new_dir = orig_dir+'/'+code+'/'+paper
            os.mkdir(new_dir)
            for file in p_files[paper]:
                shutil.move(orig_dir+'/'+code+'/'+file, new_dir)
                year = file[6:8]
                if year not in years:
                    years.append(year)
            for year in years:
                new_dir = orig_dir+'/'+code+'/'+paper+'/20'+year
                os.mkdir(new_dir)
            for file in p_files[paper]:
                year = file[6:8]
                shutil.move(orig_dir+'/'+code+'/'+paper+'/'+file, orig_dir+'/'+code+'/'+paper+'/20'+year)