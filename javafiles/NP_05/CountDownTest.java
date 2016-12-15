public class CountDownTest implements Runnable {

  private String name;

  public CountDownTest(String name) {
    this.name = name;
  }

  public void run() {
    for (int i = 3; i >= 0 ; i--) {
      try {
        Thread.sleep(1000);
      } catch (InterruptedException e) {}
      System.out.println(name + " : " + i);
    }
  }

  public static void main(String[] args) {
    CountDownTest cdt1 = new CountDownTest("thread 1");
    CountDownTest cdt2 = new CountDownTest("thread 2");
    Thread t1 = new Thread(cdt1);
    Thread t2 = new Thread(cdt2);
    t1.start();
    t2.start();
  }

}
