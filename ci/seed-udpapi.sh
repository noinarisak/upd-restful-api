#!/usr/bin/env bash

# Author: noi@uprisingtech.com
# Date:  2019-06-04
# Desc:
#
# ie.
# $./seed-updapi.sh http://localhost:5000
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

arg_api_host="${1:-http://localhost:5000}"

# Helpers
red=$'\e[1;31m'
grn=$'\e[1;32m'
yel=$'\e[1;33m'
blu=$'\e[1;34m'
mag=$'\e[1;35m'
cyn=$'\e[1;36m'
end=$'\e[0m'

API_ENDPOINT=${arg_api_host}/api/configs

function display() {
    printf "%b\n" "${red}==== ${1:-'NO_LABEL'} ====${end}"
}

main() {
    display "Seeding API_ENDPOINT: ${API_ENDPOINT}"
    curl -d "@example1.json" -H "Content-Type: application/json" -X POST ${API_ENDPOINT}
    curl -d "@example2.json" -H "Content-Type: application/json" -X POST ${API_ENDPOINT}
    curl -d "@example3.json" -H "Content-Type: application/json" -X POST ${API_ENDPOINT}

    display "Config list: ${API_ENDPOINT}"
    curl -X GET ${API_ENDPOINT}

    display "GET .well-known/default-setting"
    SUB_DOMAIN_EXAMPLE_1_ENDPOINT=${API_ENDPOINT}/example_1/something/.well-known/default-setting
    curl -X GET ${SUB_DOMAIN_EXAMPLE_1_ENDPOINT}
}

main
