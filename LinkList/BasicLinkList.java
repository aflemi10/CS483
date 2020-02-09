import java.util.*;
import java.io.*;

public class BasicLinkList{
  public static void main(String[] args)
								throws FileNotFoundException{
			
	String fileName = "./Data/nodes.txt";	
	File file = new File(fileName);
	Scanner input = new Scanner(file);
	Node n = new Node(12);	
	createList(n,input);
	print(n);

  }
	public static void createList(Node head, Scanner s){
		String value;
		Node current = head;	

		while(s.hasNext()){
			value = s.next();	
			Node n = new Node(Integer.parseInt(value));
			current.next = n;
			current = current.next;
		}
	}
	public static void print(Node n){
		if(n == null) return;	
		echo(n.toString());	

		while(n.next != null){
			n = n.next;
			echo(n.toString());
		}
		newLine();	
	}
	
	public static void newLine(){
		System.out.println("");
	}
	public static void echo(String s){
		System.out.print(s + " ");
	}
}
