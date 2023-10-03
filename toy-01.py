import os


data_directory = './data'
file_listing = os.listdir(data_directory)

for file in file_listing:
    if('.txt' in file):
        f = open(data_directory + '/' + file)
        text = f.read()
        f.close()
        print(text)