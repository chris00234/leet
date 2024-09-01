class Solution {
    public int[][] construct2DArray(int[] original, int m, int n) {
        int[][] ret = new int[m][n];
        if( m * n != original.length){
            return new int[0][0];
        }
        int pos = 0;
        for(int i = 0; i < m; i ++){
            for(int j = 0; j < n; j++){
                ret[i][j] = original[pos];
                pos += 1;
            }
        }
        return ret;
    }
}
