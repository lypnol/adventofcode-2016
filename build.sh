#!/bin/bash
# set -ev
declare a CHANGED

for f in `git --no-pager diff --raw master..${TRAVIS_COMMIT} | awk 'NF>1{print $NF}'`
do
    DAY_DIRECTORY=`echo "$f" | cut -d "/" -f1`;
    if [[ $DAY_DIRECTORY == day-* ]]; then
        DAY=$(echo $DAY_DIRECTORY | cut -d'-' -f 2)
        if [[ " ${CHANGED[*]} " == *" ${DAY} "* ]]; then
            continue;
        else
            CHANGED=("${CHANGED[@]}" "${DAY}")
            python main.py -d $DAY;
        fi
    fi
done
