import java.util.*;
import java.io.*;

public class Driver{
	public static void main(String[] args)
						throws FileNotFoundException{
		printData();
		File file = new File("./Data/graph.txt");
		Scanner sc = new Scanner(file);

		HashTable ht = new HashTable();
		makeData(sc,ht);
		
		System.out.println("FIND direct nodes of 13");
		// need node connections
		ht.findConnections("13");
						
	}
	public static void printData() throws FileNotFoundException{
		File file = new File("./Data/graph.txt");
		Scanner sc = new Scanner(file);
		System.out.println();
		System.out.println();
		System.out.println("Data: ");
		while(sc.hasNextLine()){
			String line = sc.nextLine();
			System.out.println(line);
		}
		System.out.println("***********************");
		System.out.println();
		System.out.println();
	}
	public static void makeData(Scanner s, HashTable ht){
		while(s.hasNextLine()){
			String line = s.nextLine();
			
			Scanner lineScanner = new Scanner(line);
			String u = lineScanner.next();
			ht.add(u);
			
			//System.out.println("_________X: " + u);

			while(lineScanner.hasNext()){
				String part = lineScanner.next();
				ht.add(part);
				//System.out.println(part);
				ht.connect(u,part);	
			}
		}
	}
}
