#Launchcode - Studio - Design Problems - Rectangle

#RECTANGLE¶
#A rectangle has a length and a width. A rectangle should be able to provide its area and perimeter. DONE
#A rectangle can indicate whether it is smaller than another rectangle in terms of area. 
#A rectangle can indicate whether it is in fact a square.

#create Rectangle Class
class Rectangle():
    def __init__(self, l, w):
        self.length = l
        self.width = w
    
    #method to provide area
    def rectangle_area(self):
        return self.length*self.width
    
    #method to provide perimeter
    def rectangle_perimeter(self):
        return 2*(self.length+self.width)

    #method to determine if rectanglea is smaller than rectangleb one rectangle to another
    def rectangle_compare(self)
        if rectangle_area1 > rectangle_area2
            return True



def main():
    rectangle1 = Rectangle(5, 10)
    rectangle2 = Rectangle(10,20)

    print(rectangle1)
    print(rectangle2)
    