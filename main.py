def read_file_content(txtFile):
    txtFile = open(txtFile, "r")
    txtFile = txtFile.read()

    return txtFile

def count_words():
    text = read_file_content("./story.txt").lower()
    count_words = {}
    for words in text.split():

        if words in count_words:
            count_words[words] +=1 
        else:
            count_words[words] = 1
    return count_words
print(count_words())