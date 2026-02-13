class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        for i in range(0, len(flowerbed)):
            if i == 0 and len(flowerbed) == 1:
                if n != 0:
                    if flowerbed[i] == 0:
                        return True
                elif n == 0 or flowerbed[i] == 1:
                    return True
                else: return False
            if n == 0:
                return True
            if i == 0:
                if flowerbed[i] == 0 and flowerbed[i+1] != 1:
                    flowerbed[i] = 1
                    n -= 1
            elif i == len(flowerbed)-1:
                if flowerbed[i] == 0 and flowerbed[i-1] != 1:
                    flowerbed[i] = 1
                    n -= 1
            elif flowerbed[i] == 0 and flowerbed[i-1] != 1 and flowerbed[i+1] != 1:
                flowerbed[i] = 1
                n -= 1      
        if n == 0:
            return True
        else:
            return False