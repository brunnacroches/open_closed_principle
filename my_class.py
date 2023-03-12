
class Circus:

    def present(self, presenter: any):
        presenter.presenter_show()


class Juggler:
    def presenter_show(self):
        print('Juggler presenter his show')
    

class Clown:
    def presenter_show(self):
        print('Clown presenter his show')

class Tamer:
    def presenter_show(self):
        print('Tamer presenter his show')

circus = Circus()
juggler = Juggler()
clown = Clown()
tamer = Tamer()

circus.present(juggler)
circus.present(clown)
circus.present(tamer)


    # apresentar, o apresentador. apresentação
    # present, presenter. presentation





# class Circus:
    
#     def performance(self, type):
#         if type == 1:
#             self.introduce_juggler() # aprensetação do palhaço
#         if type == 2:
#             self.introduce_clown() # aprensetação do palhaço
    
#     def introduce_juggler(self):
#         print('Juggler performing his show')
    
#     def introduce_clown(self):
#         print('Clown performing his show')

# circus = Circus(1)