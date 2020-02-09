import java.util.*;
import java.io.*;

public class Driver{
	public static void main(String[] args)
						throws FileNotFoundException{
		File file = new File("./Data/graph.txt");
		Scanner sc = new Scanner(file);

		HashTable ht = new HashTable(15);
		makeData(sc,ht);
		ht.findConnections("13");
						
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
