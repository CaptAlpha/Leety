class Solution {
    public boolean canEatInTimeK(int k, int h, int[] piles) {
        long timeTaken = 0; // Use long to avoid integer overflow
        for (int i : piles) {
            if (i % k == 0) {
                timeTaken += i / k;
            } else {
                timeTaken += i / k + 1;
            }
        }
        return timeTaken <= h;
    }

    public int minEatingSpeed(int[] piles, int h) {
        int max = -1;
        for (int i : piles) {
            if (i > max) {
                max = i;
            }
        }
        int left = 1;
        int right = max;
        int mid = left + (right - left) / 2;

        while (left <= right) {
            if (canEatInTimeK(mid, h, piles)) {
                right = mid - 1; // Try to find a smaller k
            } else {
                left = mid + 1; // Increase k
            }
            mid = left + (right - left) / 2;
        }
        return mid; // Return left, not mid
    }
}