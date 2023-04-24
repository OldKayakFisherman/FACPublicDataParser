from config import Settings;



class AuditManifest:
    def get_dbkey(self):
        return self._dbkey
    def set_dbkey(self, dbkey):
        self._dbkey = dbkey
    def get_audityear(self):
        return self._audityear
    def set_audityear(self, audityear):
        self._audityear = audityear
    def get_firewall_date(self):
        return self._firewall_date
    def set_firewall_date(self, firewall_date):
        self._firewall_date = firewall_date
    def get_previous_firewall_date(self):
        return self._previous_firewall_date
    def set_previous_firewall_date(self, previous_firewall_date):
        self._previous_firewall_date = previous_firewall_date

class DataManifestResolver:

    def __init__(self, dsn):
        self._dsn = dsn

    def get_manifest_resolver(self, dbkey, audityear):
        






class DataImport:

    def __init__(self, dsn):
      self._dsn = dsn;

    def import_general(self, records):

        print("DbKey: %s, AuditYear: %s, and Firewall Date: %s, Previous Firewall Date: %s"
              % (records[0][1], records[0][0], records[0][58], records[0][59]))
