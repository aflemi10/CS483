public class Node{

	private int value;
	public Node next;

	Node(){
		this(0);
	}

	Node(int value){
		this.value = value;
		next = null;
	}

	public void setNext(Node n){
		this.next = n;	
	}

	@Override
	public String toString(){
		return value + "";
	}
}
