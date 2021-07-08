class Arithmetic
{
	public static void main(String[] args)
	{
		int num = 100;
		int factor = 20;
		int sum = 0;
		
		sum = num + factor; // 100 + 20 = 120
		System.out.println("Addition sum:" + sum);
		
		sum = num - factor; // 100 - 20 = 80
		System.out.println("Subtraction sum:" + sum);
		
		sum = num * factor; // 100 * 20 = 2000
		System.out.println("Multiplicatiom sum:" + sum);
		
		sum = num / factor; // 100 / 20 = 5
		System.out.println("Division sum:" + sum);
		
		sum = num % factor; // 100 % 20 = 0
		System.out.println("Modulo division sum:" + sum);
	}
}