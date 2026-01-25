from abc import ABC, abstractmethod

class Subject(ABC):
    @abstractmethod
    def request(self):
        pass

class RealSubject(Subject):
    def request(self):
        print("Реальный объект: Обработка запроса.")

class Proxy(Subject):
    def __init__(self, real_subject, access=False):
        self._real_subject = real_subject
        self.access = access

    def request(self):
        if self.check_access():
            self._real_subject.request()
            self.log_access()

    def check_access(self):
        if self.access:
            print(f"Заместитель: Проверка доступа перед выполнением запроса. Access: {self.access}")
            return True
        print(f"Заместитель: Отказано в доступе. Access: {self.access}")

    def log_access(self):
        print(f"Заместитель: Логирование времени запроса. Access: {self.access}")

# Клиентский код
my_real_subject = RealSubject()
my_real_subject.request()

proxy = Proxy(my_real_subject)
proxy.request()

proxy = Proxy(my_real_subject, access=True)
proxy.request()

# Вывод: реализует интерфейс основного объекта и перенаправляет вызовы к реальному объекту,
# добавляя при этом дополнительную функциональность.
