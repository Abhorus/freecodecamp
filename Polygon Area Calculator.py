class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, w):
        self.width = w

    def set_height(self, h):
        self.height = h

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        pic = []
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            for i in range(self.height):
                pic.append('*' * self.width)
                pic.append('\n')
            return ''.join(pic)

    def get_amount_inside(self, shape):
        self.shape = shape
        return int(self.get_area() / shape.get_area())


    def __str__(self):
        return str(self.__class__.__name__) + '(width=' + str(self.width) + ', ' + 'height=' + str(self.height) + ')'
    #object.__class__.__name__ will get the objects name


class Square(Rectangle):
    def __init__(self, side):
        Rectangle.__init__(self, width= side, height= side) #stores side value in width & height attributes
        self.side = side

    def set_side(self,side):
        self.width = side
        self.height = side
        self.side = side

    def set_width(self, w):
        self.width = w
        self.height = w
        self.side = w

    def set_height(self, h):
        self.height = h
        self.width = h
        self.side = h

    def __str__(self):
        return str(self.__class__.__name__) + '(side=' + str(self.side) + ')'










#---------tests---------

rect = Rectangle(4,8)
sq = Square(4)
#rect.set_width(4)
#print(rect.get_area())
#print(rect.get_perimeter())
#print(rect.get_diagonal())
#print(rect.get_picture())
#print(rect.get_amount_inside(sq))
#print(rect)
#sq.set_width(2)
#sq.set_height(3)
#sq.set_height(3)
#sq.set_side(2)
print(sq)
print(sq.get_picture())
