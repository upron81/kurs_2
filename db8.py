import os

class Db:
    filename = ''

    def __init__(self, model):
        self.model = model
        self.data: list[model] = []

    def set_file(self, filename):
        self.filename = filename
        
    def get_data(self):
        if os.path.exists(self.filename): 
            with open(self.filename, 'r') as db_file:
                self.data = self.model.schema().loads(db_file.read(), many=True)
        else:
            self.data = []
    
    def set_data(self):
        with open(self.filename, 'w') as db_file:
            db_file.write(self.model.schema().dumps(self.data, many=True))    
    
    def create_model(self):
        new_model = self.model()
        func_convert = {"<class 'int'>": int, "<class 'float'>": float, "<class 'bool'>": bool, "<class 'str'>": str}
        for field in new_model.__dataclass_fields__:
            new_model.__dict__[field] = func_convert[str(type(new_model.__getattribute__(field)))](input(f'Введите {self.model.Meta.__dict__[field]}: '))
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
    
    def universum_update(self, field, func):
        pass

    def print_model(self):
        print(self.data)
