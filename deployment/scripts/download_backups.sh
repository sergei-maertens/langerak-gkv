#!/bin/bash

USER=$1
HOST=$2
BASE=/home/konkerk/backup
DEST=/tmp

day=$3

download_django() {
    backup_file=koningskerk.custom
    scp $USER@$HOST:$BASE/postgres/$day-daily/$backup_file $DEST/$backup_file
}

download() {
    download_django
}

download $3
