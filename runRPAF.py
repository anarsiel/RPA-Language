import sys
import logging

from body.Interpreter import Interpreter

interpreter = Interpreter()
try:
    interpreter.parse_file(sys.argv[1])
    # interpreter.parse_file("main.rpaf")
except (Interpreter.CompilationError, Interpreter.RunTimeError) as exception:
    logging.error(str(exception))
except Interpreter.RunTimeWarning as exception:
    logging.warning(str(exception))
except IndexError:
    logging.error("Program file name is obligatory!")