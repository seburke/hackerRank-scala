import java.util.ArrayList;
import java.util.List;

public class checkValidBST {

	class Node {
		int data;
		Node left;
		Node right;
	}


	List<Integer> getBSTList(Node node, List<Integer> values) {
		if (node.left != null) {
			getBSTList(node.left, values);
		}
		values.add(node.data);
		if (node.right != null) {
			getBSTList(node.right, values);
		}
		return values;
	}

	boolean checkValid(List<Integer> values) {
		int prev = Integer.MIN_VALUE;
		for (int x: values) {
			if (x <= prev) return false;
			prev = x;
		}
		return true;
	}


	boolean checkBST(Node root) {

		List<Integer> v = getBSTList(root, new ArrayList<Integer>());
		return checkValid(v);

	}




}
