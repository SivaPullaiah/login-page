/* A program to demonstrate constant variables */

class Constants
{
	public static void main(String[] args)
	{
		// Constant score values
		final int TOUCHDOWN = 6;
		final int CONVERSION = 1;
		final int FIELDGOAL = 3;
		
		// Calculate points scored
		int tg, pat, fg, total;
		
		tg = 4 * TOUCHDOWN;        // 4*6=24
		pat = 3 * CONVERSION;      // 3*1=3
		fg = 2 * FIELDGOAL;        // 2*3=6
		total = (tg + pat + fg);   // 24+3+6=33
		
		// Output calculated total
		System.out.println("Score:" + total);
	}
}