import os
from datetime import datetime
import logging

LOG_FILENAME = datetime.now().strftime('C:\\Users\\Sanket.Paraskar\\Desktop\\Logs\\logs_%H_%M_%S_%d_%m_%Y.log')
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
logger = logging.getLogger()

logger.addHandler(logging.FileHandler(LOG_FILENAME, 'w'))

env = 'test'
from subprocess import check_output
os.chdir(os.path.abspath(os.path.expanduser('C:\\LeadGenerator')))


def cleardb():
    cleandb = check_output(["node", "ClearDb", env , "consumer", "Sanket"], shell=True).decode()
    #logging.info("node ClearDb " + env + " consumer Sanket")
    #logging.info(cleandb)

    if 'consumer not found' in cleandb:
        logging.info("Consumer is already cleared")
        logging.info("\n")
    else:
        logging.info("Consumer is cleared successfully")
        logging.info("\n")


def weblead():
    command = check_output(["ts-node", "src/leadGen.ts", "-e", env , "-b", "Zillow", "-c", "Sanket", "-r", "Sanket", "-l", "web", "-z", "98103"], shell=True).decode()
    logging.info("Trying web lead now")
    logging.info("ts-node src/leadGen.ts -e " + env + " -b Zillow -c Sanket -r Sanket -l web -z 98103")
    logging.info(command)

    if 'CaseId' in command:
        logging.info("Web lead is created successfully")
        logging.info("\n")
    else:
        logging.info("Some error occurred")
        logging.info("\n")


def tourlead():
    command1 = check_output(["ts-node", "src/leadGen.ts", "-e", env , "-b", "Zillow", "-c", "Sanket", "-r", "Sanket", "-l", "vht", "-z", "98103"], shell=True).decode()
    logging.info("Trying tour lead now")
    logging.info("ts-node src/leadGen.ts -e " + env + " -b Zillow -c Sanket -r Sanket -l vht -z 98103")
    logging.info(command1)

    if 'CaseId' in command1:
        logging.info("VirtualTour lead is created successfully")
        logging.info("\n")
    else:
        logging.info("Some error occurred")
        logging.info("\n")


def phonelead():
    command2 = check_output(["ts-node", "src/leadGen.ts", "-e", env , "-b", "Zillow", "-c", "Sanket", "-r", "Sanket", "-l", "phone", "-z", "98103"], shell=True).decode()
    logging.info("Trying phone lead now")
    logging.info("ts-node src/leadGen.ts -e " + env + " -b Zillow -c Sanket -r Sanket -l phone -z 98103")
    logging.info(command2)

    if 'CaseId' in command2:
        logging.info("Phone lead is created successfully")
        logging.info("\n")
    else:
        logging.info("Some error occurred")
        logging.info("\n")


def zhllead():
    command3 = check_output(["ts-node", "src/leadGen.ts", "-e", env , "-b", "Zillow", "-c", "Sanket", "-r", "Sanket", "-l", "web", "-v", "zhl", "-z", "98103"], shell=True).decode()
    logging.info("Trying zhl lead now")
    logging.info("ts-node src/leadGen.ts -e " + env + " -b Zillow -c Sanket -r Sanket -l web -v zhl -z 98103")
    logging.info(command3)

    if 'CaseId' in command3:
        logging.info("ZHL lead is created successfully")
        logging.info("\n")
    else:
        logging.info("Some error occurred")
        logging.info("\n")


def flexlead():
    command4 = check_output(["ts-node", "src/leadGen.ts", "-e", env , "-b", "Zillow", "-c", "Sanket", "-r", "Sanket", "-l", "web", "-v", "flex", "-m", "ATL"], shell=True).decode()
    logging.info("Trying flex lead now")
    logging.info("ts-node src/leadGen.ts -e " + env + " -b Zillow -c Sanket -r Sanket -l web -v flex -m ATL")
    logging.info(command4)

    if 'CaseId' in command4:
        logging.info("Flex lead is created successfully")
        logging.info("\n")
    else:
        logging.info("Some error occurred")
        logging.info("\n")


cleardb()
weblead()
cleardb()
tourlead()
cleardb()
phonelead()
cleardb()
zhllead()
cleardb()
flexlead()
cleardb()

logging.info("All leads checked successfully")