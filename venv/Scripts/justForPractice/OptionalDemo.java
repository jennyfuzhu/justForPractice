package justForPractice;

import static org.junit.Assert.assertTrue;

import java.util.Optional;

import org.junit.jupiter.api.Test;

public class OptionalDemo {
	
	public void main(String[] args) {
		
		Optional<String> opt1 = Optional.of("This is a sample text");
		
		Optional<String> opt2  = Optional.empty();
		
		String name = "Carina";
		Optional<String> opt = Optional.of(name);
		
		
		if(opt1.isPresent()) {
			System.out.println("Optional one is present");
		}else {
			System.out.println("Optional one is not present");
		}
		
		opt1.ifPresent(s -> System.out.println("ifPresent method called op1"));
		opt2.ifPresent(s -> System.out.println("optional 2 is present, otherwise this "
				+ "line would not be printed out"));
	}
	@Test
	public void test_opt(String s) {
		Optional opti = Optional.of(s);
		if(opti.isPresent()) {
			System.out.println("opti is not empty");
		}else {
			System.out.println("Opti is empty");
		}
	}

}
