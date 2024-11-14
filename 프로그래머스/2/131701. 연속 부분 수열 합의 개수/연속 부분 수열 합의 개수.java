import java.util.*;

class Solution {
    Set<Integer> set;

    public int solution(int[] elements) {
        set = new HashSet<>();
        Deque<Integer> q = new ArrayDeque<>();
        
        // 큐에 모든 요소 추가
        for (int i = 0; i < elements.length; i++) {
            q.addLast(elements[i]);
        }

        int n = elements.length;
        
        // 연속 부분 수열의 합을 구하는 로직
        for (int i = 0; i < n; i++) {
            int sum = 0;
            // 연속 부분 수열을 j번 만큼 진행
            for (int j = 0; j < n; j++) {
                // 큐에서 하나씩 빼고 합산
                int popped = q.removeFirst();
                sum += popped;
                set.add(sum);
                q.addLast(popped); // 다시 큐에 추가
            }
            // 큐의 상태를 초기화하는 부분
            for (int k = 0; k < n - 1; k++) {
                int popped = q.removeFirst();
                q.addLast(popped); // 회전시켜서 다시 원형으로 만들기
            }
        }

        return set.size(); // 고유한 합의 개수 반환
    }
}
