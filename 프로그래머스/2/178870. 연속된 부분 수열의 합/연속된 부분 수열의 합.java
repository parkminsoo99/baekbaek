class Solution {
    public int[] solution(int[] sequence, int k) {
        int[] answer = new int[2];
        int end = 0;
        int min = Integer.MAX_VALUE;
        int min_start = 0;
        int min_end = 0;
        int sum = 0;
        for(int start = 0; start <sequence.length;start++){
            while(sum < k && end < sequence.length){
                sum += sequence[end];
                end +=1;
            }
            //같을 때
            if(k == sum) {
                int isMin = end - start;
                if(min > isMin){
                    min = isMin;
                    min_start = start;
                    min_end = end-1;
                }
            }
            sum -= sequence[start];
        }
        answer[0] = min_start;
        answer[1] = min_end;
        return answer;
    }
}