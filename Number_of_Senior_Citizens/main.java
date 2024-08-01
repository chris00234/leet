class Solution {
    public int countSeniors(String[] details) {
        int total = 0;
        for(String detail : details){
            int age = 0;
            for(int i = 0; i < detail.length(); i++){
                if(detail.charAt(i) >= 'A' && detail.charAt(i) <= 'Z'){
                    i += 1;
                    age += detail.charAt(i) - '0';
                    age *=10;
                    i += 1;
                    age += detail.charAt(i) - '0';
                    if(age > 60){
                        total++;
                    }
                    break;

                }
            }
        }
        return total;
    }
}
