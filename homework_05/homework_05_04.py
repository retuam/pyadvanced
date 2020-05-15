import time
import shelve


class Network:

    db = "users"
    users = {}

    def __init__(self):
        self._validate = True
        self._is_login = False

    def get_is_login(self):
        return self._is_login

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

    def _set_user(self):
        with shelve.open(self.db) as user_db:
            self._password = user_db[self._login]['password']
            self._role = user_db[self._login]['role']
            self._date_reg = user_db[self._login]['date_reg']
            self._posts = user_db[self._login]['posts']

    def _save_user(self):
        with shelve.open(self.db) as user_db:
            user_db[self._login] = {
                'password': self._password,
                'role': self._role,
                'date_reg': self._date_reg,
                'posts': self._posts,
            }

    def exit(self):
        self._save_user()
        return Network()


class Registration(Network):

    def validate_login(self):
        flag = True
        with shelve.open(self.db) as user_db:
            if self._login in user_db.keys():
                print('Login already exist')
                flag = False

        return flag

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

    def __init__(self, mode=True):
        super().__init__()
        self._login = self.set_login()
        if mode:
            self._validate = self.validate_login()
        if self._validate:
            self._password = self.set_password()
            if mode:
                self._validate = self.validate_password()


class Authorization(Registration):

    def __init__(self, reg_mode):
        super().__init__(reg_mode)
        if not reg_mode:
            if self.__search():
                self._set_user()
                self._is_login = True
                print(f'Authorization for {self._login}')
            else:
                print(f'Wrong login or password')

    def __search(self):
        try:
            with shelve.open(self.db) as user_db:
                return user_db[self._login]['password'] == self._password
        except KeyError:
            return False


class User(Authorization):

    def get_date_reg(self):
        return self._date_reg

    def get_role(self):
        return self._role

    def get_posts(self):
        return self._posts

    def __init__(self, reg_mode=True):
        super().__init__(reg_mode)
        if reg_mode:
            self._posts = []
            self._role = 'Guest'
            self._date_reg = None
            if self._validate:
                self._date_reg = time.strftime("%d.%M.%Y", time.localtime())
                if self._login == 'admin':
                    self._role = 'Administrator'
                else:
                    self._role = 'User'
                self._save_user()
                print(f'Valid registration for {self._login}')

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
            with shelve.open(self.db) as user_db:
                print([value.__str__() for value in user_db.values()])
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

        # registration
        if _action == 0 and not network.get_is_login():
            User()
        # authorization
        elif _action == 1 and not network.get_is_login():
            network = User(reg_mode=False)
            user = network
        # exit
        elif _action == 0 and network.get_is_login():
            network = network.exit()
        # view
        elif _action == 2 and network.get_is_login():
            user.view()
        # add post
        elif _action == 1 and network.get_is_login():
            user.add_post()