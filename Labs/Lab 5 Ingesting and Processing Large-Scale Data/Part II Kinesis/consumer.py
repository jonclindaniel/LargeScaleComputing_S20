
import boto3
import time
import json

kinesis = boto3.client('kinesis', region_name='us-east-1')

shard_it = kinesis.get_shard_iterator(StreamName = "test_stream",
                                     ShardId = 'shardId-000000000000',
                                     ShardIteratorType = 'LATEST'
                                     )["ShardIterator"]

i = 0
s = 0
while 1==1:
    out = kinesis.get_records(ShardIterator = shard_it,
                              Limit = 1
                             )
    for o in out['Records']:
        jdat = json.loads(o['Data'])
        s = s + len(set(jdat['tweet'].split()))
        i = i + 1

    if i != 0:
        print("Average Unique Word Count Per Tweet: " + str(s/i))
        print("Sample of Current Tweet: " + jdat['tweet'][:20])
        print("\n")
        
    shard_it = out['NextShardIterator']
    time.sleep(0.2)
