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
        if 0 <= index < len(self.data) and field in self.data[index].__dict__:
            self.data[index].__dict__[field] = new_value
    
    def _filter(self, data, func, field):
        if field in self.model().__dict__:
            return [model for model in data if func(model.__dict__[field])]
        else:
            return []
    
    def filter_to_delete(self, func, field):
        self.data = self._filter(self.data, func, field)

    def filter_one_field(self, func, field):
        self.pprint(self._filter(self.data, func, field))
    
    def filter_two_field(self, func, field, func2, field2):
        self.pprint(self._filter(self._filter(self.data, func2, field2), func, field))

    def pprint(self, data):
        head_exp = '{:>15}'*(len(self.model().__dataclass_fields__)+1)
        print(head_exp.format('#', *[self.model.Meta.__dict__[field] for field in self.model().__dataclass_fields__]))
        for index, model in enumerate(data):
            print("{:>15}".format(index), end='')
            for field in model.__dataclass_fields__:
                print("{:>15}".format(model.__dict__[field]), end='')
            print()
