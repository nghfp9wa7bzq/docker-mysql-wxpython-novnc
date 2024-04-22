"""
    Copyright (C) 2024  nghfp9wa7bzq@gmail.com

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from db.settings import *

GET_TABLES_QUERY = "SHOW TABLES;"


def create_export_to_csv_query(table_name):
    return """
        SELECT *
        INTO OUTFILE '/tmp/""" + table_name + """.csv'
        FIELDS TERMINATED BY ','
        ENCLOSED BY '"'
        LINES TERMINATED BY '\n'
        FROM """ + table_name + """;
    """
