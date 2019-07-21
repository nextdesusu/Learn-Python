class Storage:
    
    def __init__(self, name):
        self.name = name
        self.data = dict()
        self.__raw_data = None

    def __str__(self):
        return "<{}>".format(self.name)
        
    def write_data(self):
        with open(self.name, "rb") as tmp:
            self.__raw_data = tmp.read()

    def transform_data(self):
        data = read_from_tokens(self.__raw_data.decode('utf-8'))
        for item in data:
            name = ' '.join(item[1])
            self.data[name] = (item[0], item[2])
        print(self.data)
    
    def show_data(self):
        print(self.data)
        
        
commands = {
    
}

def parse(request):
    exps = request.split(" ")
    print(exps)

def tokenized(string):
    "Convert a string of characters into a list of tokens."
    return string.replace('(', ' ( ').replace(')', ' ) ').split()

def brackets_to_list(tokens: list):
    if len(tokens) == 0:
        raise SyntaxError('unexpected EOF')
    token = tokens.pop(0)
    if token == '(':
        L = []
        while tokens[0] != ')':
            L.append(brackets_to_list(tokens))
        tokens.pop(0) # pop off ')'
        return L
    elif token == ')':
        raise SyntaxError('unexpected )')
    else:
        try:
            num = int(token)
            return num
        except ValueError:
            return token

def read_from_tokens(data):
    data = data.replace('\r', '').split('\n')
    commands = [brackets_to_list(tokenized(string)) for string in data]
    return commands

def open_db():
    name = "personal.db"
    #return Storage(input("Введите название бд "))
    return Storage(name)

def main():
    db = None
    while True:
        print("Введите: в - выход, о - открыть дб, п - дописать бд, \n",
              "ч - читать информацию из бд, Текущая база данных - " + str(db))
        request = input("Введите запрос: ")
        if request == "в":
            print("Пока...")
            break
        elif request == "о":
            db = open_db()
            db.write_data()
            db.transform_data()
        if request == "п":
            write_db()
        elif request == "ч":
            parse(request)
        
if __name__ == '__main__':
    main()
