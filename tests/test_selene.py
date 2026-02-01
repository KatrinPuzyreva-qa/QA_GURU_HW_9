from idlelib import browser
import allure
from allure_commons.types import Severity
from selene.support import by
from selene import browser, have, be

@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "KatrinPuzyreva")
@allure.feature("Задачи в репозитории")
@allure.story("Авторизованный пользователь может создать задачу в репозитории")
@allure.link("https://github.com", name="Testing")


def test_selene():
    browser.open("https://github.com")

    browser.element(".header-search-button").click()  # Получаем элемент
    browser.element("#query-builder-test").type("KatrinPuzyreva-qa/QA_GURU_HW_8").submit() # Подтверждаем ввод

    browser.element(by.link_text("KatrinPuzyreva-qa/QA_GURU_HW_8")).click()# Нажимаем на ссылку

    browser.element("#issues-tab").click()  # Открываем вкладку Issues

    browser.element(by.partial_text("#No results"))

