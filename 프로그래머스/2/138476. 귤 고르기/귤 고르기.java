import java.util.*;
class Solution {
    public int solution(int k, int[] tangerine) {
        HashMap<Integer, Integer> map = new HashMap<>();
        int answer = 0;
        for(int i = 0; i < tangerine.length; i++){
            map.put(tangerine[i],map.getOrDefault(tangerine[i],0)+1);
        }
        List<Integer> list = new ArrayList<>(map.values());
        Collections.sort(list,Collections.reverseOrder());
        for(int i:list){
            k = k - i;
            if(k <= 0){
                answer +=1;
                break;
            }
            answer +=1;
        }
       
        return answer;
    }
}