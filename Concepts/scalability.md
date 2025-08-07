# Scalability Fundamentals

## 1. What is Scalability?
A system is **scalable** if it can handle increased load by adding resources rather than rewriting the code.

- **Vertical Scaling** (scale up): Increase CPU, RAM of one node  
  - Pros: Simple to implement  
  - Cons: Hardware limit; often requires downtime  
- **Horizontal Scaling** (scale out): Add more nodes to the cluster  
  - Pros: Practically limitless capacity; no downtime  
  - Cons: More complex (data distribution, coordination)  
- **Diagonal Scaling**: Start vertical, then add nodes when needed

### Beginner Tip
_Read one sentence at a time, then restate in your own words. Draw a quick sketch: one big server vs. many small servers._

## 2. Load Balancing Concepts
A **load balancer** distributes incoming traffic across multiple servers.

- **Round Robin**: Cycles requests evenly  
- **Weighted Round Robin**: Honors server capacity weights  
- **Least Connections**: Sends traffic to the least-busy server  

### Beginner Tip
_Imagine donkeys taking turns carrying baskets (Round Robin) vs. sending baskets to the donkey with the fewest baskets (Least Connections)._

## 3. CAP Theorem vs. ACID
- **CAP Theorem** (distributed systems)  
  - Guarantee any two:  
    - **Consistency**: All nodes read the same data  
    - **Availability**: Every request gets a response  
    - **Partition Tolerance**: Continues despite network failures  
- **ACID** (single-database transactions)  
  - **Atomicity**, **Consistency**, **Isolation**, **Durability** ensure each transaction leaves data valid

### Beginner Tip
_Think CAP is about networked databases; ACID is about one database’s transaction integrity._

## Self-Check Questions
1. When would you start vertical and pivot to horizontal scaling?  
2. Why can’t you have a strictly CA system in practice?  
3. Which load-balancing algorithm suits WebSocket-heavy chat traffic?
