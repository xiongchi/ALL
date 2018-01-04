package designpattern;

/**
 * Created by xiongchi on 2017/12/27.
 */
public class test1 {

    class animal{
        public void play(){
            System.out.println("animal....");
        };

        public void who(animal a){
            a.play();
        }
    }

    class cat extends animal{

        @Override
        public void play() {
            super.play();
            System.out.println("cat play");
        }
    }

    class dog extends animal{
        @Override
        public void play() {
            super.play();
            System.out.println("dog play");
        }
    }

    public void test() {
        animal a = new cat();
        a.who(new cat());
    }

    public static void main(String[] args) {
        test1 t1 = new test1();
        t1.test();
    }
}
