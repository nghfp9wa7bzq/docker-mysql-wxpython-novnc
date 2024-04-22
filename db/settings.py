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

DATABASE_HOST = "docker-mysql-wxpython-novnc-db-1"
DATABASE_USER = "docker"
DATABASE_PASSWORD = ""
DATABASE_NAME = "sakila"

if not DATABASE_PASSWORD:
    # dev
    # file_path = "secrets/db_user_password.txt"
    # with docker
    file_path = "/run/secrets/db-user-password"
    with open(file_path, "r") as psw_file:
        DATABASE_PASSWORD = psw_file.read().strip()
