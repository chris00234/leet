class Solution {
    public int minSteps(int n) {
        int count=1;
        int prev = 0;
        int steps=0;
        while(count<n){
            if((n-count)%count==0){
                prev=count;
                count+=count;
                steps+=2;
            }else if(prev!=0 && (n-count)%prev==0){
                count+=prev;
                steps++;
            }else{
                return -1;
            }
        }
        return steps;
    }
}

