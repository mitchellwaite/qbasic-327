#!/usr/bin/env bash

# For each day (set of frontend inputs)
for dayFolder in $(ls ./res/userinput);do

   # For each terminal (file in the day folder), run the front end.
   # This version of Qbasic automatically renames the transaction summary files generated
   # so we don't need to worry about overwriting output files
   for inFile in $(ls ./res/userinput/$dayFolder);do
      python ../frontend/main.py -v ./res/validAccountsFile.txt -o ./out < ./res/userinput/$dayFolder/$inFile
   done

   # Merge the transaction summary files after each day is run
   python tsfMerge.py ./out/mergedTsf.txt `ls ./out/`

   # Run the backend
   python ../backend/main.py -a ./res/masterAccountsFile.txt -t ./out/mergedTsf.txt -v ./beOut/validAccountsFile.txt -o ./beOut/masterAccountsFile.txt

   # Copy the backend outputs to the res folder so they can be used for
   # the next day
   cp ./beOut/validAccountsFile.txt ./res/validAccountsFile.txt
   cp ./beOut/masterAccountsFile.txt ./res/masterAccountsFile.txt

   # Clean up the output directories
   rm ./beOut/*
   rm ./out/*
done
