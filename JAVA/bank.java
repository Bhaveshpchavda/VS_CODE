import java.util.*;

public class bank

{
    String c_name;
    int c_id;
    
    static int acc_balance = 40000000;
    static String bank_name = "SBI";
}

public class main
{
	public static void main(String[] args) {
	Scanner sc = new Scanner(System.in);
	bank obj = new bank();
	
	System.out.print("Enter the name of the customer :");
	String a = sc.nextLine();
	
	System.out.print("Enter the ID of the customer :");
	int b = sc.nextInt();
	
	System.out.println("                                ");
	System.out.println("                                ");
	
	System.out.println("           Bank Details         ");
	System.out.println("                                ");
	System.out.println("                                ");
	System.out.println("                                ");
	
	System.out.println("The name of the customer is :" +a);
	System.out.println(a + " has account in "+ obj.bank_name);
	System.out.println(a + " bank account balance is :"+ obj.acc_balance);
	System.out.println(a + " bank ID is: "+ b);
	
		
		
	}
}