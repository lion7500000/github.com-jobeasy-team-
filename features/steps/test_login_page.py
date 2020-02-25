from time import sleep
from behave import given,when, then

@given ('Go to login page')
def Open_login_page(context):
    context.app.login_page.open_page()

@when ('Input wrong login {text}')
def Input_login(context,text):
    context.app.login_page.input_login(text)

@when ('Input wrong password {text}')
def Input_password(context,text):
    context.app.login_page.input_password(text)

@then ('Click on login button')
def Click_login_button (context):
    context.app.login_page.click_login_button()

    #sleep(5)
@then ('Verify {text} pop-up is here.')
def verify_error(context,text):
    context.app.login_page.verify_error(text)

    sleep(5)