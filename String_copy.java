
package string_copy;


public class Copy {
  
 
    
  public void Copy_1(String cadena_1, String cadena_2){
 
      for(int i = 0 ; i < cadena_1.length(); i++ ){
          
          String temp = String.valueOf(cadena_1.charAt(i));
          cadena_2 += temp;
      }
      
      System.out.println(cadena_2);
  
  }
      
      
  }
