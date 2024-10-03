from selenium.webdriver.common.by import By

NAME_INPUT_FIELD = (By.XPATH, '//label[text()="Имя"]/parent::div/input') # Имя при регистрации
EMAIL_INPUT_FIELD = (By.XPATH, '//label[text()="Email"]/parent::div/input') # Почта при регистрации
PASSWORD_INPUT_FIELD = (By.XPATH, '//label[text()="Пароль"]/parent::div/input') # Пароль при регистрации
REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']") # Кнопка зарегистрироваться при регистрации
REGISTER_ERROR = (By.XPATH, "//*[text()='Некорректный пароль']") # Неккоректный пароль при регистрации
LOGIN_HEADER = (By.XPATH, "//h2[text()='Вход']") # Кнопка входа в акаунт
USERNAME_INPUT_FIELD = (By.XPATH, '//input[@name="name" and @type="text"]') # Почта при входе в аккаунт
PASSWORD_INPUT_FIELD = (By.XPATH, '//input[@name="Пароль" and @type="password"]') # Пароль при входе в аккаунт
LOGIN_BUTTON = (By.XPATH, '//button[text()="Войти"]') # Кнопка войти
LOGIN_TO_ACCOUNT_BUTTON = (By.XPATH, '//button[text()="Войти в аккаунт"]') # Кнопка войти в аккаунт
PLACE_AN_ORDER = (By.XPATH, '//button[text()="Оформить заказ"]') # Кнопка оформить заказ
PERSONAL_CABINET_LINK = (By.XPATH, '//p[contains(@class, "AppHeader_header__linkText__3q_va") and text()="Личный Кабинет"]') # Переход в личный кабинет
LOGOUT_BUTTON = (By.XPATH, '//button[text()="Выход"]') # Выход
REGISTER_AND_FORGOT_PASSWORD_LOGIN_BUTTON = (By.CLASS_NAME, "Auth_link__1fOlj") # Кнопка войти
CONSTRUCTOR_LINK = (By.XPATH, "//p[text()='Конструктор']") # Конструктор
SVG_ICON = (By.CSS_SELECTOR, "svg[xmlns='http://www.w3.org/2000/svg']") # Лого

BUNS_SECTION = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and .//span[text()='Булки']]") # Булки
SAUCES_SECTION = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and .//span[text()='Соусы']]") # Соусы
FILLINGS_SECTION = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and .//span[text()='Начинки']]") # Начинки

BUNS_SECTION_ACTIVE = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and contains(@class, 'tab_tab_type_current') and .//span[text()='Булки']]")  # Нажатые булки
SAUCES_SECTION_ACTIVE = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and contains(@class, 'tab_tab_type_current') and .//span[text()='Соусы']]") # Нажатые соусы
FILLINGS_SECTION_ACTIVE = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and contains(@class, 'tab_tab_type_current') and .//span[text()='Начинки']]") # Нажатые начинки







