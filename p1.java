public class p1{
    public static void main(String[] args) {
        A(500);
        
    }
    public static void A( int n){
        if(n<=1){
            System.out.print(n+"    ");
        }
        else{
            A(n/2);
            System.out.print(n%2+"    ");
        }
    }
}