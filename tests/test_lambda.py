import allure
from allure_commons.types import Severity
from selene.support import by
from selene.support.shared import browser


def test_dynamic_steps():
    allure.dynamic.tag("web")
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature("Задачи в репозитории")
    allure.dynamic.story("Неавторизованный пользователь может открыть публичный репозиторий")
    allure.dynamic.link("https://github.com", name="Testing")
    with allure.step("Открываем главную страницу"):
        browser.open("https://github.com")

    with allure.step("Поиск репозитория"):
        browser.element(".header-search-button").click()  # Получаем элемент
        browser.element("#query-builder-test").type("KatrinPuzyreva-qa/QA_GURU_HW_8").submit()  # Подтверждаем ввод

    with allure.step("Переходим по ссылке репозитория"):
        browser.element(by.link_text("KatrinPuzyreva-qa/QA_GURU_HW_8")).click()  # Нажимаем на ссылку

    with allure.step("Открываем вкладку Issues"):
        browser.element("#issues-tab").click()

    with allure.step("Проверяем наличие No results"):
        browser.element(by.partial_text("#No results"))

