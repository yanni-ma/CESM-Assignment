#!/bin/bash

module purge
module load gcc

cd dat

echo "check_certificate = off" >> ~/.wgetrc

wget https://ftp.gnu.org/pub/gnu/ncurses/ncurses-6.1.tar.gz
tar xfz ncurses-6.1.tar.gz
cd ncurses-6.1
./configure --with-shared --prefix=/home/cc/cesm/apps
make -j 24
make install
cd ..
rm -rf ncurses-6.1
rm ncurses-6.1.tar.gz

git clone https://github.com/tcsh-org/tcsh
cd tcsh
./configure --prefix=/home/cc/cesm/apps
make -j 24
make install
cd ..
rm -rf tcsh
cd /home/cc/cesm/apps/bin
ln -s tcsh csh


