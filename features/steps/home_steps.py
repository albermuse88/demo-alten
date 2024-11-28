from behave import step, use_step_matcher

from page_object.po_home import HomePage

use_step_matcher('re')


@step("user navigating to the website '(?P<url>.+)'")
def access_website(context, url):
    context.page = HomePage(context.driver)
    context.page.access_website(url)


@step("user clicks on the main section of sectors")
def access_main_section_sectors(context):
    context.page.access_main_section_sectors()


@step("user clicks on the section public administration")
def access_section_public_administration(context):
    context.page = HomePage(context.driver)
    context.page.access_section_public_administration()


@step("user clicks on the section aeronautic")
def access_section_aeronautic(context):
    context.page = HomePage(context.driver)
    context.page.access_section_aeronautic()
