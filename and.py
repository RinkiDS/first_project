import logging
import os

logging_str = "[%(asctime)s: %(levelname)s: %(module)s] %(message)s"
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)
logging.basicConfig(filename= os.path.join(log_dir,"running_logs.log"),level=logging.INFO, format=logging_str, filemode="a")

def callme(name,age):
    """use to log name and age 

    Args:
        name (string):name of the caller
        age (integer): age of the caller

     Raises:
        e: calculation errors

    Returns:
       integer: inetger
    """
    logging.info(f"Hello, My name is {name} and I'm {age} years old.")
    age_cal=0
    try:
         age_cal =age/10
         logging.info(f"My calculated age is {age_cal}")    
    except Exception as e:
        logging.warning(f"comes in exception {e}")
        raise e
    return age_cal  
   

if __name__=="__main__":
  name="Rinki"
  age=11
  callme(name,name)
