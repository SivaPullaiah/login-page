class Camparison
{
	public static void main(String[] args)
	{
		// to compare two text String values for equality(==)
		String txt = "Fantastic";
		String lang = "Java";
		boolean state = (txt == lang); //assign test result
		System.out.println("String equality test:" + state);
		
		// to compare for inequality(!=)
		state = (txt != lang); // assign result
		System.out.println("String inequality test:" + state);
		
		// to compare two integer values
		int dozen = 12;
		int score = 20;
		state = (dozen > score); // assign result
		System.out.println("Greater than test:" + state);
		
		// to compare the integers once more
		state = (dozen < score); // assign result
		System.out.println("Less than test:" + state);
	}
}