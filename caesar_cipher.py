import cypher
class CasesarCipher(cypher.Cypher):
    '''This is the derived class of cypher that has a redefinition of certain methods'''
    def __init__(self, shift):
        '''Creates the class
        Args:
        self : This is used to refer to itself to establish data types
        shift (int): This is the value used to shift the alphabet array to encrypt based
        on what the user wanted'''
        super().__init__()
        if type(shift) == int:
            self._shift = shift
        else:
            raise TypeError("Not a number") 
    def _encrypt_letter(self, letter):
        '''Allows us to encrypt a letter that is sent to be encrypt
        Args:
        self: This is how we use elements from this class
        letter (string): A single letter that needs to be encrypted
        Returns:
        self._alphabet[location+self._shift](string): This is the encryped letter that is
        returned based on the shift given by user'''
        location = 0
        for i in range (0,26,1):
            if letter == self._alphabet[i]:
                location = i
        if location + self._shift > 25:
            location -= 26
        return self._alphabet[location+self._shift]
    def _decrypt_letter(self, letter):
        '''Allows us to decrypt a letter that is sent to be decrypt
        Args:
        self: This is how we use elements from this class
        letter (string): A single letter that needs to be decrypted
        Returns:
        self._alphabet[location-self._shift](string): This is the decryped letter that is
        returned based on shift value given by user'''
        location = 0
        for i in range (0,26,1):
            if letter == self._alphabet[i]:
                location = i
        if location - self._shift < 0:
            location += 26
        return self._alphabet[location-self._shift]
