from behave import *
from hamcrest import assert_that, equal_to
from lib.fizzbuzz import FizzBuzz

@given('the number "{number:d}"')
def step_given_the_number_as_int(context, number):
    context.number = number

@given('the string "{some_string}"')
def step_given_the_string(context, some_string):
    context.string = some_string

@when("we run do_fizz with the number")
def step_when_we_run_do_fizz_with_the_number(context):
    fb = FizzBuzz()
    context.results = str(fb.do_fizz(context.number))

@when("we run do_fizz with the string")
def step_when_we_run_do_fizz_with_the_string(context):
    fb = FizzBuzz()
    try:
        context.results = fb.do_fizz(context.string)
    except Exception as exc:
        context.results = exc

@then('we expect back "{text}"')
def step_then_we_expect_back(context, text):
    assert_that(context.results, equal_to(text))

@then('we expect a TypeError exception')
def step_then_we_expect_typeerror_exception(context):
    assert_that(isinstance(context.results, TypeError))
