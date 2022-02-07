class Manager(object):
    def __enter__(self):
        print("Entering")
        return 'Some value'
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        print('Exiting')
        print(exc_type, exc_value, exc_traceback)