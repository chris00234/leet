class Solution {
    public int rangeSum(int[] nums, int n, int left, int right) {
        int[] arr = new int[n*(n+1)/2];
        int pos = 0;
        for(int num : nums){
            arr[pos] = num;
            pos += 1;
        }
        for(int i = 0; i < nums.length; i++){
            int tmp = nums[i];
            for(int j = i + 1; j < nums.length; j++){
                tmp += nums[j];
                arr[pos] = tmp;
                pos += 1;
            }
        }
        Arrays.sort(arr);
        int ret = 0;
        final int mod = (int) 1e9 + 7;

        for(int t = left; t <= right; t++){
            ret = (ret +arr[t-1]) % mod;
        }

        return ret;
    }
}
