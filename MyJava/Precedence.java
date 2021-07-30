class Precedence
{
	public static void main(String[] args)
	{
		int sum = 32 - 8 + 16 * 2;
		System.out.println("Default order:" + sum);
		
		sum = (32-8+16)*2;
		System.out.println("Specified order:" + sum);
		
		sum = (32-(8+16))*2;
		System.out.println("Nested specific order:" + sum);
	}
}