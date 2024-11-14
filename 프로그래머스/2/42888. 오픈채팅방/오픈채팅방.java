import java.util.*;
class Solution {
    public String[] solution(String[] record) {
        String[] splitedList = new String[3];
        HashMap<String, String> map = new HashMap<>();
        //map에 넣기
        int resultArraySize = 0;
        for(int i = 0; i< record.length;i++){
            splitedList = record[i].split(" ");
            if(splitedList[0].equals("Enter")){
                map.put(splitedList[1],splitedList[2]);
                resultArraySize +=1;
            }
            else if(splitedList[0].equals("Leave")){
                resultArraySize +=1;
            }
            else if(splitedList[0].equals("Change")){
                 map.put(splitedList[1],splitedList[2]);
            }
        }
        
        String[] answer = new String[resultArraySize];
        //result생성
        int count = 0;
        for(int i = 0; i< record.length;i++){
            splitedList = record[i].split(" ");
            if(splitedList[0].equals("Enter")){
                String s = map.get(splitedList[1]);
                answer[count++] = s + "님이 들어왔습니다.";
            }
            else if(splitedList[0].equals("Leave")){
                String s = map.get(splitedList[1]);
                answer[count++] = s + "님이 나갔습니다.";
            }
        }
        
        return answer;
    }
}