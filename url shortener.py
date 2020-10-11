import pyshorteners

url  = input("Enter the link: ")

shortener = pyshorteners.Shortener()
x= shortener.tinyurl.short()

print(x)