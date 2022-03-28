/* -------------------------------------------------------------
* Author:  Andrew Zeiser
* Program: Program2
*
* Description: 
* This Program functions like a calculator. If you create a test 
* driver you will be able solve any simple arithmetic question. 
* -------------------------------------------------------------
*/
public class Calculator {
	
	private double total=0;
	
	
	// Creating the constructors
	
	public Calculator() {
		this(0.0);
	}
	
	public Calculator(double inNumber) {
		
		
		
		total = inNumber;
		
	}
	
	
	// creating the Add Subtract multiply and divide method
	
	public double add(double inNumber) {
		
		total += inNumber;
		
		return total;
	}

	
	public double subtract(double inNumber) {

		total-=inNumber;
		return total;
	
	}
		
	public double multiply(double inNumber) {
		total*=inNumber;
		return total;
	}
	
	public double divide(double inNumber) {
		total/=inNumber;
		return total;
		
	}
	
	// creating the resetFirstNumber method
	
	public void resetFirstNumber(double inNumber) {
		total=inNumber;
		
	}
	
	public void resetFirstNumber() {
		total=0.0;
		
	}
	
	
	
}
