import os
import time
import shutil
from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
from .soft_asserts import SoftAssert


class Tools:
    def __init__(self):
        load_dotenv()
        self.soft_asserts = SoftAssert()
        # Set the relative download directory path
        self.folder_name = os.getenv("DOWNLOADS_FOLDER")
        # Environment URL
        self.url = os.getenv("ENV_URL")
        # Get the absolute path to the download directory
        self.download_directory = os.path.abspath(self.folder_name)
        # Create ChromeOptions object
        chrome_options = webdriver.ChromeOptions()
        # Set the download directory in ChromeOptions
        prefs = {"download.default_directory": self.download_directory}
        chrome_options.add_experimental_option("prefs", prefs)
        # Create a Chrome WebDriver instance with the configured options
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get(self.url)
        self.driver.maximize_window()

    @staticmethod
    def get_filename_from_url(url: str) -> str:
        # For example, you need to get Zultys_Fax_2.2_x64.msi from https://ids2.zultys.com/Zultys_Fax_2.2_x64.msi
        return os.path.basename(url)

    @staticmethod
    def clear_folder(folder_path: str):
        # Clearing folder contents
        try:
            # To get all objects in folder
            file_list = os.listdir(folder_path)
            for file_name in file_list:
                file_path = os.path.join(folder_path, file_name)
                try:
                    # To delete object if it's a file
                    if os.path.isfile(file_path):
                        os.unlink(file_path)
                    # To delete object if it's a folder
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                except Exception as e:
                    print(f"Failed to delete {file_path}. Reason: {e}")
        except Exception as e:
            print(f"Failed to clear downloads folder. Reason: {e}")

    def check_object_downloading(self, target_file: str, timeout=600):
        start_time = time.time()
        file_path = os.path.join(self.download_directory, target_file)

        while time.time() - start_time < timeout:
            # Check if the target file exists in the download directory
            if os.path.isfile(file_path):
                self.driver.find_elements("tag name", "a")
                print(f"Download completed: {file_path}")
                return

            time.sleep(1)
        # In order to catch errors, and do not stop your test
        self.soft_asserts.errors.append(
            f"The file {target_file} failed to download, Timeout exceeded ({timeout} seconds)")

    def get_all_hyperlinks(self) -> list:
        return self.driver.find_elements(By.TAG_NAME, 'a')
