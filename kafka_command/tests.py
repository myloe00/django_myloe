#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022-07-26 5:02 PM
# @Author  : myloe
# @File    : tests.py
import json
import time

from kafka import KafkaProducer
server = "192.168.0.201"
port = 9092
version = "2.8.1"
print(tuple([int(i) for i in version.split(".")]))
print(f"{server}:{port}")
producer = KafkaProducer(
    bootstrap_servers=f"{server}:{port}",  api_version=tuple([int(i) for i in version.split(".")])
)
future = producer.send("test", value=json.dumps({"a": 2, "b": 2}).encode())
# send为异步操作
future.get()
print("111")