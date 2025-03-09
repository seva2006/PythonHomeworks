import math

class Vector:
    def __init__(self, *args):
        self.args = args

    def __str__(self):
        return f"Vector({','.join(map(str, self.args))})"

    def __add__(self, other):
        if len(self.args) != len(other.args):
            raise ValueError("Vectors must be the same size")
        else:
            return Vector(*(x1 + x2 for x1, x2 in zip(self.args, other.args)))

    def __sub__(self, other):
        if len(self.args) != len(other.args):
            raise ValueError("Vectors must be the same size")
        else:
            return Vector(*(x1 - x2 for x1, x2 in zip(self.args, other.args)))

    def __mul__(self, other):
        # Handling dot product
        if isinstance(other, Vector):  # Dot product
            if len(self.args) != len(other.args):
                raise ValueError("Vectors must be the same size")
            return sum(x1 * x2 for x1, x2 in zip(self.args, other.args))
        elif isinstance(other, (int, float),):  # Scalar multiplication
            return Vector(*(x * other for x in self.args))
        else:
            raise ValueError("Multiplication only supports scalar or vector")

    def magnitude(self):
        return math.sqrt(sum(x ** 2 for x in self.args))  # Return scalar magnitude

    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize zero vector")
        else:
            return Vector(*(x / mag for x in self.args))

if __name__ == "__main__":
    # Create vectors
    v1 = Vector(1, 2, 3)
    v2 = Vector(4, 5, 6)

    # Print the vector
    print(v1)          # Output: Vector(1, 2, 3)

    # Addition
    v3 = v1 + v2
    print(v3)          # Output: Vector(5, 7, 9)

    # Subtraction
    v4 = v2 - v1
    print(v4)          # Output: Vector(3, 3, 3)

    # Dot product
    dot_product = v1 * v2
    print(dot_product) # Output: 32

    # Scalar multiplication
    v5 = v1*3 # Scalar multiplication (3 * v1)
    print(v5)          # Output: Vector(3, 6, 9)

    # Magnitude
    print(v1.magnitude())  # Output: 3.7416573867739413

    # Normalization
    v_unit = v1.normalize()
    print(v_unit)      # Output: Vector(0.267, 0.534, 0.801)
