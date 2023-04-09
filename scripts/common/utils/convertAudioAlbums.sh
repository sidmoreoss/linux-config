for FILE in *;
do
echo "Working on file : "$FILE;
IFS='|' read -ra ADDR <<< "$FILE"
album="${ADDR[0]}"
file="${ADDR[1]}"
echo Creating dir : "$album"
mkdir "$album"
mv "$FILE" "$album/$file"
done
