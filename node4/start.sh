nohup geth \
    --datadir . \
    --port 30314 \
    --bootnodes "enode://cb07f0b11991022b6003a98f432b1bd628a538a57103d8abcfc8df76117581fd186eb85f23b915b8cafe34aa2b7c10e43ece1991cf90bf8cfe2a501f8eeb095d@127.0.0.1:0?discport=30311" \
    --networkid 23452 \
    --unlock 0x763f028d36bdb0ecc5359dc537dc13905e85d19c \
    --password password.txt \
    --authrpc.port 8554 \
    > node.logs 2>&1 &
