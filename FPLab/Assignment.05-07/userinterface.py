import datetime


class UserInterface:
    def __init__(self, utils, ctrl):
        self.utils = utils
        self.ctrl = ctrl

        self.menuOptions = {
            0 : "0. Exit",
            1 : "1. Add clients or movies",
            2 : "2. Remove clients or movies",
            3 : "3. Update clients or movies",
            4 : "4. List clients or movies",
            5 : "5. Rent a movie",
            6 : "6. Return a movie",
            7 : "7. Search for clients or movies",
            8 : "8. Statistics",
            9 : "9. Print rental list [DEBUG]"
        }


    def clientsOrMovies(self):
        '''
        :return: 1 or 2, depending on the input
        '''

        print("1. Client")
        print("2. Movie")

        option = self.utils.readInteger(">> ")
        return option


    def showMenu(self):
        '''
        :return: None

        Prints the menu options
        '''

        for val in self.menuOptions.values():
            print(val)


    def addClient(self):
        '''
        :return: None

        Reads the new client's name, then adds it to the client list
        '''

        name = self.utils.readString("Input name: ")
        self.ctrl.addClient(name)


    def addMovie(self):
        title = self.utils.readString("Input title: ")
        description = self.utils.readString("Input description: ")
        genre = self.utils.readString("Input genre: ")
        self.ctrl.addMovie(title, description, genre)


    def removeClient(self):
        name = self.utils.readString("Input name: ")

        if not self.ctrl.removeClient(name):
            print("Command was not executed.")


    def removeMovie(self):
        title = self.utils.readString("Input title: ")

        if not self.ctrl.removeMovie(title):
            print("Command was not executed.")


    def listClients(self):
        clients = self.ctrl.getClients()
        for client in clients:
            print("[" + str(client.getId()) + " - " + client.getName() + "]")


    def listMovies(self):
        movies = self.ctrl.getMovies()
        for movie in movies:
            print("[" + str(movie.getId()) + " - " + movie.getTitle() + " - " + movie.getDescription() + " - " + movie.getGenre() + "]")


    def rentMovie(self):
        name = self.utils.readString("Who are you? (input name): ")
        result = self.ctrl.searchClientMatch(name)
        if len(result) > 0:
            print("Assuming you are " + result[0] + ". If you are not, please input \"0\" and reenter your correct name! If this is you, enter any other number then press enter to continue")
            tmp = self.utils.readInteger(">> ")
            if tmp == 0:
                return
        else:
            print("Couldn't find your name! Returning.")
            return

        clientId = self.ctrl.getClientIdByName(result[0])

        movies = self.ctrl.getMovies()
        movieAvailable = False
        for movie in movies:
            if not movie.isRented():
                movieAvailable = True
                break

        if not movieAvailable:
            print("There are no available movies to rent!")
            return

        print("Movies available for renting: ")

        # we need this to make sure the user does not enter
        # some invalid movie id
        movieIds = []

        for movie in movies:
            if not movie.isRented():
                movieIds.append(movie.getId())
                print("[" + str(movie.getId()) + " - " + movie.getTitle() + " - " + movie.getDescription() + " - " + movie.getGenre() + "]")

        option = self.utils.readInteger("Which movie would you like to rent? ")

        if option not in movieIds:
            print("Invalid movie id chosen!")
            return

        if movies[option - 1].isRented():
            print("The movie you are trying to rent is already rented!")
        else:
            self.ctrl.addRental(movies[option - 1].getId(), clientId, datetime.datetime.now())


    def updateClient(self):
        oldName = self.utils.readString("Input the name you want to replace: ")
        newName = self.utils.readString("Input new name: ")

        if not self.ctrl.updateName(oldName, newName):
            print("Command was not executed.")

    def updateMovie(self):
        oldTitle = self.utils.readString("Input the title you want to replace: ")
        newTitle = self.utils.readString("Input new title: ")
        newDescription = self.utils.readString("Input new description: ")
        newGenre = self.utils.readString("Input new genre: ")

        if not self.ctrl.updateMovie(oldTitle, newTitle, newDescription, newGenre):
            print("Command was not executed.")


    def searchClient(self):
        name = self.utils.readString("Input name: ")

        result = self.ctrl.searchClientMatch(name)
        if len(result) > 0:
            print(result)
        else:
            print("No matching result found.")


    def searchMovie(self):
        title = self.utils.readString("Input title: ")

        result = self.ctrl.searchMovieMatch(title)
        if len(result) > 0:
            print(result)
        else:
            print("No matching result found")


    def printRentalList(self):
        rlist = self.ctrl.getRentedMovies()
        for rental in rlist:
            print(str(rental.getRentalId()) + " - " + str(rental.getMovieId()) + " - " + str(rental.getClientId()) + " - "  + str(rental.getRentedDate()) + " - " + str(rental.getDueDate()))


    def run(self):
        while True:
            self.showMenu()
            option = self.utils.readInteger(">> ")

            '''
            if option in self.menuOptions.keys():
                list(self.menuOptions.values())[option][1]()
            else:
                print("Unknown option!")
            '''

            if option == 0:
                exit()

            elif option == 1:
                clientOrMovie = self.clientsOrMovies()

                if clientOrMovie == 1:
                    self.addClient()
                elif clientOrMovie == 2:
                    self.addMovie()
                else:
                    print("Invalid input!")

            elif option == 2:
                clientOrMovie = self.clientsOrMovies()

                if clientOrMovie == 1:
                    self.removeClient()
                elif clientOrMovie == 2:
                    self.removeMovie()
                else:
                    print("Invalid input!")

            elif option == 3:
                clientOrMovie = self.clientsOrMovies()

                if clientOrMovie == 1:
                    self.updateClient()
                elif clientOrMovie == 2:
                    self.updateMovie()
                else:
                    print("Invalid input")

            elif option == 4:
                clientOrMovie = self.clientsOrMovies()

                if clientOrMovie == 1:
                    self.listClients()
                elif clientOrMovie == 2:
                    self.listMovies()

            elif option == 5:
                self.rentMovie()

            elif option == 6:
                pass
            elif option == 7:
                clientOrMovie = self.clientsOrMovies()

                if clientOrMovie == 1:
                    self.searchClient()
                elif clientOrMovie == 2:
                    self.searchMovie()
                else:
                    print("Invalid input")

            elif option == 8:
                pass
            elif option == 9:
                self.printRentalList()
            else:
                print("Unknown option!")