class SoftAssert:
    # For soft error catching.
    def __init__(self):
        self.errors = []

    def assert_equal(self, actual, expected, message=None):
        try:
            assert actual == expected
        except AssertionError as e:
            self.errors.append(f"AssertionError: {message}. Actual: {actual}, Expected: {expected}")

    def assert_true(self, condition, message=None):
        try:
            assert condition
        except AssertionError as e:
            self.errors.append(f"AssertionError: {message}. Condition: {condition}")

    def assert_false(self, condition, message=None):
        try:
            assert not condition
        except AssertionError as e:
            self.errors.append(f"AssertionError: {message}. Condition: {condition}")

    def assert_contains(self, actual, expected, message=None):
        try:
            assert expected in actual
        except AssertionError as e:
            self.errors.append(f"AssertionError: {message}. Actual: {actual}, Expected to contain: {expected}")

    def assert_not_contains(self, actual, unexpected, message=None):
        try:
            assert unexpected not in actual
        except AssertionError as e:
            self.errors.append(f"AssertionError: {message}. Actual: {actual}, Expected not to contain: {unexpected}")

    def assert_list_equal(self, actual_list, expected_list, message=None):
        try:
            assert actual_list == expected_list
        except AssertionError as e:
            self.errors.append(f"AssertionError: {message}. Actual List: {actual_list}, Expected List: {expected_list}")

    def assert_dict_equal(self, actual_dict, expected_dict, message=None):
        try:
            assert actual_dict == expected_dict
        except AssertionError as e:
            self.errors.append(f"AssertionError: {message}. Actual Dictionary: {actual_dict}, Expected Dictionary: {expected_dict}")

    def assert_length(self, actual, expected_length, message=None):
        try:
            assert len(actual) == expected_length
        except AssertionError as e:
            self.errors.append(f"AssertionError: {message}. Actual Length: {len(actual)}, Expected Length: {expected_length}")

    def assert_not_none(self, value, message=None):
        try:
            assert value is not None
        except AssertionError as e:
            self.errors.append(f"AssertionError: {message}. Value is None.")

    def assert_none(self, value, message=None):
        try:
            assert value is None
        except AssertionError as e:
            self.errors.append(f"AssertionError: {message}. Value is not None.")

    def assert_raises(self, exception_type, func, *args, **kwargs):
        try:
            func(*args, **kwargs)
            self.errors.append(f"AssertionError: Expected exception {exception_type}, but none was raised.")
        except exception_type as e:
            pass

    def assert_all(self):
        assert not self.errors, f"Soft assert errors: {self.errors}"
