class Solution:
    def minAvailableDuration(self, slots1, slots2, duration: int):

        pointer1 = 0
        pointer2 = 0
        tbc = [0,0]



        while True:

            # loop invariant: at the beginning of each loop, the pointers are pointing at 
            # the unused time slot with smallest start time

            if pointer1 == len(slots1):
                return 

            elif pointer2 == len(slots2):  
                return 





            """#if the time slots of one people run out
            if pointer1 > len(slots1) or pointer2 > len(slots2):
                return []

            else:
                # choose a new slot (with earliest start time) to compare
                if pointer1 < len(slots1) and pointer2<len(slots2) and slots1[pointer1][0] <= slots2[pointer2][0]:
                    expected_slot = [slots1[pointer1][0],slots1[pointer1][0]+duration]

                    # if the expected time slot fits in itself
                    if slots1[pointer1][0] + duration <= slots1[pointer1][1]:
                        # if the expected slot fits in the other person's time
                        if expected_slot[0] >= tbc[0] and expected_slot[1] <= tbc[1]:
                            print(expected_slot)
                            return expected_slot
                    # if it doesn't fit, update the to_be_compared time slot
                    tbc = slots1[pointer1]
                    # increase the pointer
                    pointer1+=1
                elif pointer1 < len(slots1) and pointer2<len(slots2):
                    expected_slot = [slots2[pointer2][0],slots2[pointer2][0]+duration]


                    # if the expected time slot fits in itself
                    if slots2[pointer2][0] + duration <= slots2[pointer2][1]:
                        # if the expected slot fits in the other person's time
                        if expected_slot[0] >= tbc[0] and expected_slot[1] <= tbc[1]:
                            return expected_slot
                    # if it doesn't fit, update the to_be_compared time slot
                    tbc = slots2[pointer2]
                    # increase the pointer
                    pointer2+=1
                else:
                    return []"""

input = [[[10,50],[60,120],[140,210]],
[[0,15],[60,70]],
12]
s = Solution()
print(s.minAvailableDuration(input[0],input[1],input[2]))


