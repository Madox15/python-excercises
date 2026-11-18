import math


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        return math.sqrt(self.width**2 + self.height**2)

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        picture = ""
        for i in range(self.height):
            picture += "*" * self.width + "\n"
        return picture

    def get_amount_inside(self, shape):
        if isinstance(shape, Rectangle):
            vertical_fits = self.height // shape.height
            horizontal_fits = self.width // shape.width
            return vertical_fits * horizontal_fits

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def set_width(self, width):
        self.width = width
        self.height = width

    def set_height(self, height):
        self.width = height
        self.height = height

    def set_side(self, side):
        self.width = side
        self.height = side

    def __str__(self):
        return f"Square(side={self.width})"


"""set_width: Overrides the set_width method from the Rectangle class. It should set the width and height to the side length.
set_height: Overrides the set_height method from the Rectangle class. It should set the width and height to the side length.
set_side: Sets the height and width of the square equal to the side length.
The Square class should be able to access the Rectangle class methods.

If an instance of a Square is represented as a string, it should look like: Square(side=9)."""
