from dataclasses import dataclass
from dataclasses_json import dataclass_json
from db8 import Db


@dataclass_json
@dataclass
class Event:
    udk: str = 'удк'
    name: str = 'название'
    type_: str = 'тип'
    date: str = 'дата'
    number_people: int = 0
    lastnames: str = 'фамилия'

    class Meta:
        udk = 'удк'
        name = 'название'
        type_ = 'тип'
        date = 'дата'
        number_people = 'кол. людей'
        lastnames = 'фамилия'


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
                db.pprint(db.data)
            case ['create']:
                db.create_model()
            case ['delete', index]:
                db.delete_model(int(index))
            case ['update', index, field, new_value]:
                db.update_model(int(index), field, new_value)
            case ['exit']:
                db.set_data()
                exit()

        if db.filename:
            db.set_data()
        
        
if __name__ == "__main__":
    main()
