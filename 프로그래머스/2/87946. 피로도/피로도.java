import java.util.*;
class Solution {
    int max = 0;
    int[][] customDungeons;
    public int solution(int k, int[][] dungeons) {
        boolean[] visited = new boolean[dungeons.length];
        customDungeons=dungeons;
        int originalLife = k;
        for(int i = 0; i< customDungeons.length; i++){
            k = originalLife;
            
            if(canIgo(customDungeons[i],k)){
                k -= customDungeons[i][1];
                bruthForth(i, visited.clone(), 1, k);
            }
        }
        int answer = max;
        return answer;
    }
    private void bruthForth(int start, boolean[] visited, int count, int life){
        visited[start] = true;
        if (max < count) max = count;
        for(int i = 0; i< customDungeons.length; i++){
            if(canIgo(customDungeons[i], life) && visited[i] != true){
                life -= customDungeons[i][1];
                count +=1;
                bruthForth(i, visited.clone(), count, life);
                life += customDungeons[i][1];
                count -=1;
            }
        }
        return;
    }
    private boolean canIgo(int[] dungeons,int life){
        return dungeons[0] <= life;
    }
}