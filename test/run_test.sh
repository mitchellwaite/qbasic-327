#!/usr/bin/env bash

# Runs pytest and dumps stdout to a log file in the "res" directory

cd test

pytest | tee "../res/$(date "+%Y%h%d_%H%M%S").log"
