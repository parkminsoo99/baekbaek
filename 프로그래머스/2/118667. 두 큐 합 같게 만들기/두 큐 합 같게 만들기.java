import java.util.*;

class Solution {
    public int solution(int[] queue1, int[] queue2) {
        // 두 큐를 하나의 연속 배열처럼 활용하기 위해 초기화
        Deque<Long> q1 = new ArrayDeque<>();
        Deque<Long> q2 = new ArrayDeque<>();
        long sum1 = 0, sum2 = 0;
        
        for (long num : queue1) {
            q1.add(num);
            sum1 += num;
        }
        for (long num : queue2) {
            q2.add(num);
            sum2 += num;
        }
        
        // 두 큐의 합이 홀수면 나누는 것이 불가능
        if ((sum1 + sum2) % 2 != 0) {
            return -1;
        }
        
        long target = (sum1 + sum2) / 2;
        int maxOperations = (queue1.length + queue2.length) * 2; // 최대 가능한 이동 횟수
        int operations = 0;

        // 큐 상태를 조정하여 합을 맞추기
        while (operations <= maxOperations) {
            if (sum1 == target) {
                return operations; // 두 큐의 합이 같아진 경우
            } else if (sum1 > target) {
                // sum1이 더 크면 q1에서 하나 빼서 q2로 이동
                long num = q1.pollFirst();
                sum1 -= num;
                sum2 += num;
                q2.addLast(num);
            } else {
                // sum2가 더 크면 q2에서 하나 빼서 q1으로 이동
                long num = q2.pollFirst();
                sum2 -= num;
                sum1 += num;
                q1.addLast(num);
            }
            operations++;
        }

        // 여기까지 왔다면 합을 맞출 수 없는 경우
        return -1;
    }
}
