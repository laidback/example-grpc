#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from concurrent import futures
import logging as log
import os
import sys
import yaml
import time
import grpc
import greeter
import grpctest_pb2_grpc

loc = os.path.dirname(__file__)
CONFFILE = os.getenv('GRPCTEST_SERVER_CONFFILE', loc + '/config.yml')
DEBUG = os.getenv('GRPCTEST_SERVER_DEBUG', None)


def load_config():
    '''Load Yaml config based on the env'''
    try:
        with open(CONFFILE, 'r') as ymlfile:
            config = yaml.load(ymlfile)['server']
            log.info('Successfully loaded config file: {}'.format(CONFFILE))
    except Exception as error:
        log.error('Error loading config file: {} \nwith Error: {}'.format(CONFFILE, error))
        sys.exit(1)
    return config

def setup_log():
    '''setup logging'''
    log_level = log.DEBUG if DEBUG else log.INFO
    log_format = '%(asctime)s %(levelname)-8s %(message)s'
    log_datefmt = '%a, %d %b %Y %H:%M:%S'
    log.basicConfig(level=log_level, format=log_format, datefmt=log_datefmt)
    return log

def serve():
    '''Serve as if this was your last day on earth'''
    # setup base
    log = setup_log()
    config = load_config()

    # setup server
    listen_string = ':'.join([
        config['host'],
        config['port'],
    ])
    log.info("Starting thread pool ...")
    with futures.ThreadPoolExecutor(max_workers=10) as executor:
        server = grpc.server(executor)
        grpctest_pb2_grpc.add_GreeterServicer_to_server(greeter.Service(), server)
        server.add_insecure_port(listen_string)
        log.info("Starting server on: {}".format(listen_string))
        server.start()
        try:
            while True:
                time.sleep(10)
        except KeyboardInterrupt:
            server.stop(0)

if __name__ == "__main__":
    serve()

