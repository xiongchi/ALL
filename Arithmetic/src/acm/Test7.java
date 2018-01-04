package acm;

/**
 * Created by xiongchi on 2017/12/22.
 * 请实现一个函数，将一个字符串中的空格替换成“%20”。
 * 例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
 */
public class Test7 {
    public String replaceSpace(StringBuffer str) {
        StringBuffer newStr = new StringBuffer();
        for(int i = 0; i < str.length(); i++){
            if (str.charAt(i) == ' '){
                newStr.append("%20");
            }else
                newStr.append(str.charAt(i));
        }
        return newStr.toString();

    }
}
