from utils.tools import Tools


class ButtonsPage(Tools):
    def __init__(self):
        super().__init__()

    def check_hyperlink_definition(self):
        # Get all hyperlinks on a current page.
        hyperlinks = self.get_all_hyperlinks()
        for hyperlink in hyperlinks:
            href = hyperlink.get_attribute('href')
            text = hyperlink.text
            # Checking if it's download link (Easy to extend this check, if there are other file extensions.)
            if href.endswith(('.msi', '.exe')):
                # Click on object in UI
                hyperlink.click()
                self.check_object_downloading(target_file=self.get_filename_from_url(href))
            # If it's not, then just print
            else:
                print(f"Link object: {text}, URL: {href}")
