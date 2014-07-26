"""regularPolygon.

    Compute the area, apothem, radius, and interior angle of regular polygons.
    Apothem is the radius of the inscribed circle (line from the side to the
    center of the polygon).
    Radius is the radius of the circumcircle (line from the center of the
    angle formed by two sides to the center of the polygon).

    return float
    
"""

import math

def area(numberOfSides, aSideLength, apothem):
        if numberOfSides > 4:
                anArea = 0.5 * numberOfSides * aSideLength * apothem
        # Error
        else: anArea = 0
        return anArea

def areaByApothem(numberOfSides, apothem):
        # Square
        if numberOfSides == 4:
                anArea = (apothem * 2.0) ** 2
        # Regular Polygon
        elif numberOfSides > 4:
                anArea = numberOfSides * (apothem ** 2) * (math.tan(math.pi/numberOfSides))
        # Error
        else : anArea = 0
        return anArea

def areaByRadius(numberOfSides, radius):
        # Regular Polygon
        if numberOfSides > 3:
                anArea = (numberOfSides / 2) * (radius ** 2) * (math.sin(math.pi * 2/numberOfSides))
        # Error
        else : anArea = 0
        return anArea

def areaBySideLength(numberOfSides, aSideLength):
        # Triangle
        if numberOfSides == 3:
                anArea = ((aSideLength ** 2) * math.sqrt(3)) / 4
        # Square
        elif numberOfSides == 4:
                anArea = (aSideLength) ** 2
        # Regular Polygon
        elif numberOfSides > 4:
                anArea = (numberOfSides * (aSideLength ** 2)) / (4.0 * math.tan(math.pi/numberOfSides))
        # Error         
        else : anArea = 0
        return anArea

def apothem (numberOfSides, aSideLength):
        # Regular Polygon
        if numberOfSides > 3:
                anApothem = (aSideLength/2.0) * (1.0 / (math.tan(math.pi / numberOfSides)))
        else: anApothem = 0
        return anApothem

def radius (numberOfSides, aSideLength):
        # Regular Polygon
        if numberOfSides > 3:
                aRadius = (aSideLength/2.0) * (1.0 / (math.sin(math.pi / numberOfSides)))
        else: aRadius = 0
        return aRadius

# Results in degrees
def interiorAngleDegree (numberOfSides):
        if numberOfSides > 3:
                anInteriorAngle = ((numberOfSides - 2.0) / numberOfSides) * 180.0
        # Error
        else: anInteriorAngle = 0
        return anInteriorAngle

# Results in radians
def interiorAngle (numberOfSides):
        if numberOfSides > 3:
                anInteriorAngle = ((numberOfSides - 2.0) / numberOfSides) * math.pi
        # Error
        else: anInteriorAngle = 0
        return anInteriorAngle

if __name__ == "__main__":      #Test run results
    #If the calculations match, print True otherwise print False.
    # Check some of the area calculations
    testData = ((6, 2.5, 21.650635094610966),
                (6, 5, 86.60254037844386),
                (4, 2.5, 25.0),
                (4, 5, 100))
    valid = True
    for x in testData:
      valid = valid and areaByApothem(x[0], x[1]) == x[2]
    # Check the interior angle calculations
    valid = valid and math.radians(interiorAngleDegree(6)) == interiorAngle(6)
    print valid
    
