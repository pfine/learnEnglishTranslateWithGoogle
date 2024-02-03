#!/usr/bin/python3

import sys

# import os
# import io
# import time
from gtts import gTTS


def loadListFromTxtFile():
    text_file = open("source-rus.txt", "r")  # <== SOURCE TEXT LIST !!!
    lines = text_file.readlines()
    resultLines = []

    for line in lines:
        line = line.strip()
        # print(' > line = ', line)
        # make sure that empty lines will be removed from pool
        # if not line in ['\n', '\r\n']:
        if len(line) != 0:
            resultLines.append(line)
    return resultLines


def main():
    listFromFile = loadListFromTxtFile()
    # print(' >>>--START--> listFromFile = ', listFromFile)
    if len(listFromFile) == 0:
        print(" !!! Lack of words to convert them to mp3")
        sys.exit(1)

    i = len(listFromFile) - 1
    # print(' >>>--START--> i = ', i)
    while i >= 0:
        # print(' > i = ', i)
        # print(' > listFromFile[i] = ', listFromFile[i])
        line2translate = listFromFile[i].split(",")[0]  # take only fitst part to comma
        print(" > line2translate = ", line2translate)

        # If line start with # - skip it
        if line2translate.startswith("#"):
            i = i - 1
            # print(' > i = ', i)
            print(" > line2translate = ", line2translate, " - SKIPPED")
            continue

        # lang can be find here https://gtts.readthedocs.io/en/v2.2.1/_modules/gtts/lang.html
        tts = gTTS(text=line2translate, lang="ru", slow=False)

        # File name used to save
        save_file_name = ""
        if "/" in line2translate:
            save_file_name = line2translate.replace("/", "")
        elif "\\" in line2translate:
            save_file_name = line2translate.replace("\\", "")
        else:
            save_file_name = line2translate

        try:
            # <== OUTPUT DIRECTORY !!!
            tts.save("output/" + save_file_name + ".mp3")
        except ValueError as e:
            print(" >>> e = ", e)
            print(" > line2translate = ", line2translate, " - failed, so repeat")
        except Exception as e:
            print(" >>> Exception = ", e)
            print(
                " > line2translate = ",
                line2translate,
                " - failed, OTHER ISSUE, so repeate",
            )
        else:  # no eception !!!
            i = i - 1
            # print(' > i = ', i)
            print(" > line2translate = ", line2translate, " - DONE")


if __name__ == "__main__":
    main()
