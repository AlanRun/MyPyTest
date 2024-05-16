import allure
import pytest

from common.log_util import my_log


class AssertUtil:
    def __init__(self):
        self.log = my_log('AssertUtil')

    def assert_code(self):
        pass

    @allure.step("Verify {expected} is equal to {actual}")
    def equal_to(self, expected, actual):
        pytest.assume(expected == actual, f"Expected: '{expected}', != Actual: '{actual}'")

    @allure.step("Verify {expected} is not equal to {actual}")
    def not_equal_to(self, expected, actual):
        pytest.assume(expected != actual, f"Expected: '{expected}', == Actual: '{actual}'")

    @allure.step("Verify {expected} is greater than {actual}")
    def greater_than(self, expected, actual):
        pytest.assume(expected > actual, f"Expected: '{expected}', Actual: '{actual}'")

    @allure.step("Verify {expected} is greater than or equal to {actual}")
    def greater_than_or_equal_to(self, expected, actual):
        pytest.assume(expected >= actual, f"Expected: '{expected}', Actual: '{actual}'")

    @allure.step("Verify {expected} is less than {actual}")
    def less_than(self, expected, actual):
        pytest.assume(expected < actual, f"Expected: '{expected}', Actual: '{actual}'")

    @allure.step("Verify {expected} is less than or equal to {actual}")
    def less_than_or_equal_to(self, expected, actual):
        pytest.assume(expected <= actual)

    @allure.step("Verify {actual} is true")
    def is_true(self, actual):
        pytest.assume(actual)

    @allure.step("Verify {actual} is false")
    def is_false(self, actual):
        pytest.assume(not actual)

    @allure.step("Verify {actual} is None")
    def is_none(self, actual):
        pytest.assume(actual is None)

    @allure.step("Verify {actual} is not None")
    def is_not_none(self, actual):
        pytest.assume(actual is not None)

    @allure.step("Verify {actual} is empty")
    def is_empty(self, actual):
        pytest.assume(not actual)

    @allure.step("Verify {actual} is not empty")
    def is_not_empty(self, actual):
        pytest.assume(bool(actual))

    @allure.step("Verify {expected} is in {actual}")
    def is_in(self, expected, actual):

        pytest.assume(expected in actual, f"Expected: '{expected}', not in Actual: '{actual}'")

    @allure.step("Verify {expected} is not in {actual}")
    def is_not_in(self, expected, actual):
        pytest.assume(expected not in actual, f"Expected: '{expected}', in Actual: '{actual}'")

    @allure.step("Verify {expected} is instance of {actual}")
    def is_instance_of(self, expected, actual):
        pytest.assume(isinstance(expected, actual))

    @allure.step("Verify {expected} is not instance of {actual}")
    def is_not_instance_of(self, expected, actual):
        pytest.assume(not isinstance(expected, actual))

    @allure.step("Verify {actual} is close to {expected}")
    def is_close_to(self, expected, actual):
        pytest.assume(abs(expected - actual) < 0.001)

    @allure.step("Verify {expected} is not close to {actual}")
    def is_not_close_to(self, expected, actual):
        pytest.assume(abs(expected - actual) >= 0.001)

    @allure.step("Verify {expected} is equal to {actual} within {delta}")
    def equal_to_with_delta(self, expected, actual, delta):
        pytest.assume(abs(expected - actual) <= delta)

    @allure.step("Verify {expected} is not equal to {actual} within {delta}")
    def not_equal_to_with_delta(self, expected, actual, delta):
        pytest.assume(abs(expected - actual) > delta)

    @allure.step("Verify {expected} is greater than {actual} within {delta}")
    def greater_than_with_delta(self, expected, actual, delta):
        pytest.assume(expected - actual > delta)

    @allure.step("Verify {expected} is greater than or equal to {actual} within {delta}")
    def greater_than_or_equal_to_with_delta(self, expected, actual, delta):
        pytest.assume(expected - actual >= delta)

    @allure.step("Verify {expected} is less than {actual} within {delta}")
    def less_than_with_delta(self, expected, actual, delta):
        pytest.assume(actual - expected > delta)

    @allure.step("Verify {expected} is less than or equal to {actual} within {delta}")
    def less_than_or_equal_to_with_delta(self, expected, actual, delta):
        pytest.assume(actual - expected >= delta)

