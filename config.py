import os
import re

class CONFIG:
  host="127.0.0.1",
  http_port=7474,
  user="neo4j",  # 数据库user name，如果没有更改过，应该是neo4j
  password="123456"


# 读取环境变量,更新到Config后，以和容器一起使用
for k in os.environ:
  if k in CONFIG.__dict__:
    print('use environ var:',k,os.environ.get(k))
    setattr(CONFIG, k, os.environ.get(k))
