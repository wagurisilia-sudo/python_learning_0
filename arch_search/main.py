import webbrowser

def open_archlinux_website(url):
 webbrowser.open(url)

def browser_mode_ask():
 while True:
  choice = input("Do you want to open this website? (yes/no)\n").lower()
  if choice == "yes" :
   
   return True

  if choice == "no":
   
   return False
    
  else :
   
   continue


browser_mode = "ask"

name = input("Hello, what your name?\n")

print("Hello", name, "\n",)

languages = {
  "english": "https://archlinux.org/",
    "french": "https://archlinux.fr/",
    "german": "https://archlinux.de/",
    "japanese": "https://wiki.archlinux.jp/",
    "chinese": "https://www.archlinuxcn.org/",
 } 

language = input("This is a arch linux website guide, Which language do you need?(English, French, German, Japanese, Chinese)\n").lower()

while True:

 if language in languages:
  print("WEB:",(languages[language]),)

  if browser_mode == "always":
   open_archlinux_website(languages[language])
   break
  

  elif browser_mode == "ask":
   if browser_mode_ask() :
    open_archlinux_website(languages[language])
   break
   


     
  else :
   print("[ERROR1002], incorrect mode\n")
   break




 else :
  language = input("Sorry, please try again (or quit)[ERROR:1001]\n").lower()
  if language == "quit":
   break  
 