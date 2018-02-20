#try1
class RectangleArea(object):
    
        def __init__(self, width, length):
                self.__width = width
                self.__length = length
                self.__area = width*length

        def get_area(self):
                return self.__area

def main():
        width = int(input("Enter the width of a rectangle: "))
        length = int(input("Enter the lengh of a rectangle: "))
        #creation of Object
        area = RectangleArea (width, length)
        
        #display of the values stored in the fields
        print("A rectangle with a width of ",width,"and a legth of ",length,"is",area.get_area())
        
main()
