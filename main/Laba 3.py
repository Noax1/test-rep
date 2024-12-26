class Singleton:
    _instance = None  # Переменная для хранения единственного экземпляра
    def __new__(cls, *args, **kwargs):
        # Проверяем, существует ли уже экземпляр
        if not cls._instance:
            # Создаем новый экземпляр только при первом вызове
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def do_something(self):
        print("Singleton instance is working.")

# Использование
singleton1 = Singleton()
singleton2 = Singleton()
print(singleton1 is singleton2)  # True: оба объекта ссылаются на один и тот же экземпляр
singleton1.do_something()


from abc import ABC, abstractmethod

# Абстрактный класс Creator, который задает фабричный метод
class Creator(ABC):
    @abstractmethod
    def factory_method(self):
        pass

    def some_operation(self):
        # Используем фабричный метод для получения продукта
        product = self.factory_method()
        print(f"Created: {product.__class__.__name__}")
        product.use()

# Абстрактный интерфейс для продуктов
class Product(ABC):
    @abstractmethod
    def use(self):
        pass

# Конкретные реализации продуктов
class ConcreteProductA(Product):
    def use(self):
        print("Using ConcreteProductA.")

class ConcreteProductB(Product):
    def use(self):
        print("Using ConcreteProductB.")

# Конкретные реализации фабрики
class ConcreteCreatorA(Creator):
    def factory_method(self):
        return ConcreteProductA()
class ConcreteCreatorB(Creator):
    def factory_method(self):
        return ConcreteProductB()

# Использование
creator = ConcreteCreatorA()
creator.some_operation()  # Создает и использует ConcreteProductA
creator = ConcreteCreatorB()
creator.some_operation()  # Создает и использует ConcreteProductB



# Абстрактная фабрика
class AbstractFactory(ABC):
    @abstractmethod
    def create_product_a(self):
        pass

    @abstractmethod
    def create_product_b(self):
        pass

# Абстрактные интерфейсы продуктов
class AbstractProductA(ABC):
    @abstractmethod
    def function_a(self):
        pass

class AbstractProductB(ABC):
    @abstractmethod
    def function_b(self):
        pass

# Конкретные реализации продуктов
class ProductA1(AbstractProductA):
    def function_a(self):
        print("ProductA1 is working.")

class ProductB1(AbstractProductB):
    def function_b(self):
        print("ProductB1 is working.")

class ProductA2(AbstractProductA):
    def function_a(self):
        print("ProductA2 is working.")

class ProductB2(AbstractProductB):
    def function_b(self):
        print("ProductB2 is working.")


# Конкретные реализации фабрик
class Factory1(AbstractFactory):
    def create_product_a(self):
        return ProductA1()

    def create_product_b(self):
        return ProductB1()


class Factory2(AbstractFactory):
    def create_product_a(self):
        return ProductA2()

    def create_product_b(self):
        return ProductB2()


# Использование
factory = Factory1()
product_a = factory.create_product_a()
product_b = factory.create_product_b()
product_a.function_a()  # ProductA1 is working
product_b.function_b()  # ProductB1 is working

factory = Factory2()
product_a = factory.create_product_a()
product_b = factory.create_product_b()
product_a.function_a()  # ProductA2 is working
product_b.function_b()  # ProductB2 is working


# Продукт, который будет строиться
class Product:
    def __init__(self):
        self.parts = []

    def add_part(self, part):
        self.parts.append(part)

    def show_parts(self):
        print("Product parts:", ", ".join(self.parts))

# Строитель, который определяет шаги построения
class Builder:
    def __init__(self):
        self.product = Product()

    def build_part_a(self):
        self.product.add_part("PartA")

    def build_part_b(self):
        self.product.add_part("PartB")

    def build_part_c(self):
        self.product.add_part("PartC")

    def get_result(self):
        return self.product

# Директор, который задает порядок построения
class Director:
    def __init__(self, builder):
        self.builder = builder

    def construct(self):
        # Определяем порядок шагов построения
        self.builder.build_part_a()
        self.builder.build_part_b()
        self.builder.build_part_c()

# Использование
builder = Builder()
director = Director(builder)
director.construct()  # Конструирует продукт по шагам
product = builder.get_result()
product.show_parts()  # Product parts: PartA, PartB, PartC