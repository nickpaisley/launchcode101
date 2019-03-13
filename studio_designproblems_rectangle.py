#Launchcode - Studio - Design Problems - Rectangle

#RECTANGLE¶
#A rectangle has a length and a width. A rectangle should be able to provide its area and perimeter. DONE
#A rectangle can indicate whether it is smaller than another rectangle in terms of area. DONE but without a function only a comparison call.
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

    #method to determine if rectangle1 is smaller than rectangle2
    def __le__(self, other):
        return ((self.length, self.width) <= (other.length, other.width))
                
    #method to compare sides of rectangle to determine isbox
    def rectangle_isbox(self):
        return self.length == self.width



def main():
    #create 2 diff size rectangles
    rectangle1 = Rectangle(1, 10)
    rectangle2 = Rectangle(10,20)
    rectangle3 = Rectangle(10,10)
    
    #print the 2 rectangle's area
    print("R1 Area : ", rectangle1.rectangle_area())
    print("R2 Area : ", rectangle2.rectangle_area())
    
    #print the 2 rectangle's perimeter
    print("R1 Perimeter : ", rectangle1.rectangle_perimeter())
    print("R2 Perimeter : ", rectangle2.rectangle_perimeter())

    #see if R1 is smaller than R2
    print("R1 is smaller than R2", rectangle1 <= rectangle2)
    print("Function, R1 is smaller than R2", rectangle1.__le__(rectangle2))

    #check to see if R1 is a box
    print ("R3 is a Box : ", rectangle3.rectangle_isbox())
    
if __name__ == "__main__":
    main()
