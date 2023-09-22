from dataclasses import dataclass
import os
import yaml


@dataclass
class Event:
    udk: str
    name: str
    type_: str
    date: str
    number_people: int
    lastnames: str


class Db:
    data: list[Event] = []
    
    def set_file(self, filename):
        self._filename = filename
        
    def get_data(self):
        with open(self._filename, 'r') as db_file:
            self.data = yaml.safe_load(db_file)
    
    def set_data(self):
        with open(self._filename, 'w') as db_file:
            yaml.dump(self.data, db_file)    
            
    
def main():
    db = Db()
    while True:
        command = input(": ").strip().split()
        match command:
            case ('db', filename):
                if not os.path.exist(filename): 
                    open(filename, 'x').close()
                db.set_file(filename)
            
            case ('getall'):
                print(db.data)
        
        
if __name__ == "__main__":
    pass
