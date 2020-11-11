#!/usr/bin/python3

from gtts import gTTS
import sys, os, io, time

def loadListFromTxtFile():
    text_file = open("test_source.txt", "r") # <== SOURCE TEXT LIST !!!
    lines = text_file.readlines()
    resultLines = []

    for line in lines:
        line = line.strip()
        # print(' > line = ', line)
        # make sure that empty lines will be removed from pool
        #if not line in ['\n', '\r\n']:
        if len(line) != 0:
            resultLines.append(line)
    return resultLines

# def repeatTranslate(word2translate):
#     print(' >> word2translate = ', word2translate)
#     tts = gTTS(text=word2translate, lang="en")
#     tts.save("output/" + word2translate + ".mp3")  # <== OUTPUT DIRECTORY !!!

def main():
    listFromFile = loadListFromTxtFile()
    # print(' >>>--START--> listFromFile = ', listFromFile)
    if (len(listFromFile) == 0):
        print(' !!! Lack of words to convert them to mp3')
        sys.exit(1)

    i = len(listFromFile) - 1
    # print(' >>>--START--> i = ', i)
    while i >= 0:
        # print(' > i = ', i)
        # print(' > listFromFile[i] = ', listFromFile[i])
        line2translate = listFromFile[i].split(',')[0] # take only fitst part to comma
        # print(' > line2translate = ', line2translate)
        tts = gTTS(text=line2translate, lang="en")
        try:
            tts.save("output/" + line2translate + ".mp3") # <== OUTPUT DIRECTORY !!!
        except ValueError as e:
            # print(' >>> e = ', e)
            print(' > line2translate = ', line2translate, ' - failed, so repeat')
        except Exception as e:
            print(' >>> Exception = ', e)
            print(' > line2translate = ', line2translate, ' - failed, OTHER ISSUE, so repeate')
        else: # no eception !!!
            i = i - 1
            # print(' > i = ', i)
            print(' > line2translate = ', line2translate, ' - DONE')

if __name__ == "__main__":
    main()