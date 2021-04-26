#! /usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from robot.api import Failure
from robot.api import logger


class TodoMVC:
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def connect(self, url):
        self._driver = webdriver.Chrome()
        self._driver.implicitly_wait(10)
        self._driver.get(url)

    def done_task(self, task):
        todo_lists = self._driver.find_elements_by_css_selector(
            "ul.todo-list>li")
        for i in todo_lists:
            if i.find_element_by_tag_name("label").text == task:
                i.find_element_by_css_selector("input.toggle").click()

    # Timeout Error occur if not found
    def clear_completed_button_appear(self):
        self._driver.find_element_by_css_selector("button.clear-completed")

    def is_task_completed(self, task):
        todo_lists = self._driver.find_elements_by_css_selector(
            "ul.todo-list>li.completed label")
        result = False
        for i in todo_lists:
            if i.text == task:
                result = True
        if not result:
            raise Failure("Task {name:s} is not completed".format(name=task))

    def get_item_amount(self):
        return self._driver.find_element_by_css_selector("footer span.todo-count strong").text

    def create_new_task(self, task):
        textbox = self._driver.find_elements_by_css_selector("input.new-todo")
        textbox[0].send_keys(task, Keys.ENTER)

    def task_should_exist(self, task):
        todo_lists = self._driver.find_elements_by_css_selector(
            "ul.todo-list>li")
        found = False
        for i in todo_lists:
            if i.find_element_by_tag_name("label").text == task:
                found = True
        if not found:
            raise Failure("Task " + task + " should exist in Todo list")

    def there_are_task(self, tasks):
        for i in tasks:
            self.create_new_task(i)

    def amount_of_task_is(self, amount):
        todos = self._get_todo()
        if len(todos) != int(amount):
            raise Failure("There should be {expected:s} todos. (found {actual:d})".format(
                expected=amount, actual=len(todos)))

    def todo_is_empty(self):
        if len(self._get_todo()) == 0:
            return
        driver = self._driver

        toggle = driver.find_element_by_css_selector('label[for=toggle-all]')
        toggle.click()

        clear_completed = driver.find_element_by_css_selector(
            "button.clear-completed")
        clear_completed.click()

    def quit(self):
        self._driver.quit()

    def _get_todo(self):
        list = []
        self._driver.implicitly_wait(1)
        todo_lists = self._driver.find_elements_by_css_selector(
            "ul.todo-list>li")
        self._driver.implicitly_wait(10)
        for i in todo_lists:
            list.append(i.find_element_by_tag_name("label").text)
        return list
