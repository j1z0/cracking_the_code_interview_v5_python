'''
Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
'''

def rotate(matrix, num_layers):
    for layer in range(num_layers / 2):
        first = layer
        last = num_layers - 1 - layer
        for i in range(first, last):
            offset = i - first

            top = matrix[first][i]

            # left -> top
            matrix[first][i] = matrix[last-offset][first]

            # bottom -> left
            matrix[last - offset][first] = matrix[last][last - offset]

            # right -> bottom
            matrix[last][last - offset] = matrix[i][last]

            # top -> right
            matrix[i][last] = top

    return matrix

if __name__ == "__main__":
    matrix = [[0,0,0,0],
              [0,0,0,0],
              [0,0,0,0],
              [1,1,1,1]]

    print rotate(matrix, 4)

