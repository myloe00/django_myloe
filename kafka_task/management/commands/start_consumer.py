#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022-07-22 5:24 PM
# @Author  : myloe
# @File    : start_consumer.py
from django.core.management.base import BaseCommand
from gevent.pool import Pool
from kafka_task.consumer_task import Task
from kafka import KafkaConsumer
from django.conf import settings

class Command(BaseCommand):
    help = "开启消费者"

    def add_arguments(self, parser):
        parser.add_argument("--multi", default=1, type=int)
        parser.add_argument("--topic", type=str)

    def handle(self, *args, **options):
        pools = Pool(options.get("multi"))
        topic = options.get("topic")
        consumer = KafkaConsumer(topic, group_id="normal_task", bootstrap_servers=f"{settings.server}:{settings.port}")
        consumer.assign(topic)
        with True:
            pools.spawn(Task().do, 1, 2)

