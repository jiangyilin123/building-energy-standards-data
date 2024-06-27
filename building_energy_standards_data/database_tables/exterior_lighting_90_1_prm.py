import sqlite3

from building_energy_standards_data.database_tables.exterior_lighting_definition import (
    ExtLightDef,
)

TABLE_NAME = "exterior_lighting_90_1_prm"


class ExtLightDef901PRMTable(ExtLightDef):
    def __init__(self):
        super(ExtLightDef901PRMTable, self).__init__(
            table_name=TABLE_NAME,
            initial_data_directory=f"building_energy_standards_data/database_files/{TABLE_NAME}",
        )