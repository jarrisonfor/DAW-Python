import os
import math
import random


def initColors():
    os.system("cls")


def findLargestElement(rows, cols, lengthArray, matrix):
    for i in range(rows):
        for j in range(cols):
            lengthArray.append(len(str(matrix[i][j])))
    lengthArray.sort()
    largestElementLength = lengthArray[-1]

    return largestElementLength


def createMatrix(rows, cols, matrixToWorkOn, matrix):
    for i in range(rows):
        matrixToWorkOn.append([])
        for j in range(cols):
            matrixToWorkOn[i].append(str(matrix[i][j]))


def makeRows(rows, cols, largestElementLength, rowLength, matrixToWorkOn, finalTable, color):

    for i in range(rows):
        currentRow = ""
        for j in range(cols):
            if ((color != None) and (j == 0 or i == 0)):
                currentEl = " " + "\033[38;2;" + str(color[0]) + ";" + str(
                    color[1]) + ";" + str(color[2]) + "m" + matrixToWorkOn[i][j] + "\033[0m"
            else:
                currentEl = " " + matrixToWorkOn[i][j]

            if (largestElementLength != len(matrixToWorkOn[i][j])):
                if (color != None):
                    if (j == 0 or i == 0):
                        currentEl = currentEl + " " * (largestElementLength - (len(currentEl) - len("\033[38;2;" + str(
                            color[0]) + ";" + str(color[1]) + ";" + str(color[2]) + "m" + "\033[0m")) + 2) + "|"
                    else:
                        currentEl = currentEl + " " * \
                            (largestElementLength - len(currentEl) + 2) + "|"
                else:
                    currentEl = currentEl + " " * \
                        (largestElementLength - len(currentEl) + 2) + "|"
            else:
                currentEl = currentEl + " " + "|"
            currentRow += currentEl
        finalTable.append("|" + currentRow)
    if (color != None):
        rowLength = len(currentRow) - len("\033[38;2;" + str(color[0]) + ";" + str(
            color[1]) + ";" + str(color[2]) + "m" + "\033[0m")
    else:
        rowLength = len(currentRow)

    return rowLength


def createWrappingRows(rowLength, finalTable):
    wrappingRows = ""
    for i in range(rowLength - 1):
        wrappingRows += "-"
    wrappingRows = "+" + wrappingRows
    wrappingRows += "+"

    finalTable.insert(0, wrappingRows)
    finalTable.append(wrappingRows)


def createRowUnderFields(largestElementLength, cols, finalTable):
    rowUnderFields = ""
    for j in range(cols):
        currentElUnderField = "+"
        currentElUnderField = currentElUnderField + \
            "-" * (largestElementLength + 2)
        rowUnderFields += currentElUnderField
    rowUnderFields += "+"
    finalTable.insert(2, rowUnderFields)


def printRowsInTable(finalTable):
    for row in finalTable:
        print(row)


def printTable(matrix, useFieldNames=False, color=None):
    rows = len(matrix)
    cols = len(matrix[0])
    lengthArray = []
    largestElementLength = None
    rowLength = None
    matrixToWorkOn = []
    finalTable = []

    largestElementLength = findLargestElement(rows, cols, lengthArray, matrix)
    createMatrix(rows, cols, matrixToWorkOn, matrix)
    rowLength = makeRows(rows, cols, largestElementLength,
                         rowLength, matrixToWorkOn, finalTable, color)
    createWrappingRows(rowLength, finalTable)
    if (useFieldNames):
        createRowUnderFields(largestElementLength, cols, finalTable)
    printRowsInTable(finalTable)
