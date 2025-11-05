import sys

class CustomException(Exception):
    def __init__(self,message,error_detail:Exception = None):
       self.error_message = self.get_detailed_error_message(message,error_detail=error_detail)
       super().__init__(self.error_message)

    def get_detailed_error_message(self,message,error_detail:Exception = None):
        _,_,exc_tb = sys.exc_info()
        line_number = exc_tb.tb_lineno if exc_tb else 'N/A'
        file_name = exc_tb.tb_frame.f_code.co_filename if exc_tb else 'N/A'
        error_message = f"Error occurred in script: {file_name} at line number: {line_number} with message: {message}"
        return error_message
    
    def __str__(self):
        return self.error_message
