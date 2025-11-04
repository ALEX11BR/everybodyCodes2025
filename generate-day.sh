#!/usr/bin/env sh
cd "$(dirname $(readlink -f "$0") )"

PreviousDay=$(ls . | grep 'd[0-9]\+' | tr --delete d | sort --numeric-sort | tail --lines 1)

cp -r d1 d"$(expr "$PreviousDay" + 1)"
