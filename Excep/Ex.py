class MyException(Exception):
    def __init__(self, msg):
        # Call the base class constructor with the parameters it needs
        super(Exception, self).__init__(msg)
