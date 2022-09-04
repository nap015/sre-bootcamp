# These functions need to be implemented
import hashlib

class Token:
    
    #import mysql.connect

    def generate_token(self, username, password):
        string = 'F^S%QljSfV'+password
        r = hashlib.sha512(string.encode()).hexdigest()
        return r
        
#         cnx = mysql.connector.connect(user='secret', password='noPow3r',
#                               host='127.0.0.1',
#                               database='employees')
#         cnx.close()
        #return 'test'


class Restricted:

    def access_data(self, authorization):
        return 'test'
