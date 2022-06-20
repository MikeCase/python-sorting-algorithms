import random
from helper_decorators import MyDecorators


class SortAlgos:

  def __init__(self):
    pass

  @MyDecorators.timer
  def py_default_sorting_algo(self, sel: list):
    """ Python's default sort function. It uses the timsort algorithm """
    return sorted(sel)

  @MyDecorators.timer
  def selectionSort(self, sel: list):
    """ Selection sort with single while loop."""

    # Define a counter variable (i)
    # loop over the lenth of the list
    # Select the smallest value in the list assign to variable (smallest)
    # set the index of the smallest element (index_of_smallest)
    # Swap values of the current element with the element currently defined as the smallest element.
    # Update counter variable, move back to step one of the loop.
    # loop finished, return the sorted list.

    ## PSEUDO CODE ##
    # idx=0
    # while idx is less than the length of the list
    #   get smallest element
    #   get index of the smallest element
    #   set current index to value of smallest index
    #   increment index
    # return updated list

    i=0
    while i < len(sel):
      smallest = min(sel[i:])
      index_of_smallest = sel.index(smallest)
      sel[i],sel[index_of_smallest] = sel[index_of_smallest],sel[i]
      i+=1
    return sel

  @MyDecorators.timer
  def bubbleSort(self, sel: list):
    """ BubbleSort algorithm

        ## PSEUDO CODE ##
        get length of list
        loop over list from 0 to length
          loop over list again from 0 to length - first loop index - 1
            if list index value > list index + 1 value
              swap indexes.
        loop finished return sorted list
    """
    n = len(sel)
    for i in range(n):
      for j in range(0, n-i-1):
        if sel[j] > sel[j+1]:
          sel[j], sel[j+1] = sel[j+1], sel[j]
      # i+=1

    return sel

  @MyDecorators.timer
  def combSort(self, sel: list):
    """ Comb Sort Algorithm. Improvement on Bubble Sort

    ### PSEUDO CODE ###
    get list length
    set the gap to the length of the list
    default swapped to true for while loop to run
    loop if gap not equal 1 or swapped == true
      set gap to 1.3 * smaller than current gap length
      set swapped to false
      loop from 0 to list length - gap size
        if list index value > list index + gap value
          swap current index value with list index + gap value
          set swapped back to true to continue while loop
      loop finished return list.
    """
    n = len(sel)
    gap = n
    swapped = True

    while gap != 1 or swapped == 1:
      gap = self._getNextGap(gap)
      swapped = False

      for i in range(0, n-gap):
        if sel[i] > sel[i+gap]:
          sel[i], sel[i+gap]=sel[i+gap], sel[i]
          swapped = True

    return sel

  def _getNextGap(self, gap):
    """ Comb Sort helper function """
    gap = (gap*10)//13
    if gap < 1:
      return 1
    return gap

  @MyDecorators.timer
  def insertionSort(self, sel: list):
    """ Insertion Sort Algorithm """

    for i in range(1, len(sel)):
      key = sel[i]
      j = i-1
      while j >= 0 and key < sel[j]:
        sel[j+1] = sel[j]
        j -= 1
      sel[j+1] = key
    return sel


  def mergeSort(self, sel: list):
    """ Merge Sort Algorithm """
    if len(sel) > 1:
      # Find middle of the list
      mid = len(sel)//2

      # Create two new lists for the halves of the original list
      L = sel[:mid]
      R = sel[mid:]
      self.mergeSort(L)
      self.mergeSort(R)
      i=j=k=0

      while i < len(L) and j < len(R):
        if L[i] < R[j]:
          sel[k] = L[i]
          i += 1
        else:
          sel[k] = R[j]
          j += 1
        k += 1

      while i < len(L):
        sel[k] = L[i]
        i += 1
        k += 1

      while j < len(R):
        sel[k] = R[j]
        j += 1
        k += 1


    return sel