from behave import step, use_step_matcher

from page_object.po_public_administration import PublicAdministrationPage

use_step_matcher('re')


@step("user verifies the next text '(?P<text>.+)' in the screen public administration")
def verify_text(context, text):
    context.page = PublicAdministrationPage(context.driver)
    context.page.verify_text(text)
