#!/usr/bin/env sh

curl -sSk -XPOST localhost:8080/v1/echo -d '{"name": "lukas"}'

# vim: set sw=4 ts=4 sts=4 et ai
