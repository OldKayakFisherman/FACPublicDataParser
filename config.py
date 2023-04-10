import os
from dotenv import load_dotenv

load_dotenv()


class Settings:

    def __init__(self):
        self._zip_url = os.getenv("ZIP_URL")
        self._output_dir = os.getenv("OUTPUT_DIR")
        self._zip_file = os.getenv("ZIP_FILE")
        self._zip_dir = os.getenv("ZIP_DIR")
        self._refresh_files = os.getenv("REFRESH_FILES")

    def get_zip_url(self) -> str:
        return self._zip_url

    def get_output_dir(self) -> str:
        return self._output_dir

    def get_zip_file(self) -> str:
        return self._zip_file

    def get_zip_dir(self) -> str:
        return self._zip_dir

    def get_refresh_files(self) -> bool:
        return self._refresh_files
