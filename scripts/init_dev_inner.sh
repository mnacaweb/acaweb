# cat das_portal/fixtures/develop.sql | ./manage dbshell

cat scripts/data/initial.sql | ./manage dbshell
mkdir -p media
chmod 777 media
cd media
rm -rf *
tar -xvzf ../scripts/data/initial.tgz
