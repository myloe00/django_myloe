#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022-07-22 5:24 PM
# @Author  : myloe
# @File    : start_consumer.py

from django.core.management.base import BaseCommand
from django.conf import settings
from gevent.pool import Pool
from kafka_command.consumer_task import Add
from kafka import KafkaConsumer


class Command(BaseCommand):
    help = "开启消费者"

    def add_arguments(self, parser):
        parser.add_argument("topic", type=str)
        parser.add_argument("--multi", default=1, type=int)
        parser.add_argument("--group_id", default="normal_task", type=str)

    def handle(self, *args, **options):
        pools = Pool(options.get("multi"))
        topic = options.get("topic")
        group_id = options.get("group_id")
        print(topic)
        bootstrap_servers = f"{settings.SERVER}:{settings.PORT}"
        print(bootstrap_servers)
        consumer = KafkaConsumer(topic, group_id=group_id, bootstrap_servers=bootstrap_servers, api_version=tuple([int(i)  for i in settings.VERSION.split(".")]))
        print("起动消费者")
        while True:
            for msg in consumer:
                print("11111111")
                print(msg)
                pools.spawn(Add().do, 1, 2)

