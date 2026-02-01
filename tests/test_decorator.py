import allure
from allure_commons.types import Severity
from selene.support import by
from selene.support.shared import browser

@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "KatrinPuzyreva")
@allure.feature("Задачи в репозитории")
@allure.story("Авторизованный пользователь может создать задачу в репозитории")
@allure.link("https://github.com", name="Testing")


def test_decorator_steps():
    open_main_page()
    search_for_repository("KatrinPuzyreva-qa/QA_GURU_HW_8")
    go_to_repository("KatrinPuzyreva-qa/QA_GURU_HW_8")
    open_issue_tab()
    should_see_issue_with_number("")


@allure.step("Открываем главную страницу")
def open_main_page():
    browser.open("https://github.com")


@allure.step("Поиск репозитория {repo}")
def search_for_repository(repo):
    browser.element(".header-search-button").click()  # Получаем элемент
    browser.element("#query-builder-test").type(repo).submit()  # Подтверждаем ввод


@allure.step("Переходим по ссылке репозитория {repo}")
def go_to_repository(repo):
    browser.element(by.link_text(repo)).click()# Нажимаем на ссылку


@allure.step("Открываем таб Issues")
def open_issue_tab():
    browser.element("#issues-tab").click()  # Открываем вкладку Issues


@allure.step("Проверяем наличие Issue No results")
def should_see_issue_with_number(number):
    browser.element(by.partial_text("#No results"))

