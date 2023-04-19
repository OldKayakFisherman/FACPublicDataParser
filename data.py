from config import Settings;
class DataImport:

    def __init__(self):
        self._settings = Settings()
        self._dsn = self._settings.