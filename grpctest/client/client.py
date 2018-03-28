#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging as log
import os
import sys
import yaml
import argparse
import grpc
import grpctest_pb2
import grpctest_pb2_grpc

loc = os.path.dirname(__file__)
CONFFILE = os.getenv('GRPCTEST_CLIENT_CONFFILE', loc + '/config.yml')
DEBUG = os.getenv('GRPCTEST_CLIENT_DEBUG', None)

def greeter_say_hello(stub):
    req = grpctest_pb2.HelloRequest(name="super")
    res = stub.SayHello(req)
    log.info("client req: {}".format(req))
    log.info("client res: {}".format(res))

def parse_args():
    '''Parse cli'''
    parser = argparse.ArgumentParser(description = 'Client')

#    parser.add_argument(
#      '--action',
#      type=str,
#      metavar='Action',
#      choices=ACTIONS.keys(),
#      default='update',
#      required=True,
#      help='Action to perform, default is "update"')
#
#    parser.add_argument(
#      '--query',
#      type=str,
#      metavar='Query',
#      default='all',
#      help='The Query to perform, default is "all"')
#
#    parser.add_argument(
#      '--platform',
#      type=str,
#      metavar='Platform',
#      default='crpcc',
#      help='The Platform on which to operate, default is "crpcc"')
#
#    parser.add_argument(
#      '--startdate',
#      type=lambda d: datetime.strptime(d, "%d.%m.%Y %H:%M:%S"),
#      metavar='Startdate',
#      default=DEFAULT_STARTDATE,
#      help="""The Startdate where we start to sample: d.m.Y H:M:S""")
#
#    parser.add_argument(
#      '--enddate',
#      type=lambda d: datetime.strptime(d, "%d.%m.%Y %H:%M:%S"),
#      metavar='Enddate',
#      default=DEFAULT_ENDDATE,
#      help="""The Enddate where we start to sample: d.m.Y H:M:S""")
#
#    parser.add_argument(
#      '--step',
#      type=str,
#      metavar='Step',
#      default=DEFAULT_STEP,
#      help="""The Stepping """)

    args = parser.parse_args()
    return args

def load_config(args):
    '''Load Yaml config based on the env'''
    try:
        with open(CONFFILE, 'r') as ymlfile:
            config = yaml.load(ymlfile)['client']
            config.update({'args': vars(args)})
            log.info('Successfully loaded config file: {}'.format(CONFFILE))
    except Exception as error:
        log.error('Error loading config file: {} \n with Error: {}'.format(CONFFILE, error))
        sys.exit(1)
    return config

def setup_log():
    '''setup logging'''
    log_level = log.DEBUG if DEBUG else log.INFO
    log_format = '%(asctime)s %(levelname)-8s %(message)s'
    log_datefmt = '%a, %d %b %Y %H:%M:%S'
    log.basicConfig(level=log_level, format=log_format, datefmt=log_datefmt)
    return log

def run():
    '''Run like you never run before'''
    # setup base
    log = setup_log()
    args = parse_args()
    config = load_config(args)

    # setup client
    conn_string = ':'.join([
        config['server']['host'],
        config['server']['port'],
    ])
    channel = grpc.insecure_channel(conn_string)
    stub = grpctest_pb2_grpc.GreeterStub(channel)

    log.info("-------------- GetFeature --------------")
    greeter_say_hello(stub)

if __name__ == "__main__":
    run()
