#!/bin/bash
#ping a list of servers 

textfile=$1
if [[ '' == $textfile ]]; then
    echo "Please Enter a File Name After Cmd"
    exit 1
fi

sed '/^$/d' $textfile > output_18972.txt
listofips=$(cat output_18972.txt)

for entry in ${listofips[@]}; do
	ping -c 2 $entry | grep -o '[0-9] packets received' >> outputping_18972.txt
    echo "Running Ping: $entry"
done

paste -d '|' output_18972.txt outputping_18972.txt > final_18972.txt
rm outputping_18972.txt
rm output_18972.txt

echo Good >> Good_18972.txt
echo Bad >> Bad_18972.txt

grep "2 packets received" final_18972.txt | sed 's/\|2 packets received//' >> Good_18972.txt
grep "0 packets received" final_18972.txt | sed 's/\|0 packets received//' >> Bad_18972.txt

rm final_18972.txt

paste -d ',' Good_18972.txt Bad_18972.txt >> final.csv
rm Good_18972.txt
rm Bad_18972.txt

echo "Done! final.csv"


