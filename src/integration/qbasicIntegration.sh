#!/usr/bin/env bash

# Create output directories. If they exist, ignore the error from mkdir
mkdir out beOut 2> /dev/null

# For each day (set of frontend inputs)
for dayFolder in $(ls ./res/userinput);do

   # For each terminal (file in the day folder), run the front end.
   # This version of Qbasic automatically renames the transaction summary files generated
   # so we don't need to worry about overwriting output files
   for inFile in $(ls ./res/userinput/$dayFolder);do
      python ../frontend/main.py -v ./res/validAccountsFile.txt -o ./out < ./res/userinput/$dayFolder/$inFile
   done

   # Merge the transaction summary files after each day is run
   python tsfMerge.py ./out/mergedTsf.txt `find ./out -name *.txt`

   # Run the backend
   python ../backend/main.py -a ./res/masterAccountsFile.txt -t ./out/mergedTsf.txt -v ./beOut/validAccountsFile_$dayFolder.txt -o ./beOut/masterAccountsFile_$dayFolder.txt

   # Copy the backend outputs to the res folder so they can be used for
   # the next day
   cp ./beOut/validAccountsFile_$dayFolder.txt ./res/validAccountsFile.txt
   cp ./beOut/masterAccountsFile_$dayFolder.txt ./res/masterAccountsFile.txt

   # Clean up the output directories
#   rm ./beOut/*
   rm ./out/*
done
