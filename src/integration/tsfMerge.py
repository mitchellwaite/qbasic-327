import sys

mergedArr = []

for i in range(2,len(sys.argv)):
    try:
        # Get an array of the transaction summary file
        tmpArr = []
        with open(sys.argv[i], 'r') as iFile:
            tmpArr = iFile.read().splitlines()

        # Check that the last element is deposit
        if not tmpArr[len(tmpArr) - 1].startswith("EOS"):
            raise Exception("Last transaction not EOS")

        # Remove the EOS at the end
        del tmpArr[len(tmpArr) - 1]
        mergedArr.extend(tmpArr)
    except Exception as e:
        print str(e)

# Append an EOS to the merged transaction summary file
mergedArr.append("EOS 0000000 000 0000000 ***")

with open(sys.argv[1], 'w') as oFile:
    for item in mergedArr:
        oFile.write("%s\n" % item)
