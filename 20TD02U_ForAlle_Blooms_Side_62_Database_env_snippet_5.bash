# Eksempel på å sette opp MongoDB Sharding
mongod --shardsvr --replSet rs0 --dbpath /var/lib/mongo --port 27018
mongod --configsvr --replSet configReplSet --dbpath /var/lib/mongo/config --port 27019
mongos --configdb configReplSet/localhost:27019 --port 27017

# Legg til en shard
mongo --eval "sh.addShard('rs0/localhost:27018')"