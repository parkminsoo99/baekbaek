import java.util.*;
import java.io.*;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int Start = Integer.parseInt(st.nextToken());
        boolean [] visited = new boolean[N+1];
        ArrayList<ArrayList<Integer>> list = new ArrayList<>();
        for(int i = 0; i < N+1; i++){
            list.add(new ArrayList<>());
        }
        for(int i = 0; i < M; i++){
            st = new StringTokenizer(bf.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            list.get(x).add(y);
            list.get(y).add(x);
        }
        for(int i = 0; i<N+1;i++){
            Collections.sort(list.get(i));
        }
        dfs(visited.clone(), list, Start);
        System.out.println();
        bfs(visited.clone(), list, Start);
    }
    static void bfs(boolean[] visited, ArrayList<ArrayList<Integer>> list, int start){
        visited[start] = true;
        Deque<Integer> q = new ArrayDeque<>();
        q.add(start);
        while(!q.isEmpty()){
            int poped = q.removeFirst();
            visited[poped] = true;
            System.out.print(poped+" ");
            for(Integer i: list.get(poped)){
                if(visited[i] != true){
                    q.add(i);
                    visited[i] = true;
                }
            }
        }
    }
    static void dfs(boolean[] visited, ArrayList<ArrayList<Integer>> list, int start){
        System.out.print(start+" ");
        visited[start] = true;
        for(Integer i: list.get(start)){
            if(visited[i] != true){
                dfs(visited,list,i);
            }
        }
    }
}
