class Urls:
    __BASE_URL = "https://selenium1py.pythonanywhere.com/"
    __LOGIN_PAGE_URL = "https://selenium1py.pythonanywhere.com/{language}/accounts/login/"
    current_language = 'es'

    @classmethod
    def set_language(cls, language):
        cls.current_language = language

    @classmethod
    def get_base_url(cls):
        return cls.__BASE_URL

    @classmethod
    def get_login_page_url(cls):
        return cls.__LOGIN_PAGE_URL.format(language=cls.current_language)
