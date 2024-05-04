/**
 * @param {number[]} people
 * @param {number} limit
 * @return {number}
 */
var numRescueBoats = function(people, limit) {
    let sorted_people = people.sort((a, b) => a - b);
    let l = 0;
    let r = people.length - 1;
    let total = people.length;
    let ans = 0;
    console.log(sorted_people);
    let val = 0;
    let num = 0;
    while(r > l){
        val += sorted_people[r] + sorted_people[l];
        if(val < limit){
            l++;
            r--;
            ans += 1;
            val = 0;
        }
        else if(val > limit){
            ans += 1;
            r--;
            val = 0;
        }
        else{
            r--;
            l++;
            ans+= 1;
            val = 0;
        }
    }
    return l === r ? ans + 1: ans;
}
// 50, 49, (2,47), (2,41,2), (6, 33, 6), (7, 26, 10), (10, 22, 10), (11, 18, 12), (13)
