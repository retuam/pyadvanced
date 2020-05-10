import time


class Network:

    users = {}

    def __init__(self):
        self._user = None
        self._is_login = False

    def get_is_login(self):
        return self._is_login

    def get_user(self):
        return self._user

    def get_navigation(self):
        if self._is_login:
            return {
                0: 'exit',
                1: 'add post',
                2: 'view',
            }
        else:
            return {
                0: 'registration',
                1: 'authorization',
            }


class Registration(Network):

    def validate_login(self):
        if self._login in Network.users.keys():
            print('Login already exist')
            return False

        return True

    def validate_password(self):
        if not self._password.isalnum():
            print('Password is invalid')
            return False
        elif self._password != self.set_password_validate():
            print('Validate password isn\'t similar to password')
            return False

        return True

    @staticmethod
    def set_login():
        return str(input('Enter your login: '))

    @staticmethod
    def set_password():
        return str(input('Enter your password: '))

    @staticmethod
    def set_password_validate():
        return str(input('Enter your password one more: '))

    def get_password(self):
        return self._password

    def get_login(self):
        return self._login

    def __init__(self):
        self._login = self.set_login()
        self._validate = self.validate_login()
        self._password = self.set_password()
        self._validate = self.validate_password()


class Authorization(Registration):

    def __init__(self):
        self._is_login = False
        self._user = None
        self._login = self.set_login()
        self._password = self.set_password()
        if self.__search():
            self._user = Network.users[self._login]
            self._is_login = True
            print(f'Authorization for {self._login}')
        else:
            print(f'Wrong login or password')

    def __search(self):
        try:
            return Network.users[self._login].get_password() == self._password
        except KeyError:
            return False


class User(Registration):

    def get_date_reg(self):
        return self._date_reg

    def get_role(self):
        return self._role

    def get_posts(self):
        return self._posts

    def __init__(self):
        super().__init__()
        self._posts = []
        self._role = 'Guest'
        self._date_reg = None
        if self._validate:
            self._date_reg = time.strftime("%d.%M.%Y", time.localtime())
            if self._login == 'admin':
                self._role = 'Administrator'
            else:
                self._role = 'User'
            Network.users[self._login] = self
            print(f'Valid registration for {self._login}')
        else:
            print(1)

    def __str__(self):
        return str({
            'login': self.get_login(),
            'data_reg': self.get_date_reg(),
            'role': self.get_role(),
            'posts': [(row['txt'], row['date']) for row in self.get_posts()]
        })

    def add_post(self):
        _post = str(input('Enter your post: '))
        if _post:
            self._posts.append({
                'txt': _post,
                'date': time.strftime("%d.%M.%Y", time.localtime())
            })

    def view(self):
        if self.get_role() == 'Administrator':
            print([value.__str__() for value in Network.users.values()])
        else:
            print(self)


if __name__ == '__main__':
    network = Network()
    while network.get_navigation():
        print('Next action:', *[(str(key) + ' - ' + value) for key, value in network.get_navigation().items()])

        try:
            _action = int(input('Enter your action: '))
        except ValueError:
            continue

        try:
            network.get_navigation()[_action]
        except KeyError:
            break

        if _action == 0 and not network.get_is_login():
            User()
        elif _action == 1 and not network.get_is_login():
            network = Authorization()
            user = network.get_user()
        elif _action == 0 and network.get_is_login():
            network = Network()
        elif _action == 2 and network.get_is_login():
            user.view()
        elif _action == 1 and network.get_is_login():
            user.add_post()