import java.util.*;
class Solution {
    public int solution(int[] queue1, int[] queue2) {
        Deque<Long> q1 = new ArrayDeque();
        Deque<Long> q2 = new ArrayDeque();
        int answer = 0;
        int count = 0;
        long SUM1 = 0;
        long SUM2 = 0;
        for(long i : queue1){
            q1.add(i);
            SUM1 += i;
        }
        for(long i : queue2){
            q2.add(i);
            SUM2 +=i;
        }
        long finish = (q1.size() + q2.size()) * 2;
        if((SUM1 + SUM2) % 2 == 1){
            answer = -1;
            return answer;
        }
        else{
            long divided = (long) (SUM1 + SUM2) / 2;
            long minusSUM1 = SUM1 - divided;
            long minusSUM2 = SUM2 - divided;
            long zeroValue = 0;
            if(minusSUM2 > minusSUM1){
                zeroValue = SUM2 - divided;
            }
            else{
                zeroValue = SUM1 - divided;
            }
            
            while (zeroValue != 0){//추후 -1일 때도 추가 필요
                if(count > finish){
                    answer = -1;
                    return answer;
                }
                if(minusSUM1 < minusSUM2 && zeroValue > 0){
                    count +=1;
                    long popped = q2.removeFirst();
                    zeroValue -= popped;
                    q1.addLast(popped);
                }
                if(minusSUM1 < minusSUM2 && zeroValue < 0){
                    count +=1;
                    long popped = q1.removeFirst();
                    zeroValue += popped;
                    q2.addLast(popped);
                }
                if(minusSUM1 > minusSUM2 && zeroValue > 0){
                    count +=1;
                    long popped = q1.removeFirst();
                    zeroValue -= popped;
                    q2.addLast(popped);
                }
                if(minusSUM1 > minusSUM2 && zeroValue < 0){
                    count +=1;
                    long popped = q2.removeFirst();
                    zeroValue += popped;
                    q1.addLast(popped);
                }
            }
        }
        answer = count;
        return answer;
    }
}