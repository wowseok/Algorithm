class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0
        volume = 0

        left, right = 0, len(height) - 1 #양쪽 포인터
        left_max, right_max = height[left], height[right] # 처음에는 가장 양쪽의 장벽이 세워진다.

        while left < right: #왼쪽 포인터는 오른쪽 포인터보다 작아야함
            left_max = max(left_max, height[left])#양쪽의 장벽이 큰지, 현재 인덱스의 높이가 높은지
            right_max = max(right_max, height[right])

            if left_max <= right_max: #장벽의 높이가 오른쪽이 높은경우 오른쪽으로 나아가며 채워나가야한다.
                volume += left_max - height[left]
                left += 1
            
            else:
                volume += right_max - height[right] # 왼쪽이 높은경우 왼쪽으로 나아가며 채워나간다.
                right -= 1
        return volume

