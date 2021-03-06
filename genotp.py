"""Generate OTP Command Line Tools

Usage:
  genotp INSTANCE USERNAME [SECRET]
  genotp INSTANCE USERNAME [-t TIME]

Options:
  -h --help     Show this screen.
  --version     Show version.
  INSTANCE      Instance eg. klrx010, bewx1551)
  USERNAME      Username
  SECRET        Secret key
  TIME          Generate TOTP at specific time, (Format: "YYYY-MM-DD-HH:MM:SS"). If not specified, local time is used

"""
from docopt import docopt

import pyotp
import datetime
import hashlib
import configparser
import os


def config_file_init(filename):
    config = configparser.ConfigParser()

    # w+ to create file if not exist
    f = open(filename, 'w+')
    config.add_section('Setting')
    config.set('Setting', 'digits', '8')
    config.set('Setting', 'interval', '30')
    config.write(f)
    f.close()


def main(args):
    config = configparser.ConfigParser()

    inst = args['INSTANCE']
    username = args['USERNAME']
    secret = args['SECRET']
    time = args['TIME']

    # Create instance config file if not exist
    if not os.path.isfile(inst):
        config_file_init(inst)
        print(inst, 'config file created')

    config.read(inst)

    # Check whether Setting Section Exist
    if not config.has_section('Setting'):
        config_file_init(inst)
        config.read(inst)

    # r+ to read and write the file without truncating
    f = open(inst, 'r+')

    if secret:
        secret = secret.replace(' ', '')
        # contain secret
        if not config.has_section(username):
            # Create user if not exist
            config.add_section(username)
            config.set(username, 'secret', secret)
        else:
            # Replace previous secret
            config.set(username, 'secret', secret)
        config.write(f)
    else:
        # get secret
        try:
            secret = config[username]['secret']
        except:
            error = username + " does not exist"
            raise ValueError(error)

        if secret is None:
            raise ValueError('Empty Secret Key')

    interval = int(config['Setting']['interval'])
    digits = int(config['Setting']['digits'])

    totp = pyotp.TOTP(secret, digits=digits, digest=hashlib.sha256, interval=interval)

    f.close()

    print("Instance:", inst)
    print("User:", username)
    # Check if -t specified:
    if time:
        date_object = datetime.datetime.strptime(time, '%Y-%m-%d-%H:%M:%S')
        print("Time:", date_object)
        print("TOTP:", totp.at(date_object))
    else:
        print("Current Time:", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        print("TOTP:", totp.now())

if __name__ == '__main__':
    arguments = docopt(__doc__, version='genotp 1.0')
    # print(arguments)

    main(arguments)
