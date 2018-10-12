# Learning-Pyhton
Hesap makinesi
print ("Yapmak istediğiniz işlemi seçiniz")
print ("Toplama işlemi için 1'e basınız")
print ("Çıkarma işlemi için 2'e basınız")
print ("Bölme işlemi için 3'e basınız")
print ("Çarpma işlemi için 4'e basınız")
x = "1"
y = 20
z = 45
if x == "1":
    print ("Toplama işlemi için sayı yazınız")
    print (y + z)
elif x == "2":
    print ("Çıkarma işlemi için sayı yazınız")
elif x == "3":
    print ("Bölme işlemi için sayı yazınız")
elif x == "4":
    print ("Çarpma işlemi için sayı yazınız
Sezar Şifreleme
MAX_KEY_SIZE = 26
def getMode():
   while True:
      print('Do you wish to encrypt or decrypt a message?')
      mode = input().lower()
      if mode in 'encrypt e decrypt d'.split():
         return mode
      else:
         print('Enter either "encrypt" or "e" or "decrypt" or "d".')
def getMessage():
   print('Enter your message:')
   return input()
def getKey():
   key = 0
   while True:
      print('Enter the key number (1-%s)' % (MAX_KEY_SIZE))
      key = int(input())
      if (key >= 1 and key <= MAX_KEY_SIZE):
         return key
def getTranslatedMessage(mode, message, key):
   if mode[0] == 'd':
      key = -key
   translated = ''
   for symbol in message:
      if symbol.isalpha():
         num = ord(symbol)
         num += key
         if symbol.isupper():
            if num > ord('Z'):      #90
               num -= 26
            elif num < ord('A'):    #65
               num += 26
         elif symbol.islower():
            if num > ord('z'):      #122
               num -= 26
            elif num < ord('a'):    #97
               num += 26
         translated += chr(num)
      else:
         translated += symbol
   return translated
mode = getMode()
message = getMessage()
key = getKey()
print('Your translated text is:')
print(getTranslatedMessage(mode, message, key))
