name = input("Hello, what your name?\n")
print("Hello", name, "\n",)

language = input("This is a arch linux website guide, Which language do you need?(English, French, German, Japanese, Chinese)\n").lower()

while True:
 
 languages = {
  "english": "https://archlinux.org/",
    "french": "https://archlinux.fr/",
    "german": "https://archlinux.de/",
    "japanese": "https://wiki.archlinux.jp/",
    "chinese": "https://www.archlinuxcn.org/",
 } 

 if language in languages:
  print("WEB:",languages[language])
  break
 else :
  language = input("Sorry, please try again (or quit)[ERROR:1001]").lower()
  if language == "quit":
   break  
 