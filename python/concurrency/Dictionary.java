 public class Dictionary {
     private final ReadWriteLock readWriteLock =  new ReadWriteLock();

     private HashMap<String, String> dictionary =
                                        new HashMap<String, String>();

     public void edit(String key, String value) {
         readWriteLock.lockWrite();
         try {
             dictionary.put(key, value);
        }
        finally {
            readWriteLock.unlockWrite();
            }
    }

   public String get(String key) {
       readWriteLock.lockRead();
       try{
           return dictionary.get(key);
       } finally {
           readWriteLock.unlockRead();
     }
   }
}
