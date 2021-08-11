
import os
import glob 



dirpath = "../training/yolo/data/images"


#text files
text_files = [f for f in os.listdir(dirpath) if f.endswith('.TXT')]
#image files
image_files = [f for f in os.listdir(dirpath) if f.endswith('.JPG')]

images_dir = "../train/images"
labels_dir = "../train/labels"


# Create new directories
os.mkdir(images_dir)
os.mkdir(labels_dir)


# Move image files to image directory
for file in image_files:
    os.rename(dirpath + "/" + file, images_dir + "/" + file)


# Move text files to text directory
for file in text_files:
    os.rename(dirpath + "/" + file, labels_dir + "/" + file)


def find_decimal(test_str):
    index_list = [i for i, ltr in enumerate(test_str) if ltr == '.']
    return index_list[-1]



def process_text_files(dir_filepath):
    text_file_paths = glob.glob(dir_filepath + "/*") 
    
    #For each file in the directory, fix the format
    for filepath in text_file_paths:
        file = open(filepath, 'r')
        data = file.readlines()
        for i, line in enumerate(data):
            index = find_decimal(line)
            data[i] = line[:index-1] + ' ' + line[index-1:]
        file = open(filepath, 'w')
        file.writelines(data)
            
        file.close()


process_text_files(path_2)

