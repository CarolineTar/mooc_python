### Classe de dictionaires ordonnés ###
class OrderedDictionnary:
    def __init__(self, *entry):
        self.keys=list()
        self.values=list()
        # un dictionaire a été entré
        if len(entry)==1  and type(entry[0]) == dict:
            dico = entry[0]
            for key, value in dico.items():
                try:
                    new_key = str(key)
                    new_value = int(value)
                except:
                    raise Exception("les valeurs", entry,"ne sont pas au bon format0")
                new_key = new_key.strip()
                self.keys.append(new_key)
                self.values.append(new_value)
        #plusieurs arguments ont été entrés
        elif len(entry) >=1:
            for val in entry:
                symb=str(val)
                sep = symb.split("=")
                if len(sep) == 2:
                    try:
                        new_key = str(sep[0])
                        new_value = int(sep[1])
                    except:
                        raise Exception("les valeurs", entry,"ne sont pas au bon format1")
                    new_key = new_key.strip()
                    self.keys.append(new_key)
                    self.values.append(new_value)
                else:
                    raise Exception("les valeurs", entry,"ne sont pas au bon format2")
        if len(self.keys) != len(self.values):
            raise Exception("il y a un problème !!!")

    def __repr__(self):
        output="{"
        output +=  self.keys[0] + ":" + str(self.values[0])
        for i in range(1,len(self.keys)):
            output +=  " ," + self.keys[i] + ":" + str(self.values[i])
        output +="}"
        return output


    def __getitem__(self, item):
        for ind, key in enumerate(self.keys):
            if item == key:
                return(self.values[ind])
        print("la clé", item, "n est pas dans", self)
    
    def __delitem__(self, item):
        # je n'ai repris que celui là parce que la flemme, mais idéalement il faudrait tous les modifier
        if item in self.keys:
            ind = self.keys.index(item)
            del self.keys[ind]
            del self.values[ind]
            print("nous avons supprimé lentrée", item)
        else: 
            print("la clé", item, "n est pas dans", self)

    
    def __setitem__(self, wanted_key, new_value):
        test = 0
        for ind, key in enumerate(self.keys):
            if wanted_key == key:
                try:
                    self.values[ind]=int(new_value)  
                except:
                    raise Exception("la valeur", new_value,"ne sont pas au bon format4")     
                test = 1
                print("l'ancienne valeur a été remplacée")
        if test == 0:
            try:
                self.keys.append(str(wanted_key))
                self.values.append(int(new_value))
            except:
                raise Exception("les valeurs", wanted_key, new_value,"ne sont pas au bon format5")
            print("nous avons ajouté cet item à la place", len(self.values))
            
    def __contains__(self, wanted_key):
        test = 0
        for key in self.keys:
            if wanted_key == key:
                test = 1
                return True
        if test == 0:
            return False

    def __len__(self):
        return len(self.keys)

    def sort(self, rev = False):
        sorted_keys = sorted(self.keys, reverse = rev)
        sorted_values = list()
        for num1, new_key in enumerate(sorted_keys):
            for num2, old_key in enumerate(self.keys):
               if new_key == old_key:
                   sorted_values.append(self.values[num2])
        self.keys = sorted_keys
        self.values = sorted_values

    def my_generator(self):
            for key in self.keys:
                yield key

    def __iter__(self):
        # méthode plus simple que la précédente
        return iter(self.keys)

    def keys(self):
        return self.keys
    
    def values(self):
        return self.values
    
    def items(self):
        for ind, key in enumerate(self.keys):
            value = self.values[ind]
            yield (key, value)
        return output
    
    def __add__(self, new_dico):
        if type(new_dico) ==dict:
            new_object = OrderedDictionnary(new_dico)
            total_keys = self.keys
            total_values = self.values
            for ind, key in enumerate(new_object.keys):
                total_keys.append(key)
                total_values.append(new_object.values[ind])
            self.keys=total_keys
            self.values = total_values
            return self
        else:
            raise Exception(new_dico, "n'est pas un dictionnaire!")
        

test = OrderedDictionnary("pommes = 49", "poires = 45")
