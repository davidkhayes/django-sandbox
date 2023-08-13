#!/bin/sh

TIMESTAMP=`/bin/date "+%Y%m%d%H%M%S"`

ping -c 10 8.8.8.8 > files/${TIMESTAMP}.TXT

exit 0

