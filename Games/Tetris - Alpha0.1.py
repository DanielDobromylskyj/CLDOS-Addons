import random
class Board():
    def __init__(self):
        self.objects = []
        self.totalIDS = 0

    def SummonShape(self, ShapeData):
        print(type(ShapeData), ShapeData)
        Shape, Character = ShapeData
        self.objects.append([True, Shape, Character, [5 ,1], self.totalIDS]) # The First Value Is A Check For Is It Falling? Or Is It Static
        self.totalIDS += 1

    def UpdatePhysics(self):
        self.fallby = 1
        moving_object = self.objects[len(self.objects) - 1]
        next_move_object = self.objects[len(self.objects) - 1]
        if moving_object[0] != True:
            piece = random.choice(["I", "J", "T", "S", "Z", "L", "O"])
            c = globals()['Piece']()
            self.SummonShape(getattr(c, piece)())


        def NextMove(next_move_object):
            global Key
            if Key == "d": # Move Right Or Right
                Key = ""
                next_move_object[3][0] = moving_object[3][0] + 1 # dont Work
            elif Key == "a":
                Key = ""
                next_move_object[3][0] = moving_object[3][0] - 1

            elif Key == "e": # Rotate
                Key = ""
                print("e")
            elif Key == "q":
                Key = ""
                print("q")

            return next_move_object

        # if its Moving Run This Loop And Apply Physics
        if moving_object[0] == True:
            next_move_object = NextMove(next_move_object)
            next_move_object[3][1] = next_move_object[3][1] + self.fallby

            # Check For Collisions: If True >>> Means Collision. Else: Nothing
            if self.CheckCol(next_move_object):
                moving_object[0] = False


            #if self.objects[len(self.objects) - 1][0] == True:
            #    self.objects.pop(len(self.objects) - 1)
            #     self.objects.append(moving_object)
        else:
            pass


        time.sleep(0.5)






    def CheckKey(self):
        import tkinter as tk

        def key(event):
            global Key
            Key = event.char

        root = tk.Tk()
        root.bind_all('<Key>', key)
        root.withdraw()
        root.mainloop()

    def CheckCol(self, shape):
        shp_State, shp_Shape, shp_char, shp_location, shp_id = shape
        for object in self.objects: # Check For Object Hitting The Other Objects
            _, obj_Shape, obj_char, obj_location, obj_id = object
            if shp_id != obj_id:
                for obj_part in obj_Shape:
                    for shp_part in shp_Shape:
                        if obj_part[0] + obj_location[0] == shp_part[0] + shp_location[0] + 1:
                            if obj_part[1] + obj_location[1] == shp_part[1] + shp_location[1] + 1:
                                print("Hit Part")
                                return True # True = colition

        if shp_location[1] >= 14:
            return True # True = colition





    def Display(self):
        print("")
        PrintList = [[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]]
        for object in self.objects:
            for block in object[1]:
                try:
                    PrintList[object[3][1] + block[1]][object[3][0] + block[0]] = object[2]
                except IndexError:
                    pass

        for line in PrintList:
            print(line)







class Piece():
    def I(self):
        shape = [(0,0), (0, 1), (0, 2), (0, 3)] # 0,0 = Bottom left
        return (shape, "I")

    def T(self):
        shape = [(0, 0), (1, 0), (2, 0), (1, 1)] # 0,0 = Bottom left
        return (shape, "T")

    def J(self):
        shape = [(0, 0), (1, 0), (2, 0), (0, 1)]  # 0,0 = Bottom left
        return (shape, "J")

    def L(self):
        shape = [(0, 0), (1, 0), (2, 0), (2, 1)]  # 0,0 = Bottom left
        return (shape, "L")

    def Z(self):
        shape = [(0, 1), (1, 0), (1, 1), (2, 0)]  # 0,0 = Bottom left
        return (shape, "Z")

    def O(self):
        shape = [(0, 0), (1, 0), (1, 1), (0, 1)]  # 0,0 = Bottom left
        return (shape, "O")

    def S(self):
        shape = [(0, 0), (1, 0), (1, 1), (2, 1)]  # 0,0 = Bottom left
        return (shape, "O")

import time
import threading

p = Piece()
b = Board()
global Key
Key = ""
t = threading.Thread(target=b.CheckKey)
t.start()

b.SummonShape(p.O())

while True:
    b.UpdatePhysics()
    b.Display()