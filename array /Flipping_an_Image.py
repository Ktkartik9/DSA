# Problem: Flipping an Image

# Method: In-Place Row Reversal and Bit Inversion

# Logic:
        """Iterate through each row in image and reverse its elements in-place to flip it horizontally
           Then iterate through every element in each reversed row and invert its bit by performing
           1 - element (0 becomes 1, and 1 becomes 0)"""


class Solution:
    def flipAndInvertImage(self, image):
        for i in image:
            i.reverse()

            for j in range(len(i)):
                i[j] = 1 - i[j]
        
        return image
