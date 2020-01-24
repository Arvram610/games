class phoneb: #skapar en klass med alla funktioner
    def __init__(self):
        self.phonebook = {}
    def add(self,x,y):  # lägger till så att jag kan lägga till personer i katalogen
        self.phonebook[x] = y
    def write(self): #listar alla objekt
        for x, y in self.phonebook.items():
            print(x + " " + y)
    def delete(self, key): #tar bort ett eller flera objekt
        key = key.replace(" ", "")
        key = key.split(",")
        key =list(key)
        for i in key:
            try:
                del (self.phonebook[i])
                print("item: " + str(i) + " is now deleted")
            except:
                print("item: " + str(i) + " could not be deleted")
    def search(self, word): #tro det eller ej men hastighetskillnaden är så liten att den bara ligge på några millisekunder. detta tar ca 3 millisekunder medans if word in self.phonebook tar ca 2 sekunder om talet är mindre än 50 miljoner
        if len(self.phonebook)<50000000:
            y=False
            for i in self.phonebook:
                if i == word:
                    print(word + "'s number is " + self.phonebook[word])
                    y=True
                    break
            if y == False:
                print("The word/number you searched for is not in the phonebook.")
        else:
            if word in self.phonebook:
                print(word + "'s number is " + self.phonebook[word])
            else:
                print("The word/number you searched for is not in the phonebook.")