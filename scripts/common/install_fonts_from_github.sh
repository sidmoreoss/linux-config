#!/bin/bash

mkdir -p ~/.fonts/ || echo "Failed to create ~/.fonts/ directory" && exit;

cd ~/.fonts || exit;


echo
tput setaf 3;echo "Installing Source-Sans (Adobe Font)";tput sgr0;

wget -q --show-progress -N https://github.com/adobe-fonts/source-sans/archive/release.zip

unzip release.zip

rm release.zip


echo
tput setaf 3;echo "Installing Source-Serif (Adobe Font)";tput sgr0;

wget -q --show-progress -N https://github.com/adobe-fonts/source-serif/archive/release.zip

unzip release.zip

rm release.zipm
