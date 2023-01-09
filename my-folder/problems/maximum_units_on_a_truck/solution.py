class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x:x[1],reverse=True)
        total_u=0

        for box,units in boxTypes:
            if truckSize<=box:
                total_u=total_u+truckSize*units
                break


            total_u+=units*box
            truckSize-=box
            

        

        return total_u
