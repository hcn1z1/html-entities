from bs4 import BeautifulSoup as bs4
import os


class Encrypter:
    def __init__(self,letter):
        self.letter = letter 
        self.page = bs4(self.letter, features="lxml")
        self.banned  = ["style","script","html","meta","head","body","color","styles"]

    def     (self,letter = None):
        if letter is not None:self.letter = letter
        '''
            HTML Source Page to HTML Entities
        '''
        content = self.page.text.replace("\n"," ").split(" ")
        # making a list of all words in html letter
        for word in content:
            if word != '\n' and word != ' ' and len(word)>2 and word not in self.banned:
                newWord = '' 
                for letter in word:
                    if (letter >= 'a' and letter <= 'z') or (letter >= 'A' and letter <= 'Z'):
                        newWord += f'&#{ord(letter)};'
                    else: pass
                if len(newWord)>4:
                    self.letter = self.letter.replace(word,newWord)
        return letter


class EncryptionHardOne(Encrypter):
    '''
        Encode the whole HTML source to entities
        BUt there is some conditions

        1 remove any unnecessary \'#\', it breaks the encryption, for example: href="#".
        2 consider removing <style> Content </style> and add it after encryption to make
        the encryption works.
        3 always use base64 or email-embedded images instead of urls.
        4 if an image doesnt work when embedded to base64, please 
        remove it from source code then add it later.

        :return: Letter type: str
    '''
    def __init__(self,letter):
        Encrypter.__init__(self,letter)
        self.letter = letter 
        self.page = bs4(self.letter, features="html.parser")
        self.banned  = []

    def encodingLetterX(self):
        '''
            Encrypting everything
        '''
        # getting tags used on script
        self.banned = [tag.name for tag in self.page.find_all()]
        self.bannedNames = []
        # now changing content of attributes in tags like this lol:

        for i in self.banned:
            Items = list(self.page.find_all(i))
            for Item in Items:
                gatheredAttr = list(Item.attrs.keys())
                for attr in gatheredAttr:
                    
                    # sometimes bs4 returns attributes contents as string
                    # and sometimes as a list. we took each case seperately
                    # the condition use to encode the string was only for strings
                    # and special css characters such as "-" and ":"
                    # encoding special character "#" may cause billions of problems.
                    # the script aint perfect but it does most of the work.

                    if type(Item.attrs[attr]) == str:
                        replacement = ""
                        for p in Item.attrs[attr]:
                            if (p >= 'a' and p <= 'z') or (p >= 'A' and p <= 'Z') or p =="-" or p ==":" or p==";" or p ==" " :replacement += f'&#{ord(p)};'
                            else: replacement += p
                        if Item.attrs[attr] not in self.bannedNames:
                            self.letter = self.letter.replace(Item.attrs[attr],replacement)
                            self.bannedNames += Item.attrs[attr].split(":")

                    elif type(Item.attrs[attr]) == list: 
                        for item in Item.attrs[attr]:
                            replacement = ""
                            for p in item:
                                if (p >= 'a' and p <= 'z') or (p >= 'A' and p <= 'Z') or p =="-" or p ==":" or p==";" or p == " ":replacement += f'&#{ord(p)};'
                                else: replacement += p
                            if item not in self.bannedNames:
                                self.letter = self.letter.replace(item,replacement)
                                self.bannedNames += item.split(":")  
            # remove duplicates tags 
            for r in range(self.banned.count(i)):
                self.banned.remove(i)
        # encoding content of letter with method encodingLetter
        # just to be obvious, banned is a list of words that we dont want to replace
        # method 'replace' replace everything in a string with no conditions.
        # i was afraid it will change a tag or an already encoded letter.
        # and that's the main use of banned and bannedNames

        self.banned += self.bannedNames
        self.encodingLetter(self.letter)
        return self.letter

