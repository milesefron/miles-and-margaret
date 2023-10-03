import os


targets = ['disappointing', 'great', 'awesome']

data_directory = './data'
file_listing = os.listdir(data_directory)

for file in file_listing:
    if('.txt' in file):
        f = open(data_directory + '/' + file)
        text = f.read()

#convert text to lowercase
        text = text.lower()

        sentences = text.split('.')
        for sentence in sentences:
            for target in targets:
                if target in sentence:
                    print(target + ":: " + sentence)

        f.close()
