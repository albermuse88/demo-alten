from behave import step, use_step_matcher

from page_object.po_aeronautic import AeronauticPage

use_step_matcher('re')


@step("user verifies the next text '(?P<text>.+)' in the screen aeronautic")
def verify_text(context, text):
    context.page = AeronauticPage(context.driver)
    context.page.verify_text(text)
