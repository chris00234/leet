class Solution {
    public int[] frequencySort(int[] nums) {
        Map<Integer, Integer> map = new HashMap<Integer,Integer>();
        List<Integer> ans = new ArrayList<>();
        for(int num: nums){
            ans.add(num);
            if(map.get(num) == null){
                map.put(num, 1);
            }
            else{
                map.put(num, map.get(num) + 1);
            }
        }
        Collections.sort(ans, (a, b) ->                 
            (map.get(a) == map.get(b))? b - a : map.get(a) - map.get(b)
        );

        return ans.stream().mapToInt(i -> i).toArray();
    }
}
