import math
import time
import os

A, B, C = 0, 0, 0

cubeWidth = 20
width = 160
height = 44
zBuffer = [0] * (width * height)
buffer = ['.'] * (width * height)
backgroundASCIICode = '.'
distanceFromCam = 100
horizontalOffset = 0
K1 = 40
incrementSpeed = 0.6

def calculateX(i, j, k):
    return j * math.sin(A) * math.sin(B) * math.cos(C) - k * math.cos(A) * math.sin(B) * math.cos(C) + j * math.cos(A) * math.sin(C) + k * math.sin(A) * math.sin(C) + i * math.cos(B) * math.cos(C)

def calculateY(i, j, k):
    return j * math.cos(A) * math.cos(C) + k * math.sin(A) * math.cos(C) - j * math.sin(A) * math.sin(B) * math.sin(C) + k * math.cos(A) * math.sin(B) * math.sin(C) - i * math.cos(B) * math.sin(C)

def calculateZ(i, j, k):
    return k * math.cos(A) * math.cos(B) - j * math.sin(A) * math.cos(B) + i * math.sin(B)

def calculateForSurface(cubeX, cubeY, cubeZ, ch):
    x = calculateX(cubeX, cubeY, cubeZ)
    y = calculateY(cubeX, cubeY, cubeZ)
    z = calculateZ(cubeX, cubeY, cubeZ) + distanceFromCam

    ooz = 1 / z

    xp = int(width / 2 + horizontalOffset + K1 * ooz * x * 2)
    yp = int(height / 2 + K1 * ooz * y)

    idx = xp + yp * width
    if 0 <= idx < width * height:
        if ooz > zBuffer[idx]:
            zBuffer[idx] = ooz
            buffer[idx] = ch

def main():
    os.system('clear')
    while True:
        buffer[:] = [backgroundASCIICode] * (width * height)
        zBuffer[:] = [0] * (width * height)

        cubes = [(20, -2 * 20), (10, 1 * 10), (5, 8 * 5)]
        for cubeWidth, offset in cubes:
            horizontalOffset = offset
            cubeX = -cubeWidth
            while cubeX < cubeWidth:
                cubeY = -cubeWidth
                while cubeY < cubeWidth:
                    calculateForSurface(cubeX, cubeY, -cubeWidth, '@')
                    calculateForSurface(cubeWidth, cubeY, cubeX, '$')
                    calculateForSurface(-cubeWidth, cubeY, -cubeX, '~')
                    calculateForSurface(-cubeWidth, cubeY, cubeWidth, '#')
                    calculateForSurface(cubeX, -cubeWidth, -cubeY, ';')
                    calculateForSurface(cubeX, cubeWidth, cubeY, '+')
                    cubeY += incrementSpeed
                cubeX += incrementSpeed

        print('\x1b[H')
        for i in range(0, len(buffer), width):
            print(''.join(buffer[i:i+width]))

        global A, B, C
        A += 0.05
        B += 0.05
        C += 0.01
        time.sleep(0.016)

if __name__ == '__main__':
    main()
