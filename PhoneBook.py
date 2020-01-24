class person():
    def __init__(self,name,number):
        self.name=name
        self.number=number

class phoneb(person): #skapar en klass med alla funktioner
    def __init__(self):
        self.phonebook = []
    def add(self,name ,number):  # lägger till så att jag kan lägga till personer i katalogen
        class_name = person(name,number)
        self.phonebook.append(class_name)
    def write(self): #listar alla objekt
        for i in self.phonebook:
            i=self.phonebook.index(i)
            print(self.phonebook[i].name + " " + self.phonebook[i].number)
    def delete(self, key): #tar bort ett eller flera objekt
        key = key.replace(" ", "")
        key = key.split(",")
        for i in key:
            key_id=key.index(i)

            try:
                for y in self.phonebook:
                    person_id=self.phonebook.index(y)
                    x=str(self.phonebook[person_id].name)

                    if x == key[key_id]:
                        self.phonebook.remove(y)
                        print("item: " + str(i) + " is now deleted")
                    else:
                        print("item: " + str(i) + " could not be deleted")
            except:
                print("item: " + str(i) + " could not be deleted")
    def search(self, word):
        if len(self.phonebook)<50000000:
            y=False
            for i in self.phonebook:
                if i.name == word:
                    print(word + "'s number is " + self.phonebook[self.phonebook.index(i)].number)
                    y=True
                    break
            if y == False:
                print("The word/number you searched for is not in the phonebook.")


