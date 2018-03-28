#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging as log
import grpc
import grpctest_pb2
import grpctest_pb2_grpc


class Service(grpctest_pb2_grpc.GreeterServicer):

    def SayHello(self, request, context):
        log.info("server context: {}".format(context))
        log.info("server request: {}".format(request))
        response = grpctest_pb2.HelloResponse(message="yeah got it.")
        log.info("server response: {}".format(response))
        return response

