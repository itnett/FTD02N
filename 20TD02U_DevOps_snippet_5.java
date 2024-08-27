import static org.junit.Assert.assertEquals;
   import org.junit.Test;

   public class MyAppTest {
       @Test
       public void testAddition() {
           assertEquals(5, MyApp.add(2, 3));
       }
   }