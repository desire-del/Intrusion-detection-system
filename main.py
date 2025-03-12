from ids import logger
from ids.exception import CustomException
import sys

try:
    print(1/0)
except Exception as e:
    print("Exception occured")