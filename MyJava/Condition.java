class Condition
{
	public static void main(String[] args)
	{
		int num1 = 22;
		int num2 = 27;
		String result;
		
		result = (num1 % 2 == 0) ? "odd" : "even";
		System.out.println(num1 + "is" + result);
		
		result = (num2 % 2 == 0) ? "odd" : "even";
		System.out.println(num2 + "is" + result);
	}
}