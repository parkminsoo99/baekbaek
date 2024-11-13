import java.util.*;

class Solution {
    int x = 0;
    int y = 0;

    // 이동할 수 있는지 여부를 체크하는 메서드
    private boolean isCanGo() {
        return x <= 5 && x >= -5 && y <= 5 && y >= -5;
    }

    public int solution(String dirs) {
        Set<Pair> set = new HashSet<>();
        set.add(new Pair(1, 2));
        set.add(new Pair(1, 2));  // 중복된 Pair이므로 추가되지 않음

        List<Pair> list = new ArrayList<>(set);
        System.out.println(set);  // 출력: [(1, 2)]

        // 첫 번째 Pair의 값을 각각 a, b에 저장
        Pair pair = list.get(0);
        int a = pair.getFirst();  // 1
        int b = pair.getSecond(); // 2
        System.out.println(a + "" + b);

        // dirs 문자열을 순회하며 각 방향에 맞는 처리를 해주어야 함
        for (char c : dirs.toCharArray()) {
            if (c == 'U' && isCanGo()) {
                // 'U' 방향 처리 (상)
            }
        }

        int answer = 0;
        return answer;
    }
}

class Pair {
    int first;
    int second;

    // 생성자
    public Pair(int first, int second) {
        this.first = first;
        this.second = second;
    }

    // equals 메서드 오버라이드 (두 Pair가 동일한지 비교)
    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Pair pair = (Pair) o;
        return first == pair.first && second == pair.second;
    }

    // first 값 반환
    public int getFirst() {
        return first;
    }

    // second 값 반환
    public int getSecond() {
        return second;
    }
    @Override
    public int hashCode(){
        return Objects.hash(first,second);
        
    }
    // Pair의 문자열 표현
    @Override
    public String toString() {
        return "(" + first + ", " + second + ")";
    }
}
