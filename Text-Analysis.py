'''
Project 4 - Text Analysis - Spring 2021 
Author: Matthias Cannon and matthiasc

Text Analysis

I have neither given or received unauthorized assistance on this assignment.
Signed: Matthias Cannon
'''

def read_text(inFile):
    string = ''
    with open(inFile, 'r') as file:
            string += file.read()
    return string


def clean_text(rawText):
    lowercase = rawText.lower()
    letterList = list(lowercase)
    symbols = ',;:.?![]*()-\'\"'
    for i in range(len(letterList)):
        if letterList[i] in symbols:
            letterList[i] = ''
    returnString = ''.join(letterList)
    return returnString

def get_word_frequencies(wordList):
    dictionary = {}
    for word in wordList:
        if word in dictionary.keys():
            dictionary[word] += 1
        else:
            dictionary[word] = 1
    return dictionary
    
def count_syllables(word):
    ''' Estimates and returns the number of syllables in
    the specified word. '''
    syllables = 0
    vowels = 'aeiouy'
    word = word.lower().strip(".:;?!")
    if word[0] in vowels:
        syllables += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index-1] not in vowels:
            syllables += 1
    if word.endswith('e'):
        syllables -= 1
    if word.endswith('le'):
        syllables += 1
    if syllables == 0: 
        syllables = 1
    return syllables

def count_all_syllables(wordList):
    total = 0
    for word in wordList:
        total += count_syllables(word)
    return total

def main():
    
    print('Welcome to the Text Analyzer!')
    fileName = input('Name of file to analyze? ')
    print()
    read = read_text('dream_speech.txt')
    clean = clean_text(read)
    wordList = clean.split()
    dictionary = get_word_frequencies(wordList)
    totalSyllables = count_all_syllables(wordList)
    numSentences = read.count('!') + read.count('.') + read.count('?')
    numWords = len(wordList)
    numUniqueWords = len(dictionary.keys())
    avgWordsPerSentence = round(numWords/numSentences, 1)
    avgSyllablesPerWord = round(totalSyllables / numWords, 1)
    
    
    readingScore = 206.835 - 1.015 * (numWords/numSentences) - 84.6 * (totalSyllables/numWords)
    gradeLevel = 0.39 * (numWords/numSentences) + 11.8 * (totalSyllables/numWords) - 15.59
    roundedScore = round(readingScore, 1)
    roundedGrade = round(gradeLevel, 1)
    
    print('Number of sentences: ' + str(numSentences))
    print('Number of words: ' + str(numWords))
    print('Number of unique words: ' + str(numUniqueWords))
    print('Average words per sentence: ' + str(avgWordsPerSentence))
    print('Average syllables per word: ' + str(avgSyllablesPerWord))
    print('Reading-ease score: ' + str(roundedScore))
    print('U.S. grade level: ' + str(roundedGrade))
    print()
    
    while True:
        word = input('Enter word to check ("q" to quit) ')
        if word == 'q':
            break
        if word in dictionary.keys():
            numAppearances = dictionary[word.lower()]
        else:
            numAppearances = 0
        
        if numAppearances == 1:
            print('The word "' + word + '" appears ' + str(numAppearances) + ' time.')
        else:
            print('The word "' + word + '" appears ' + str(numAppearances) + ' times.')
    print()
    print('Thanks for using the Text Analyzer!')
if __name__=="__main__":
    main() 