import java.util.*;
class Solution {
    public int solution(String[] want, int[] number, String[] discount) {
        int answer = 0;
        ArrayList<String> list = new ArrayList<>(Arrays.asList(discount));
        int sum = 0;
        int count = 0;
        for(int i: number){
            sum += i;
        }
        while (true){
            ArrayList<String> subList = new ArrayList<>();
            if( count+sum > discount.length) break;
            for(int j = count; j<count+sum; j++){
                subList.add(list.get(j));
            }
            for(int j = 0; j<want.length; j++){
                if(Collections.frequency(subList, want[j]) != number[j]) break;
                if(j == want.length -1) answer +=1;
            }
            count +=1;
        }
        
        return answer;
    }
}