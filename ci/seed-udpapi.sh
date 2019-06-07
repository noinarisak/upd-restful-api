#!/usr/bin/env bash

# Author: noi@uprisingtech.com
# Date:  2019-06-04
# Desc:
#
# ie.
# $./seed-updapi.sh
#

set -o errexit
set -o pipefail
set -o nounset
# set -o xtrace

# Set magic variables for current file & dir
__dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
__file="${__dir}/$(basename "${BASH_SOURCE[0]}")"
__base="$(basename ${__file} .sh)"
__root="$(cd "$(dirname "${__dir}")" && pwd)" # <-- change this as it depends on your app

# Helpers
red=$'\e[1;31m'
grn=$'\e[1;32m'
yel=$'\e[1;33m'
blu=$'\e[1;34m'
mag=$'\e[1;35m'
cyn=$'\e[1;36m'
end=$'\e[0m'


TARGET_ENDPOINT=http://localhost:5000/api/configs

function display() {
    printf "%b\n" "${red}==== ${1:-'NO_LABEL'} ====${end}"
}

main() {
    display "Seeding TARGET_ENDPOINT: ${TARGET_ENDPOINT}"
    curl -d "@example1.json" -H "Content-Type: application/json" -X POST ${TARGET_ENDPOINT}
    curl -d "@example2.json" -H "Content-Type: application/json" -X POST ${TARGET_ENDPOINT}
    curl -d "@example3.json" -H "Content-Type: application/json" -X POST ${TARGET_ENDPOINT}

    display "Config list"
    curl -X GET ${TARGET_ENDPOINT}
}

main
