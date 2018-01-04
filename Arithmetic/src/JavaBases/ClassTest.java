package JavaBases;


/**
 * Created by xiongchi on 2017/12/28.
 */
public class ClassTest {

    static  class Gum{
        static {
            System.out.println("loading Gum");
        }
    }

    public void run(){

        try {
            Class.forName("ClassTest");
            Class.forName("Gum");
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
//        ClassTest ct = new ClassTest();
//        ct.run();
        try {
            Class.forName("JavaBases.Toy");
            //创建对象是就运行static中的代码
            Toy toy = new Toy();
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        }

    }


}
