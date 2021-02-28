import requests
import sys

from bs4 import BeautifulSoup

url = "https://context.reverso.net/translation/"

language_list = ["arabic", "german", "english", "spanish", "french", "hebrew", "japanese", "dutch",
                 "polish", "portuguese", "romanian", "russian", "turkish", "all"]

em_list = []

text_list = []

text_list2 = []

translation_list = []

j = 0

my_arg_list = str(sys.argv)

# print("Hello, welcome to the translator. Translator supports:")
#
# for i in range(len(language_list)):
#     print(str(i + 1) + ".", language_list[i])
#
# print("Type the number of your language:")
#
# lang_input_a = int(input())
#
# print("Type the number of a language you want to translate to or '0' to translate to all languages:")
#
# lang_input_b = int(input())
#
# if lang_input_a == lang_input_b:
#       print("ERROR")
#       exit()

# print("Type the word you want to translate:")
#
# word = str(input())

word = sys.argv[3]

word = word.lower()

if sys.argv[1].lower() not in language_list:
    print("Sorry, the program doesn't support", sys.argv[1])
    exit()
elif sys.argv[2].lower() not in language_list:
    print("Sorry, the program doesn't support", sys.argv[2])
    exit()

r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})

if r.status_code != 200:
    print("Something wrong with your internet connection")
    exit()

test = requests.get("https://context.reverso.net/translation/english-spanish/" + word,
                             headers={'User-Agent': 'Mozilla/5.0'})

if test.status_code == 404:
    print("Sorry, unable to find", word)
    exit()

if sys.argv[1] == "arabic":
    lang_a = "arabic"
    lang_input_a = 1
elif sys.argv[1] == "german":
    lang_a = "german"
    lang_input_a = 2
elif sys.argv[1] == "english":
    lang_a = "english"
    lang_input_a = 3
elif sys.argv[1] == "spanish":
    lang_a = "spanish"
    lang_input_a = 4
elif sys.argv[1] == "french":
    lang_a = "french"
    lang_input_a = 5
elif sys.argv[1] == "hebrew":
    lang_a = "hebrew"
    lang_input_a = 6
elif sys.argv[1] == "japanese":
    lang_a = "japanese"
    lang_input_a = 7
elif sys.argv[1] == "dutch":
    lang_a = "dutch"
    lang_input_a = 8
elif sys.argv[1] == "polish":
    lang_a = "polish"
    lang_input_a = 9
elif sys.argv[1] == "portuguese":
    lang_a = "portuguese"
    lang_input_a = 10
elif sys.argv[1] == "romanian":
    lang_a = "romanian"
    lang_input_a = 11
elif sys.argv[1] == "russian":
    lang_a = "russian"
    lang_input_a = 12
elif sys.argv[1] == "turkish":
    lang_a = "turkish"
    lang_input_a = 13

if sys.argv[2] == "all":
    while j < 13:
        if j+1 == lang_input_a:
            j += 1
        else:
            r = requests.get("https://context.reverso.net/translation/" + sys.argv[1] + "-" + language_list[j].lower() + "/" + word,
                             headers={'User-Agent': 'Mozilla/5.0'})

            soup = BeautifulSoup(r.content, 'html.parser')

            em = soup.find_all("em")
            translation = soup.find_all('a', {"class": 'link_highlighted'})
            text = soup.find_all('div', {"class": "src ltr"})
            text2 = soup.find_all('div', {"class": ["trg ltr", "trg rtl arabic", "trg rtl"]})

            for i in translation:
                translation_list.append(i.get_text())

            for i in text:
                text_list.append(i.get_text().strip())

            for i in text2:
                text_list2.append(i.get_text().strip())

            # print("English Translations:")
            # for i in em_list[:5]:
            #       print(i)
            #
            # print("\nEnglish Examples:")
            # for i in range(0, 5):
            #       print(text_list[i])
            #       print(text_list2[i], "\n")

            with open(word + ".txt", "a", encoding='utf-8') as file:
                # print("\n" + language_list[j], "Translations:")
                file.writelines(language_list[j] + " Translations:" + "\n")

                for i in range(0, 1):
                    # print(em_list[i])
                    file.writelines(translation_list[i] + "\n" + "\n")

                # print("\n" + language_list[j], "Examples:")
                file.writelines(language_list[j] + " Example:" + "\n")

                for i in range(0, 1):
                    # print(text_list[i])
                    file.writelines(text_list[i] + "\n")

                    # print(text_list2[i], "\n")
                    file.writelines(text_list2[i] + "\n" + "\n")
                    file.writelines("\n")

            j += 1
            em_list = []
            translation_list = []
            text_list = []
            text_list2 = []
        if j == 13:
            with open(word + ".txt", "r", encoding='utf-8') as file:
                print(file.read())
            file.close()
            exit()

elif sys.argv[2] == "turkish":
    lang_b = "turkish"
    lang_input_b = 1
elif sys.argv[2] == "german":
    lang_b = "german"
    lang_input_b = 2
elif sys.argv[2] == "english":
    lang_b = "english"
    lang_input_b = 3
elif sys.argv[2] == "spanish":
    lang_b = "spanish"
    lang_input_b = 4
elif sys.argv[2] == "french":
    lang_b = "french"
    lang_input_b = 5
elif sys.argv[2] == "hebrew":
    lang_b = "hebrew"
    lang_input_b = 6
elif sys.argv[2] == "japanese":
    lang_b = "japanese"
    lang_input_b = 7
elif sys.argv[2] == "dutch":
    lang_b = "dutch"
    lang_input_b = 8
elif sys.argv[2] == "polish":
    lang_b = "polish"
    lang_input_b = 9
elif sys.argv[2] == "portuguese":
    lang_b = "portuguese"
    lang_input_b = 10
elif sys.argv[2] == "romanian":
    lang_b = "romanian"
    lang_input_b = 11
elif sys.argv[2] == "russian":
    lang_b = "russian"
    lang_input_b = 12
elif sys.argv[2] == "turkish":
    lang_b = "turkish"
    lang_input_b = 13


r = requests.get("https://context.reverso.net/translation/" + sys.argv[1] + "-" + sys.argv[2] + "/" + word,
                     headers={'User-Agent': 'Mozilla/5.0'})

soup = BeautifulSoup(r.content, 'html.parser')

em = soup.find_all("em")
translation = soup.find_all('a', {"class": 'link_highlighted'})
text = soup.find_all('div', {"class": "src ltr"})
text2 = soup.find_all('div', {"class": "trg ltr"})

for i in translation:
    translation_list.append(i.get_text())

for i in text:
  text_list.append(i.get_text().strip())

for i in text2:
  text_list2.append(i.get_text().strip())

print("\n")

with open(word + ".txt", "a", encoding='utf-8') as file:
    file.writelines(language_list[lang_input_b-1] + " Translations:" + "\n")
    for i in range(0, 1):
      file.writelines(translation_list[i] + "\n" + "\n")

    file.writelines(language_list[lang_input_b - 1] + " Example:" + "\n")
    for i in range(0, 1):
      file.writelines(text_list[i] + "\n")

      file.writelines(text_list2[i] + "\n" + "\n")
      file.writelines("\n")

with open(word + ".txt", "r", encoding='utf-8') as file:
    print(file.read())
file.close()
exit()