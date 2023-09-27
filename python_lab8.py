from dataclasses import dataclass
import os
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class Event:
    udk: str = ''
    name: str = ''
    type_: str = 'ert'
    date: str = ''
    number_people: int = 0
    lastnames: str = ''


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
            if not os.path.exists(self.filename): 
                    open(self.filename, 'x').close()
            self.data = self.model.schema().loads(self.data, many=True)
    
    def set_data(self):
        with open(self.db_file, 'w') as db_file:
            db_file.write(self.model.schema().dumps(self.data, many=True))    
    
    def create_model(self):
        new_model = Event()
        func_convert = {"<class 'int'>": int, "<class 'float'>": float, "<class 'bool'>": bool, "<class 'str'>": str}
        for field in new_model.__dataclass_fields__:
            new_model.__dict__[field] = func_convert[str(type(new_model.__getattribute__(field)))](input(f'Введите {field}: '))
        self.data.append(new_model)
            
    def delete_model(self):
        pass
    

def main():
    db = Db()
    
    while True:
        if db.filename:
            db.get_data()
            print('Load data')
            print(type(db.data))
            print('END DATA')
            
        command = input(">>> ").strip().split()
        match command:
            case ['db', filename]:
                pass
            
            case ['getall']:
                print(db.data)
            
            case ['create']:
                db.create_model()
            
            case ['exit']:
                exit()

        if db.db_file:
            db.set_data()
            print("Save data")
        
        
if __name__ == "__main__":
    main()
