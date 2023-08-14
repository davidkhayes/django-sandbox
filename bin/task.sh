#!/bin/sh

TIMESTAMP=`/bin/date "+%Y%m%d%H%M%S"`
COUNT=${1:-10}

ping -c ${COUNT} 8.8.8.8 > files/${TIMESTAMP}.TXT

exit 0

