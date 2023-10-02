from dataclasses import dataclass
from dataclasses_json import dataclass_json
from db8 import Db


@dataclass_json
@dataclass
class Event:
    udk: str
    name: str
    type_: str
    date: str
    number_people: int
    lastnames: str

    class Meta:
        udk = 'удк'
        name = 'название'
        type_ = 'тип'
        date = 'дата'
        number_people = 'количество людей'
        lastnames = 'фамилию'


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
                db.print_model
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
