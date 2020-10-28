#!/bin/bash

#setting up git
#https://www.atlassian.com/git/tutorials/setting-up-a-repository/git-config

echo "Setting credentials for SiddharthMMore@outlook.com"

git config --global pull.rebase false
git config --global push.default simple
git config --global user.name "Siddharth More"
git config --global user.email "SiddharthMMore@outlook.com"
sudo git config --system core.editor nano
git config --global credential.helper cache
git config --global credential.helper 'cache --timeout=32000'

echo "###########################################################"
echo "Github credentials have been set"
echo "Delete the ~/.cache/git folder if you made a mistake or"
echo "if you want to switch to your personal github"
echo "###########################################################"

echo "################################################################"
echo "###################    T H E   E N D      ######################"
echo "################################################################"
