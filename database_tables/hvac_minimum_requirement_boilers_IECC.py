import sqlite3

from database_tables.hvac_minimum_requirement_boilers import HVACMinReqBoilers

TABLE_NAME = "hvac_minimum_requirement_boilers_IECC"


class HVACMinReqBoilersIECCTable(HVACMinReqBoilers):
    def __init__(self):
        super(HVACMinReqBoilersIECCTable, self).__init__(
            table_name=TABLE_NAME,
            initial_data_directory=f"database_files/{TABLE_NAME}",
        )
