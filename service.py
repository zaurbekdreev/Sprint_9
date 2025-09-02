class Service:

    def __init__(self, url):
        self._base_url = url.rstrip('/')

    @property
    def main(self):
        return self._base_url

    @property
    def signin(self):
        return f'{self.main}/signin'

    @property
    def signup(self):
        return f'{self.main}/signup'

    @property
    def recipes(self):
        return f'{self.main}/recipes'

    @property
    def recipes_create(self):
        return f'{self.recipes}/create'

    @property
    def change_password(self):
        return f'{self.main}/change-password'


foodgram = Service('https://foodgram-frontend-1.prakticum-team.ru')
