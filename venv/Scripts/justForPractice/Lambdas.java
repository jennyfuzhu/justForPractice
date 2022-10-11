package justForPractice;

public class Lambdas {
	
	public void main(String[] args) {
		Message messageThing = new Message() {

			@Override
			public void message() {
				// TODO Auto-generated method stub
				System.out.println("Hello");	
			}
			// anonymous inner class
		};
		messageThing.message();
		Message message = () -> System.out.println("Hello");
		Printable lambdaPrintable = (s) -> "Meow " + s;
		//myCat.printOut();
		message.message();
		Message message2 = () -> {
		System.out.println("hello");	
		};
		message2.message();
		printThing(lambdaPrintable);
	}

	static void printThing(Printable thing) {
		thing.printOut("!");
	}
}

