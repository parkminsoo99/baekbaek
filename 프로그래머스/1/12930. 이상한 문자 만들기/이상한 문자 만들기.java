import java.util.*;

class Solution {
    public String solution(String s) {
        StringBuilder sb = new StringBuilder();
        int count = 0;
        for(char c: s.toCharArray()){   
            if(c == ' '){
                count = 0;
                sb.append(" ");
            }
            else{
                if(count % 2 ==0) sb.append(Character.toUpperCase(c));
                else sb.append(Character.toLowerCase(c));
                count +=1;
            }
            
        }
        return sb.toString();
    }
}
