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
    
    def _filter(self, func, field):
        return [model for model in self.data if func(model.__dict__[field])]
    
    def filter_to_delete(self, func, field):
        try:
            self.data = self._filter(func, field)
        except:
            print('Ошибка')

    def filter_to_print(self, func, field):
        try:
            self.pprint(self._filter(func, field))
        except:
            print('Ошибка')

    def pprint(self, data):
        head_exp = '{:9} '*(len(self.model().__dataclass_fields__)+1)
        print(head_exp.format(' ', *self.model().__dataclass_fields__))
