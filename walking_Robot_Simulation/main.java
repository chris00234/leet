class Solution {
    public int robotSim(int[] commands, int[][] obstacles) {
            HashMap<Pair<Integer,Integer>,Boolean> visited=new HashMap<>();
        for(int[] arr:obstacles){
            visited.put(new Pair<>(arr[0],arr[1]),true);
        }
        int r=0,col=0;
        int row_incr=0,incr=1;
        HashMap<Pair<Character,Integer>,Character> allDirs=new HashMap<>();
        allDirs.put(new Pair<>('e',-1),'s');
        allDirs.put(new Pair<>('e',-2),'n');
        allDirs.put(new Pair<>('n',-1),'e');
        allDirs.put(new Pair<>('n',-2),'w');
        allDirs.put(new Pair<>('w',-1),'n');
        allDirs.put(new Pair<>('w',-2),'s');
        allDirs.put(new Pair<>('s',-1),'w');
        allDirs.put(new Pair<>('s',-2),'e');
        // System.out.println(allDirs.get(new Pair('e',-2)));
        Character curr_dir='e';
        int ans=-1;
        for(int v:commands){
            if(v==-1){
                curr_dir=allDirs.get(new Pair(curr_dir,-1));
            }
            else if(v==-2){
                curr_dir=allDirs.get(new Pair(curr_dir,-2));
            }
            System.out.println(curr_dir);
            if(curr_dir=='e'){
                row_incr=0;
                incr=1;
            }
            else if(curr_dir=='w'){
                row_incr=0;
                incr=-1;
            }
            else if(curr_dir=='n'){
                row_incr=-1;
                incr=0;
            }
            else{
                row_incr=1;
                incr=0;
            }
            for(int i=0;i<v;i++){
                int r2=r+row_incr;
                int c2=col+incr;
                System.out.println(r2+" "+c2);
                if(visited.getOrDefault(new Pair(r2,c2),false)==true){
                    System.out.println("breaked");
                    break;
                }
                r+=row_incr;
                col+=incr;
                ans=Math.max(ans,r*r+col*col);
            }
        }
        if(ans==-1){
            return 0;
        }
        return ans;
    }
}
