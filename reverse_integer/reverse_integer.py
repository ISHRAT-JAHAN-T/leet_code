class Solution {
    public int reverse(int x) {
        
         int  nbr =x;
        long rev=0; 
      
        
        while(nbr!=0)
        {
            int digit=nbr%10; 
           // System.out.println("digit : " + rev);
            rev=rev*10+digit; 
           // System.out.println("reverse number is : " + rev);
            nbr=nbr/10;
            
        }
      //  System.out.println("reverse number is : " + rev);
        
         if (rev > Integer.MAX_VALUE || rev < Integer.MIN_VALUE)
         {
             return 0;
             
         }
            
         
        return (int)rev;
        
    }
}
