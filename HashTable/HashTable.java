import java.util.*;
import java.io.*;

/*
Simple hashtable to store an array of objects
	implements seperate chaining 
	contains hash function
	insert method
	
Node
	contains - next poninter to node
	contains - entry will hold some string
*/

public class HashTable{

	private int size;
	private Object[] obj;
	private int elements;

	// at most 15 elements
	HashTable(){
		this(15);
	}

	// create a sized list of elements
	HashTable(int size){
		this.size = size;
		obj = new Object[size];
		elements = 0;
	}	
	// find index for string	
	int hashFunction(String s){
		int length = s.length();
		int sum = 0;
		for(int i = 0; i < length; i++){
			sum += s.charAt(i);
		}
		return (sum % size);
	}	
	// find index for int	
	int hashFunction(int i){
		return (i % (size + 1));
	}
	// called when list index is not null
	// find the node with "value" if found return 0
	int search(int index, String value){
		String nodeString;
		Node n = (Node)(obj[index]); 
		while( n != null){
			nodeString = n.getData();
			if(value.compareTo(nodeString) == 0){
				return 0; 
			}
			n = n.next;
		}
		return 1;
	}
	//does  search call to see if found in node
	boolean found(int index, String value){
				
		if(search(index,value) == 1){
			return false;
		}	
			return true;
	}

	// adds entry
	// checks to see if in list if so adds
	// if found does nothing
	void add(String string){
		Entry e = new Entry(string);
		String key = e.toString();
		int index = hashFunction(key);
		//if index at table is empty
		if(obj[index] == null){
			Node create = new Node(e);
			obj[index] = create; 
			return;
		}
		// get value in e
		String value = e.toString();
		//if found dont do anything
		if(found(index,value)){
			return;
		}else{
			// create node to insert e
			Node n = new Node(e);
			Node prev = null;
			Node tempNode = (Node)(obj[index]);
			// go to last node
			while(tempNode != null){
				prev = tempNode;
				tempNode = tempNode.next;
			}	
			// add to the end of the list
			prev.next = n;
			return;
		}
	}

	void connect(String u, String v){

		int key1 = hashFunction(u);
		int key2 = hashFunction(v);	

		Entry foundU = null;
		Entry foundV = null;

		//locate v
System.out.println("__________________________");
		Node n = (Node)(obj[key2]); 
		String nodeString = n.getData();
		// find v to save into u
		while(v.compareTo(nodeString) != 0){
System.out.println("__________________________");
			n = n.next;
			nodeString = n.getData();
		}
		// add v to u
		foundV = n.data;
		
		// locate u
		n = (Node)(obj[key1]);
		nodeString = n.getData();
		// find u to save into v
		while(u.compareTo(nodeString) != 0){
			n = n.next;
			nodeString = n.getData();
		}
		// add v to u
		foundU = n.data;

		foundU.addConnection(foundV);

		foundV.addConnection(foundU);
		return;
	}

	void findConnections(String s){
		int key = hashFunction(s);
		Entry foundX = null;
		//locate x
		Node n = (Node)(obj[key]); 
		String nodeString = n.getData();
		// find x 
		while(s.compareTo(nodeString) != 0){
			n = n.next;
			nodeString = n.getData();
		}
		//found 
		foundX = n.data;
		foundX.printConnections();
	}

	class Node{
		private Node next;
		private Entry data;

		Node(Entry data){
			this.data = data;	
			next = null;
		}
		
		// overrided in entry class
		String getData(){
			return data.toString();
		}	
	}
}
