class Cypher:
    '''This is the class that will define cypher and its uses and what it contains '''
    def __init__(self):
        '''Creates the class
        Args:
        self : This is used to refer to itself to establish data types'''
        self._alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    def encrypt_message(self, message):
        '''Allows us to encrypt messages that are sent to be encrypted
        Args:
        self: This is how we use elements from this class
        message(string): This is the message that the user gives
        Returns:
        "".join(newmessage): This is the encrypted message to be sent to main'''
        upmessage = list(message.upper())
        newmessage = ""
        newletter = ""
        for i in upmessage:
            if i in self._alphabet:
                newletter += self._encrypt_letter(i)
        newmessage += newletter
        return "".join(newmessage)
    def decrypt_message(self, message):
        '''Allows us to decrypt messages that are sent to be decrypted
        Args:
        self: This is how we use elements from this class
        message(string): This is the message that the user gives
        Returns:
        "".join(newmessage): This is the decrypted message to be sent to main'''
        upmessage = list(message.upper())
        newmessage = ""
        newletter = ""
        for i in upmessage:
            if i in self._alphabet:
                newletter += self._decrypt_letter(i)
        newmessage += newletter
        return "".join(newmessage)
    def _encrypt_letter(self, letter):
        '''Allows us to encrypt a letter that is sent to be encrypt
        Args:
        self: This is how we use elements from this class
        letter (string): A single letter that needs to be encrypted
        Returns:
        newletter(string): This is the encryped letter that is returned'''
        location = 0
        for i in range (0,26,1):
            if letter == self._alphabet[i]:
                location = i
        newletter = self._alphabet[25-location]
        return newletter
    def _decrypt_letter(self, letter):
        '''Allows us to decrypt a letter that is sent to be decrypt
        Args:
        self: This is how we use elements from this class
        letter (string): A single letter that needs to be decrypted
        Returns:
        newletter(string): This is the decryped letter that is returned'''
        location = 0
        for i in range (0,26,1):
            if letter == self._alphabet[i]:
                location = 25 - i
        newletter = self._alphabet[location]
        return newletter
