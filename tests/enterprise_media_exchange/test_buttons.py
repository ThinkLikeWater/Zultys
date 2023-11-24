import unittest
from pages.button_page import ButtonsPage


class TestButtons(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.buttons_page = ButtonsPage()
        # Clearing the contents of the downloads folder
        cls.buttons_page.clear_folder(cls.buttons_page.download_directory)

    @classmethod
    def tearDownClass(cls):
        cls.buttons_page.driver.quit()
        # Catching errors
        cls.buttons_page.soft_asserts.assert_all()

    def test_01_hyperlink_check(self):
        self.buttons_page.check_hyperlink_definition()


if __name__ == "__main__":
    unittest.main()
