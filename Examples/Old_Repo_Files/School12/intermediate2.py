#logging 
import logging
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s" ,
                    datefmt='%d/%m/%y %H: %M: %S')

logging.debug("This a logging message for debug from root")
logging.info("This a logging message for info from root")
logging.warning("This a logging message for warning from root")
logging.error("This a logging message for error from root")
logging.critical("This a logging message for critical from root")

# ---------------------   keep this on other file to get your logs from that file --------------------------------
import logging
Logger = logging.getLogger(__name__)
# logger.propagate = False # will not send logging info to the base file
logging.info("hello This is message from practising skiils")


#logging handlers / stream handlers / timedhandlers ---- watched----not noted
# JSON with python
import json

person = {"name" : "harsh", "age" : 19, "city" : "Chennai", "State":"Tamil Nadu", "Has_childrens":False, "intrest" : ["programming", "enegeneering"]}
personJSON = json.dumps(person, indent=4)#, sort_keys=True)
person_copy = json.load(personJSON)
print(person)
print(personJSON)
print("----", person_copy)

class User:    #defining custom class

    def __init__(self, name, age):
        self.name = name
        self.age = age

in1 = input("name : ") 
in2 = int(input("age  : "))    
user = User(in1, in2)

def encode_user(o):
    if isinstance(o, User):
        return{'name': o.name, 'age' : o.age, o.__class__.__name__:True}
    else:
        raise TypeError('object of user type is not serialisable')

userJSON = json.dumps(user, default=encode_user)
print(userJSON)

