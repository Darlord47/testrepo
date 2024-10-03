#!/bin/bash

get_size(){
  echo $(du -hs "$1" | cut -f1)
}

result=()
for i in $(ls -A); do
  result+=("$(get_size $i) $i")
done

printf "%s\n" "${result[@]}" | sort -rh