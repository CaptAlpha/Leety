import java.util.HashMap;
class Solution {
    public int numIdenticalPairs(int[] nums) {
        HashMap<Integer, Integer> hash = new HashMap<>();

        for(int i: nums){
            hash.put(i, hash.getOrDefault(i, 0) + 1);
        } 

        int count = 0;

        for(int i: hash.keySet()){
            int frequency = hash.get(i);
            count += (frequency * (frequency - 1)) / 2;
        }
        return count;

    }
}