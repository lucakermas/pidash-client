#!/usr/bin/env python3

import argparse
from urllib.parse import urlparse
import requests
from gpiozero import CPUTemperature

from pprint import pprint

arg_parser = argparse.ArgumentParser(description='Send CPU temperature to pidash.')
arg_parser.add_argument('url', metavar='U', help='The url of your pidash site.')
arg_parser.add_argument('pi', metavar='P', help='The name of the PI.')

if __name__ == '__main__':
    args = arg_parser.parse_args()
    url = args.url
    pi = args.pi

    parsed_url = urlparse(url)

    if not parsed_url.scheme or not parsed_url.netloc:
        print(url + ' is not a valid url.')
        pass

    cpu = CPUTemperature()

    d = {
            'temperature': cpu.temperature
        }

    url = url + pi

    try:
        print('Sending data to ' + url + '...')
        request = requests.post(url, data=d)
        response = request.json()

        print('Data send. Response:')
        print(response.get('message'))
    except:
        print('There was an error sending the temperature.')

