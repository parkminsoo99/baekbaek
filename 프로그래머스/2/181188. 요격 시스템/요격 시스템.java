import java.util.*;
class Solution {
    public int solution(int[][] targets) {
        int answer = 0;
        Arrays.sort(targets, (a,b) -> {return a[1]-b[1];});
        Deque<int[]> list = new ArrayDeque<>(Arrays.asList(targets));
        while(!list.isEmpty()){
            System.out.println();
            int[] poped1 = list.removeFirst();
            int start1 = poped1[0];
            int end1 = poped1[1];
            while(!list.isEmpty()){
                int[] poped2 = list.removeFirst();
                int start2 = poped2[0];
                int end2 = poped2[1];
                if(end1 <= start2){
                    list.addFirst(new int[] {start2, end2});
                    break;
                }
            }         
            answer +=1;   
        }  
        return answer;
    }
}