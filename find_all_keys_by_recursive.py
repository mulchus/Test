data = {"пользователи": {"user1": {"имя": "Евгений Онегин", "вoзраст": 30, "опыт работы": [{"компания": "X Corp", "должность": "бзкенд - разработчик"}, {"компания": "Y LLc", "должность": "аналитик данных"}]}, "user2": {"имя": "Александр Пушкин", "вoзраст": 25, "опыт работы": ["компания: Z Inc", "должность: разработчик"]}}}


def find_all_keys(input_dict: dict) -> list:
    result = []
    for key, val in input_dict.items():
        if key.startswith('имя'):
            result.append(val)
        if isinstance(val, dict):
            result.extend(find_all_keys(val))
    return result


# data = yaml.safe_load(Path(sys.argv[1]).read_text())
descriptions = find_all_keys(data)
print(descriptions)
