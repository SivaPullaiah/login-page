class Assignment
{
	public static void main(String[] args)
	{
		// to add and assign a text  String value
		
		String txt = "Fantastic";
		String lang = "Java";
		txt += lang; //assign concatenated string --> txt = txt+lang;
		System.out.println("Add & Assign Strings:" + txt);
		
		// to add and assign an integers
		
		int sum = 10;
		int num = 20;
		sum += num; //assign result(10+20=30)--> sum = sum + num;
		System.out.println("Add & Assign integers:" + sum);
		
		// to multiply and assign an integer 
		
		int factor = 5;
		sum *= factor; //(30*5=150)-->sum = sum * factor;
		System.out.println("Multiplication sum:" + sum);
		
		// to divide and assign an integer
		
		sum/=factor; //(150 / 5 = 30) --> sum = sum / factor;
		System.out.println("Division sum:" + sum);
	}
}