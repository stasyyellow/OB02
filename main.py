# ЗАДАНИЕ
# Разработай систему управления учетными записями пользователей для небольшой компании.
# Компания разделяет сотрудников на обычных работников и администраторов.
# У каждого сотрудника есть уникальный идентификатор (ID), имя и уровень доступа.
# Администраторы, помимо обычных данных пользователей, имеют дополнительный уровень доступа
# и могут добавлять или удалять пользователя из системы.

# Требования:
# 1.Класс `User*: Этот класс должен инкапсулировать данные о пользователе:
#   ID, имя и уровень доступа ('user' для обычных сотрудников).
# 2.Класс `Admin`: Этот класс должен наследоваться от класса `User`.
# Добавь дополнительный атрибут уровня доступа, специфичный для администраторов ('admin').
# Класс должен также содержать методы `add_user` и `remove_user`, которые позволяют добавлять
# и удалять пользователей из списка (представь, что это просто список экземпляров `User`).
# 3.Инкапсуляция данных: Убедись, что атрибуты классов защищены от прямого доступа и модификации снаружи.
# Предоставь доступ к необходимым атрибутам через методы (например, get и set методы).

class User:
    def __init__(self, user_id, name):
        self.__user_id = user_id
        self.__name = name
        self.__access_level = 'user'

    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_level


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self.___adm_access_lvl = 'admin'
        self.__user_list = []

    def add_user(self, user):
        if isinstance(user, User): #встроенная функ. в Питоне, которая проверяет, является ли объект экземпляром или подклассом класса.
            self.__user_list.append(user)
            print(f"Пользователь {user.get_name()} успешно добавлен.")
        else:
            print("Ошибка: Добавление пользователя не удалось.")

    def remove_user(self, user):
        if user in self.__user_list:
            self.__user_list.remove(user)
            print(f"Пользователь {user.get_name()} успешно удален.")
        else:
            print("Ошибка: Пользователь не найден.")

    def get_adm_access_lvl(self):
        return self.__adm_access_lvl

    def set_adm_access_lvl(self, new_adm_access_lvl):
        self.__adm_access_lvl = new_adm_access_lvl

user1 = User(1, "Иван Соколов")
user2 = User(2, "Мария Борисова")
user3 = User(3, "Александр Воробьёв")
user4 = User(4, "Ольга Тимофеева")
admin1 = Admin(3, "Петр Лебедев")

print()

admin1.add_user(user1)
admin1.add_user(user2)
admin1.add_user(user3)
admin1.add_user(user4)

print()

print("Список пользователей:")
for user in admin1._Admin__user_list:  # Прямой доступ к приватному атрибуту
    print(user.get_name())

print()

admin1.remove_user(user1)

print()

print("Список пользователей после удаления:")
for user in admin1._Admin__user_list:
    print(user.get_name())

