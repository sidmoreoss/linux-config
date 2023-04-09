#!/bin/bash

parent_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )
cd "$parent_path" || exit 1

echo
tput setaf 3;echo "---------------------------------------------------------------";tput sgr0;
tput setaf 2;echo ".................  Installing Binaries  .......................";tput sgr0;
tput setaf 3;echo "---------------------------------------------------------------";tput sgr0;

# setting global path to ensure binaries work
sudo ../scripts/common/set_global_PATH || exit;

# move the binaries to bin
mkdir -p $HOME/.local/bin/ || exit 1
cp -uv `ls | grep -v install.sh` $HOME/.local/bin/ || exit 1

# set execute permission to the binaries
cd $HOME/.local/bin/ || exit;
sudo chmod +x * || exit;
