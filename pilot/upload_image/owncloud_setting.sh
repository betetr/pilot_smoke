#!/bin/bash

OWNCLOUD_HTTP_PROTOCAL="http"
OWNCLOUD_HOST="172.16.1.97"
OWNCLOUD_API_PORT="8080"

OWNCLOUD_SERVICE_ADDRESS="${OWNCLOUD_HTTP_PROTOCAL}://${OWNCLOUD_HOST}:${OWNCLOUD_API_PORT}"
OWNCLOUD_FILE_API="${OWNCLOUD_HTTP_PROTOCAL}://${OWNCLOUD_HOST}:${OWNCLOUD_API_PORT}/remote.php/webdav"
OWNCLOUD_SHARE_API="${OWNCLOUD_HTTP_PROTOCAL}://${OWNCLOUD_HOST}:${OWNCLOUD_API_PORT}/ocs/v1.php/apps/files_sharing/api/v1/shares"

OWNCLOUD_USERNAME="yayuanx"
OWNCLOUD_PASSWORD="123456"