import json
import os
import sys
import argparse
import logging
from pathlib import Path
from news_reader import tasks
from news_reader.utils import get_app_location
from news_reader.utils.initial_configurations import app_default_config
from werkzeug.security import check_password_hash, generate_password_hash

app_loc = get_app_location()

# initiate logger
logger = logging.getLogger()
formatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s] %(message)s")
stdoutHandler = logging.StreamHandler(sys.stdout)
stdoutHandler.setLevel(logging.DEBUG)
stdoutHandler.setFormatter(formatter)
logger.addHandler(stdoutHandler)

config_loc = Path(os.path.join(app_loc, 'conf', 'news-config.json'))
if not os.path.exists(config_loc.absolute()):
    try:
        os.makedirs(config_loc.parent.absolute())
    except OSError as e:
        logger.info(f'Making directories failed. Check if the user has permissions to make directories at : {config_loc.parent.absolute()}')
    with open(config_loc.absolute(), 'w') as config_file:
        json.dump(app_default_config, config_file, indent=4)
    logger.info(f"Log file created at {config_loc.absolute()}")

with open(config_loc.absolute(), 'r') as config_file:
    common_config = json.load(config_file)

# creating parser object
class ArgsParser(argparse.ArgumentParser):
    def error(self, message):# Modified to show help text on error
        sys.stderr.write('\033[0;31merror: %s\n\n\033[0m' % message)
        self.print_help()
        sys.exit(2)

def run():
    parser = ArgsParser()
    subparser = parser.add_subparsers(title="commands", dest="command")

    help_texts = {
        'meta' : 'Metadata DB URL',
        'source_db' : 'Source DB URL',
        'dest_db' : 'Destination DB URL',
        'db_module' : 'Schema/Owner for the tables if any.',
        'db_tables' : 'Tables for which the solution needs to be prepared'
    }

    # Subparsers for action
    fetch_subparser = subparser.add_parser("fetch", help="Fetch the News as configured.")
    fetch_subparser.add_argument('--meta',       required = False,    nargs=1, help=help_texts['meta'], default=common_config['META_DB_URI']) # dialect://username:password@host:port/extensions
    fetch_subparser.add_argument('-s', '--source',       required = True,    nargs=1, help=help_texts['source_db']) # dialect://username:password@host:port/extensions
    fetch_subparser.add_argument('-d', '--destination',  required = True,    nargs=1, help=help_texts['dest_db']) # dialect+driver://username:password@host:port/?service_name=service
    fetch_subparser.add_argument('-m', '--module',       required = True,    nargs=1, help=help_texts['db_module'], default="public")
    fetch_subparser.add_argument('--tables',             required = False,   nargs=1, help=help_texts['db_tables'])

    args = parser.parse_args()
    
    if args.command == 'fetch':
        tasks.source()
    
    # parser.print_help()