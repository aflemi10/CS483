public class Entry{

	private int connections;
	private boolean visted;
	private String value;
	private Entry[] edges;

	Entry(String value){
		this.value = value;	
		this.connections = 0;
		this.visted = false;
		// limit the number of connections a node can have
		edges = new Entry[6];	
		for(int i = 0; i < 5; i++){
			edges[i] = null; 
		}	
	}

	void reset(){
		this.visted = false;
	}

	void discovered(){
		this.visted = true;
	}
	void addConnection(Entry e){
		String name = e.toString();
		for(int i = 0; i < connections; i++){
			String s = edges[i].toString();
			if(name.compareTo(s) == 0){
				return;
			}	
		}

		if(connections == 6){
			System.out.println("error object can at most have 5 connections");
			System.exit(0);
		}else{
			edges[connections] = e;
			connections++; 	
			return;
		}
	}
	void printConnections(){
		Entry temp = null;
		for(int i = 0; i < connections; i++){
			temp = edges[i];
			String edgeValue = temp.toString();
			System.out.print(edgeValue + " ");
		}
		System.out.println();
	}

	@Override 
	public String toString(){
		return value;
	}
}
