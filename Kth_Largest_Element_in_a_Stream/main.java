class KthLargest {
    private ArrayList<Integer> arr = new ArrayList<>();
    private int ret;
    public KthLargest(int k, int[] nums) {
        Arrays.sort(nums);
        ret = k;
        int st = ret < nums.length ? ret : nums.length;
        if(nums.length > 0){
            for(int i = 0; i < st; i++){
                arr.add(nums[nums.length - i - 1]);
            }
        }
    }
    
    public int add(int val) {

        arr.add(val);
        Collections.sort(arr, Collections.reverseOrder());
        
        return arr.get(ret - 1);
    }
}

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest obj = new KthLargest(k, nums);
 * int param_1 = obj.add(val);
 */
