import java.util.*;

public class test {

    public static int countvowels(String inputStr) {
        return Arrays.asList(inputStr.split("")).stream().filter(str-> "aeiouAEIOU".contains(str)).toArray().length;
    }

    public static void main(String[] args) {
        System.out.println("this code counts vowels");
        System.out.format("the number of vowels in hello is %d.\n", countvowels("hello"));        
    }


}


