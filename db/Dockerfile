#    Copyright (C) 2024  nghfp9wa7bzq@gmail.com

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.


FROM mysql:8 AS db-runner

ARG DB_USER_PASSWORD_FILE
ARG DOCKER_USER_NAME
ARG DOCKER_DB_NAME

# Load sample database.
RUN set -eux; \
    microdnf install -y unzip; \
    microdnf clean all

RUN curl -fL --retry 5 -o /tmp/sakila-db.zip "https://downloads.mysql.com/docs/sakila-db.zip"
RUN unzip /tmp/sakila-db.zip -d /tmp/

RUN cp /tmp/sakila-db/sakila-schema.sql /docker-entrypoint-initdb.d/01sakila-schema.sql
RUN cp /tmp/sakila-db/sakila-data.sql /docker-entrypoint-initdb.d/02sakila-data.sql

# Create non-root database user and set permissions.

# FILE permission is needed for easy CSV export.
# https://dev.mysql.com/doc/refman/8.3/en/privileges-provided.html#priv_file
# Also needed:
# https://dev.mysql.com/doc/refman/8.3/en/server-system-variables.html#sysvar_secure_file_priv
RUN --mount=type=secret,required=true,id=db-user-password set -eu; \
    { \
        echo "CREATE USER \"${DOCKER_USER_NAME}\"@\"%\" IDENTIFIED BY \"$(cat ${DB_USER_PASSWORD_FILE})\";"; \
        echo "GRANT SELECT ON ${DOCKER_DB_NAME}.* TO \"${DOCKER_USER_NAME}\"@\"%\";"; \
#        echo "GRANT FILE ON *.* TO \"${DOCKER_USER_NAME}\"@\"%\";"; \
    } > /docker-entrypoint-initdb.d/03user-setup.sql

# Remove 03user-setup.sql file, because it contains a password.
RUN set -eu; \
    { \
        echo "#!/bin/bash"; \
        echo "rm /docker-entrypoint-initdb.d/03user-setup.sql"; \
    } > /docker-entrypoint-initdb.d/04user-setup-remove.sh