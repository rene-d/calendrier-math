#!/usr/bin/env bash

# script pour lancement localement le site avec le thème Jekyll Tactile

docker build -t cal-math-2021 .
docker run --rm -ti -v $PWD:/site -p 4000:4000 -w /site cal-math-2021
