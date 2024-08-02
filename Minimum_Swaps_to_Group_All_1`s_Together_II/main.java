class Solution {
    public int minSwaps(int[] nums) {
        int l = nums.length;
        int[] ones = new int[l];
        ones[0] = nums[0] == 1 ? 1 : 0;
        for (int i = 1; i < l; i++) {
            if (nums[i] == 1) {
                ones[i] = ones[i - 1] + 1;
            } else {
                ones[i] = ones[i - 1];
            }
        }
        if (ones[l - 1] == l || ones[l - 1] == 0) {
            return 0;
        }
        int ws = ones[l - 1];
        int minSwaps = Integer.MAX_VALUE;
        int si = 0;
        int ei;
        while (si < nums.length) {
            ei = (si + ws - 1) % l;
            int totalones;
            if (ei >= si) {
                totalones = ones[ei] - (si == 0 ? 0 : ones[si - 1]);
            } else {
                totalones = ones[ei] + (ones[l - 1] - ones[si - 1]);
            }
            int swapsreq = ws - totalones;
            if (swapsreq < minSwaps) {
                minSwaps = swapsreq;
            }
            si++;
        }
        return minSwaps;
    }
}
