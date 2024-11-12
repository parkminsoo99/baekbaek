import java.util.*;
class Solution {
    public int[] solution(long n) {
        String string = Long.toString(n);
        Deque<Integer> q = new ArrayDeque<>();
        for(char c : string.toCharArray()){
            q.addFirst(Character.getNumericValue(c));
        }
        int[] answer = new int[q.size()];
        int count = 0;
        for(Integer i:q){
            answer[count++] = i;
        }
        return answer;
    }
}