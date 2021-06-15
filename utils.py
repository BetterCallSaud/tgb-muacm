
# method for returning the maximum occuring element 
# from a list
def getMaximumOccuringElement(_List):
  return max(set(_List), key=_List.count)
