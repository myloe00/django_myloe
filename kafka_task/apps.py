from django.apps import AppConfig
from . import settings as app_settings
from django.conf import settings
import logging


class KafkaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'kafka'

    def ready(self):
        """配置项拆分至不同app中的settings.py"""
        # todo django启动时自动去收集相关settings（对静态文件的收集命令或许可以参考）
        # question： 继承重写的AppConfig为何无法生效
        settings_key = [key for key in dir(app_settings) if not key.startswith("__")]
        base_settings = settings.__dir__().copy()
        same_settings =  set(settings_key) & set(base_settings)
        if same_settings:
            logging.error(f"app: {self.name}，启动失败")
            raise Exception(f"配置项相同{same_settings}")
        for key in settings_key:
            setattr(settings, key, getattr(app_settings, key))
