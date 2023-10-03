struct Node {
    val: T,
    next: Option<Box<Node<T>>>,
}

pub struct Queue<T> {
    end: Option<Node<T>>,
}

impl<T> Queue<T> {
    pub fn is_empty(&self) -> bool {
        match self.end {
            None => true,
            _ => false,
        }
    }
}
impl<T> Queue<T> {
    pub fn add(&mut self, val: T) {
        let new_node = Node::new(val);
    }
}
