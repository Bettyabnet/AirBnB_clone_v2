class DBStorage:


    def close(self):
        self.__session.remove()
