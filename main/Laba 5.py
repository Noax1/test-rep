from abc import ABC, abstractmethod

# Интерфейс
class Database(ABC):
    @abstractmethod
    def query(self, sql: str):
        pass

# Реальный субъект
class RealDatabase(Database):
    def query(self, sql: str):
        print(f"Executing query: {sql}")

# Прокси
class DatabaseProxy(Database):
    def __init__(self, has_access: bool):
        self._real_database = RealDatabase()
        self._has_access = has_access

    def query(self, sql: str):
        if self._has_access:
            self._real_database.query(sql)
        else:
            print("Access denied. Query cannot be executed.")


user_db = DatabaseProxy(has_access=False)
admin_db = DatabaseProxy(has_access=True)

user_db.query("SELECT * FROM users")  # Вывод: Access denied. Query cannot be executed.
admin_db.query("SELECT * FROM users")  # Вывод: Executing query: SELECT * FROM users



# Целевой интерфейс
class Logger(ABC):
    @abstractmethod
    def log(self, message: str):
        pass

# Сторонний класс
class ExternalLogger:
    def log_message(self, msg: str):
        print(f"External log: {msg}")

# Адаптер
class LoggerAdapter(Logger):
    def __init__(self, external_logger: ExternalLogger):
        self._external_logger = external_logger

    def log(self, message: str):
        self._external_logger.log_message(message)

external_logger = ExternalLogger()
logger = LoggerAdapter(external_logger)

logger.log("This is a test message.")  # Вывод: External log: This is a test message.



# Интерфейс устройства
class Device(ABC):
    @abstractmethod
    def print(self, data: str):
        pass

# Конкретные устройства
class Monitor(Device):
    def print(self, data: str):
        print(f"Displaying on monitor: {data}")

class Printer(Device):
    def print(self, data: str):
        print(f"Printing to paper: {data}")

# Абстракция
class Output(ABC):
    def __init__(self, device: Device):
        self._device = device

    @abstractmethod
    def render(self, data: str):
        pass

# Расширенные абстракции
class TextOutput(Output):
    def render(self, data: str):
        self._device.print(f"Text: {data}")

class ImageOutput(Output):
    def render(self, data: str):
        self._device.print(f"Image: [Binary data: {data}]")

# Использование
monitor = Monitor()
printer = Printer()

text_on_monitor = TextOutput(monitor)
text_on_printer = TextOutput(printer)

text_on_monitor.render("Hello, world!")  # Вывод: Displaying on monitor: Text: Hello, world!
text_on_printer.render("Hello, world!")  # Вывод: Printing to paper: Text: Hello, world!

image_on_monitor = ImageOutput(monitor)
image_on_monitor.render("101010101")  # Вывод: Displaying on monitor: Image: [Binary data: 101010101]