class Solution {
    public int[] getConcatenation(int[] nums) {
        int[] ret = new int[nums.length * 2];
        int i = 0;
        int k = 0;
        while (i < 2){
            for(int j = 0; j < nums.length; j++){
                ret[k]= (nums[j]);
                k += 1;
            }
            i++;
        }
        return ret;
    }
}
