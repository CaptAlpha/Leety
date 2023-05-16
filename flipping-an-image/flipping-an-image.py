class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            # Flip each row in the image
            image[i] = image[i][::-1]

            # Invert each pixel in the flipped row
            for j in range(len(image[i])):
                image[i][j] = 1 - image[i][j]

        return image
