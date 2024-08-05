class Solution {
    public String kthDistinct(String[] arr, int k) {
        Map<String, Integer> mp = new LinkedHashMap<String, Integer>();

        for(String s: arr){
            mp.put(s, mp.getOrDefault(s, 0) + 1);
        }
        String ret = "";
        if(mp.size() < k){
            return ret;
        }
        int pos = 0;
        for(String key: mp.keySet()){
            if(mp.get(key) == 1) pos += 1;
            if(pos == k){
                ret = key;
                break;
            }
            
        }
        return ret;
    }

}
