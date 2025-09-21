# Day 1: Blog System Interview Q&A

## Interview Pattern for System Design
1. **Clarify Requirements**: "What features does the blog need?"
2. **Scale Estimation**: "How many users and posts?"  
3. **High-level Design**: Draw basic architecture
4. **Deep Dive**: Focus on database schema and APIs
5. **Scale & Optimize**: Discuss bottlenecks and solutions
6. **Wrap Up**: Monitoring, security, future improvements

## Practice Questions

### Question 1: Basic Architecture
**"Design a personal blog system for 10,000 users"**

**Sample Answer Structure:**
- **Functional Requirements**: Users, posts, comments, authentication
- **Simple Architecture**: Web Server → Database → File Storage  
- **Database Schema**: Users, Posts, Comments tables with relationships
- **APIs**: CRUD operations for posts, user management
- **Technology**: Node.js/Python + PostgreSQL + simple file storage

### Question 2: Scaling Challenges  
**"Your blog now has 100,000 daily readers. What bottlenecks do you expect?"**

**Sample Answer:**
- **Database reads** become slow (lots of people reading posts)
- **Single web server** can't handle traffic
- **Image loading** slows down page performance
- **Solutions**: Read replicas, load balancer, CDN for images

### Question 3: Database Design
**"Design the database schema for blog posts with categories and tags"**

**Sample Answer:**
```
posts (id, user_id, title, content, category_id, created_at)
categories (id, name, description)
tags (id, name)
post_tags (post_id, tag_id) -- many-to-many relationship
```


### Question 4: Read-Heavy System
**"How would you optimize a blog for reading performance?"**

**Sample Answer:**
- **Database**: Add read replicas, index on frequently queried columns
- **Caching**: Redis for popular posts, browser caching for static content
- **CDN**: Serve images from geographically distributed servers
- **Pagination**: Don't load all posts at once

### Question 5: Consistency vs Availability
**"Should a blog prioritize consistency or availability? Why?"**

**Sample Answer:**
- **Choose Availability** - Users prefer seeing slightly old content over error pages
- **Eventual Consistency** works for blogs - new posts can take a few seconds to appear everywhere
- **Exception**: Admin actions (delete post) might need stronger consistency

## 60-Second Drill Responses

**"Explain horizontal vs vertical scaling with blog example"**
- **Vertical**: Upgrade to bigger server when traffic grows
- **Horizontal**: Add more web servers behind load balancer  
- **Blog example**: Start with one server, add servers as readership grows

**"Why are blogs read-heavy systems?"**
- **90% reads**: People browsing and reading posts
- **10% writes**: Authors creating new posts, readers commenting
- **Optimization**: Focus on fast reading, read replicas

**"How do you handle user uploads in distributed system?"**
- **Option 1**: Shared file storage (NFS) - simple but single point of failure
- **Option 2**: Object storage (S3) - scalable, distributed
- **Option 3**: CDN integration - fast global access

## Common Mistakes to Avoid
❌ **Over-engineering**: Don't start with microservices for a blog
❌ **Wrong database choice**: Don't use NoSQL unless you need it  
❌ **Ignoring read patterns**: Forgetting blogs are read-heavy
❌ **No caching strategy**: Missing obvious performance wins
✅ **Start simple**: Single server → Load balanced → Cached → Distributed

## Day 1 Success Criteria
- [ ] Can explain 3-tier web architecture
- [ ] Can design basic blog database schema  
- [ ] Can identify read vs write patterns
- [ ] Can propose simple scaling solutions
- [ ] Can discuss trade-offs between consistency and availability
