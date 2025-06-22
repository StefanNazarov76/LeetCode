class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        if coordinates[0] in 'aceg':
            if int(coordinates[1]) % 2 == 0:
                return True
            else:
                return False

        else:
            if int(coordinates[1]) % 2 != 0:
                return True
            else:
                return False
