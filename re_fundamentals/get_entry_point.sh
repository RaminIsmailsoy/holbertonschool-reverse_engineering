#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Usage: $0 <ELF_file>"
    exit 1
fi

file_name="$1"

if [ ! -f "$file_name" ]; then
    echo "Error: File '$file_name' does not exist."
    exit 1
fi

if ! readelf -h "$file_name" >/dev/null 2>&1; then
    echo "Error: '$file_name' is not a valid ELF file."
    exit 1
fi

source messages.sh

magic_number=$(readelf -h "$file_name" | awk -F: '/Magic:/ {gsub(/^[ \t]+/, "", $2); print $2}')
class=$(readelf -h "$file_name" | awk -F: '/Class:/ {gsub(/^[ \t]+/, "", $2); print $2}')
byte_order=$(readelf -h "$file_name" | awk -F: '/Data:/ {gsub(/^[ \t]+/, "", $2); print $2}')
entry_point_address=$(readelf -h "$file_name" | awk -F: '/Entry point address:/ {gsub(/^[ \t]+/, "", $2); print $2}')

display_elf_header_info
