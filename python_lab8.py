import os
from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class Event:
    udk: str = 'удк'
    name: str = 'название'
    type_: str = 'тип'
    date: str = 'дату'
    number_people: int = 0
    lastnames: str = 'фамилию'


class Db:
    model = Event
    data: list[model] = []
    filename = ''
    db_file = ''

    def set_file(self, filename):
        self.filename = filename
        
    def get_data(self):
        with open(self.filename, 'r') as db_file:
            self.db_file = self.filename
            self.data = self.model.schema().loads(self.data, many=True)
    
    def set_data(self):
        if not os.path.exists(self.filename): 
            open(self.filename, 'x').close()
        with open(self.db_file, 'w') as db_file:
            db_file.write(self.model.schema().dumps(self.data, many=True))    
    
    def create_model(self):
        new_model = Event()
        func_convert = {"<class 'int'>": int, "<class 'float'>": float, "<class 'bool'>": bool, "<class 'str'>": str}
        for field in new_model.__dataclass_fields__:
            new_model.__dict__[field] = func_convert[str(type(new_model.__getattribute__(field)))](input(f'Введите {field}: '))
        self.data.append(new_model)
            
    def delete_model(self, index: int):
        try:
           del self.data[index]
        except:
            print(f"Нет элемента с индексом {index}!")

    def update_model(self, index: int, field: str, new_value):
        try:
            self.data[index].__dict__[field] = new_value
        except:
            print('Ошибка')


def main():
    db = Db()
    
    while True:
        if db.filename:
            db.get_data()
            print('Load data')
            print(type(db.data))
            print('END DATA')
            
        command = [i for i in input(">>> ").split() if i]
        match command:
            case ['db', filename]:
                db.set_data()
                db.set_file(filename)
                continue
            case ['read']:
                print(db.data)
            case ['create']:
                db.create_model()
            case ['delete', index]:
                db.delete_model(int(index))
            case ['update', index, field]:
                db.update_model(int(index), field)
            case ['exit']:
                exit()

        if db.db_file:
            db.set_data()
            print("Save data")
        
        
if __name__ == "__main__":
    main()
