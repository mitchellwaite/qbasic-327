#!/usr/bin/env bash

# Runs pytest and dumps stdout to a log file in the "res" directory

cd test

datecode=$(date "+%Y%h%d_%H%M%S")

pytest -rapP --junitxml ../res/$datecode.xml | tee "../res/$datecode.log"
