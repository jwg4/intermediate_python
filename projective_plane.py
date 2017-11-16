from finite_field import FiniteField


class ProjectivePlane(object):
    def __init__(self, field):
        self.field = field

        class Point(object):
            def __init__(self, x, y, z):
                self.x = field.FFPoint(x)
                self.y = field.FFPoint(y)
                self.z = field.FFPoint(z)
                try:
                    self.X = self.x / self.z
                    self.Y = self.y / self.z
                    self.type = "plane"
                except:
                    try:
                        self.X = self.x / self.y
                        self.Y = None
                        self.type = "line"
                    except:
                        self.X = None
                        self.Y = None
                        self.type = "point"

            def __eq__(self, a):
                return (
                    self.X == a.X
                    and self.Y == a.Y
                    and self.type == a.type
                )

            def __str__(self):
                return "Point %s, %s" % (self.X, self.Y)

            def __repr__(self):
                return "Point(%d, %d, %d)" % (self.x, self.y, self.z)
        
        self.Point = Point

    def __call__(self, x, y, z):
        return self.Point(
            x, y, z
        )
