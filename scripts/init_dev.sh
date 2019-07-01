#docker-compose run web manage loaddata develop_1
#docker-compose run web manage loaddata develop_2

docker-compose run --rm web scripts/init_dev_inner.sh
