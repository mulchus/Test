data = {"пользователи": {"user1": {"имя": "Евгений Онегин", "вoзраст": 30, "опыт работы": [{"компания": "X Corp", "должность": "бзкенд - разработчик"}, {"компания": "Y LLc", "должность": "аналитик данных"}]}, "user2": {"имя": "Александр Пушкин", "вoзраст": 25, "опыт работы": ["компания: Z Inc", "должность: разработчик"]}}}


def custom_pretty_print(input_dict, indent=2):
    for key, value in input_dict.items():
        if isinstance(value, dict):
            print(' ' * indent + f'{key}:')
            custom_pretty_print(value, indent + 2)
        elif isinstance(value, list):
            print(' ' * indent + f"{key}:")
            for item in value:
                if isinstance(item, dict):
                    custom_pretty_print(item, indent + 2)
                else:
                    print(' ' * (indent + 2) + f"- {item}")
        else:
            print(' ' * indent + f"{key}: {value}")
         
            
custom_pretty_print(data)
