import logging as log

from apscheduler.schedulers.background import BackgroundScheduler
from flask import Response
import requests

from src.common.http_server import HttpServer
from src.utils.utils import increase_cpu

GET_COFFEE_ENDPOINT = '/get_coffee'


class CoffeeMachine(HttpServer):

    def __init__(self, name: str = 'The Coffee Machine', host: str = 'localhost', port: int = 8084,
                 machine_svc_host: str = 'localhost', machine_svc_port: int = 9090, cpu_increase_interval: int = 60,
                 cpu_increase_duration: int = 5, cpu_increase_threads: int = 500):
        super().__init__(name, host, port)
        self.cpu_increase_interval = cpu_increase_interval
        self.cpu_increase_duration = cpu_increase_duration
        self.cpu_increase_threads = cpu_increase_threads
        self.machine_svc_host = machine_svc_host
        self.machine_svc_port = machine_svc_port

        self.add_all_endpoints()

        # Increase CPU usage for some time
        if self.cpu_increase_duration is not None:
            self.scheduler = BackgroundScheduler()
            self.scheduler.add_job(increase_cpu, 'interval', [self.cpu_increase_duration, self.cpu_increase_threads],
                                   minutes=self.cpu_increase_interval)
            self.scheduler.start()

    def add_all_endpoints(self):
        self.add_endpoint(endpoint=GET_COFFEE_ENDPOINT, endpoint_name='espresso', handler=self.prepare_coffee)

    def prepare_coffee(self, data):
        log.info('Preparing espresso coffee')

        coffee_machine_svc_url = 'http://{}:{}{}'.format(self.machine_svc_host, self.machine_svc_port,
                                                         '/prepare_coffee')

        coffee_status = requests.post(url=coffee_machine_svc_url, json=data)

        if coffee_status.status_code == 200:
            log.info('Coffee done')
            return Response(coffee_status.text, status=coffee_status.status_code, mimetype='application/json')
        else:
            log.error('Missing some ingredients')
            return Response(coffee_status.text, status=coffee_status.status_code, mimetype='application/json')
