import os

class BaseQueryReader:

    def __init__(self, curr_dir: str, sub_dir: str):
        self._current_dir = curr_dir
        self._sub_dir = sub_dir

    def _read_query(self, query):

        target_path = os.path.join(self._current_dir, 'resources', 'queries', self._sub_dir, query)

        with open(target_path, "r+") as schema_file:
            return schema_file.read()


class ManifestQueryReader(BaseQueryReader):

    def __init__(self):
        super().__init__(os.path.dirname(os.path.realpath(__file__)), 'manifest')

    def get_retrieve_import_manifest(self) -> str:
        return self._read_query('retrieve_import_manifest')

    def get_insert_manifest(self) -> str:
        return self._read_query('insert_manifest')

