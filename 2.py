class User:
    def __init__(self, user_id, name):
        self.__user_id = user_id
        self.__name = name
        self.__access_level = 'user'

    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

#     def get_access_level(self):
#         return self.__access_level
#
#     def set_name(self, new_name):
#         self.__name = new_name
#
#     def set_access_level(self, new_access_level):
#         self.__access_level = new_access_level
#
#
# class Admin(User):
#     def __init__(self, user_id, name):
#         super().__init__(user_id, name)
#         self.__admin_access_level = 'admin'
#         self.__user_list = []
#
#     def add_user(self, user):
#         if isinstance(user, User):
#             self.__user_list.append(user)
#             print(f"Пользователь {user.get_name()} успешно добавлен.")
#         else:
#             print("Ошибка: Добавление пользователя не удалось.")
#
#     def remove_user(self, user):
#         if user in self.__user_list:
#             self.__user_list.remove(user)
#             print(f"Пользователь {user.get_name()} успешно удален.")
#         else:
#             print("Ошибка: Пользователь не найден.")
#
#     def get_admin_access_level(self):
#         return self.__admin_access_level
#
#     def set_admin_access_level(self, new_admin_access_level):
#         self.__admin_access_level = new_admin_access_level
#
#
# user1 = User(1, "Иван Соколов")
# user2 = User(2, "Мария Борисова")
# user3 = User(3, "Александр Воробьёв")
# user4 = User(4, "Ольга Тимофеева")
# admin1 = Admin(3, "Петр Лебедев")
#
# print()
#
# admin1.add_user(user1)
# admin1.add_user(user2)
# admin1.add_user(user3)
# admin1.add_user(user4)
#
# print()
#
# print("Список пользователей:")
# for user in admin1._Admin__user_list:
#     print(user.get_name())
#
# print()
#
# admin1.remove_user(user1)
#
# print()
#
# print("Список пользователей после удаления:")
# for user in admin1._Admin__user_list:
#     print(user.get_name())