from dataclasses import dataclass
from dataclasses_json import dataclass_json
from db8 import Db
import yaml


@dataclass_json
@dataclass
class Event:
    udk: str = 'удк'
    name: str = 'название'
    type_: str = 'тип'
    date: str = 'дату'
    number_people: int = 0
    lastnames: str = 'фамилию'


def main():
    db = Db(Event)
    while True:
        if db.filename:
            db.get_data()
            
        command = [i for i in input(">>> ").split() if i]
        match command:
            case ['db', filename]:
                if db.filename:
                    db.set_data()
                db.set_file(filename)
                continue
            case ['read']:
                print(yaml.dump(db.data))
            case ['create']:
                db.create_model()
            case ['delete', index]:
                db.delete_model(int(index))
            case ['update', index, field]:
                db.update_model(int(index), field)
            case ['exit']:
                db.set_data()
                exit()

        if db.filename:
            db.set_data()
        
        
if __name__ == "__main__":
    main()
