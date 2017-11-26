#!/usr/bin/env bash

# Cleans up the res directory to an initial state
rm ./res/masterAccountsFile.txt
rm ./res/validAccountsFile.txt

# Removes any leftover files from the output directories
rm ./out/*
rm ./beOut/*

# Recreates blank master/valid accounts files
touch ./res/masterAccountsFile.txt
echo "0000000" > ./res/validAccountsFile.txt
