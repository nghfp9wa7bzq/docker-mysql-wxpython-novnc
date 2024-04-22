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

import mysql.connector as mc

from db.settings import *
from db.queries import *


class Database:
    def __init__(self):
        pass

    def get_table_names(self):
        try:
            with mc.connect(
                    host=DATABASE_HOST,
                    user=DATABASE_USER,
                    password=DATABASE_PASSWORD,
                    database=DATABASE_NAME
            ) as connection:
                try:
                    with connection.cursor() as cursor:
                        cursor.execute(GET_TABLES_QUERY)

                        result = dict()
                        index = 1
                        for data in cursor:
                            result[index] = data
                            index += 1
                        return result

                except mc.Error as e:
                    print(e)
        except mc.Error as e:
            print(e)

    def save_table_to_csv(self, table_name):
        try:
            with mc.connect(
                    host=DATABASE_HOST,
                    user=DATABASE_USER,
                    password=DATABASE_PASSWORD,
                    database=DATABASE_NAME
            ) as connection:
                try:
                    with connection.cursor() as cursor:
                        cursor.execute(create_export_to_csv_query(table_name))
                except mc.Error as e:
                    print(e)
        except mc.Error as e:
            print(e)