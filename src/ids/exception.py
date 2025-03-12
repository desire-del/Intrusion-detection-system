from ids import logger
import sys

class CustomException(Exception):
    def __init__(self, message, error_detail:sys):
        self.message = message
        self.error_detail = error_detail
        super().__init__(self.message)
        logger.error(error_message(self.message,self.error_detail))
        

    def __self__(self):
        return self.message


def error_message(error, error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename

    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
         file_name,exc_tb.tb_lineno,str(error))
    return error_message


