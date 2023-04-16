# AnswerMe
## Submission for AI60008, Spring 2023, IIT Kharagpur.
Topic - Question Answering on Knowledge Graph

![image](https://user-images.githubusercontent.com/62075225/232343813-877fc16e-96d8-4875-982b-dbb08bf60548.png)

![image](https://user-images.githubusercontent.com/62075225/232343934-f035de0a-5cd8-4009-8881-3fe448d21e0a.png)

![image](https://user-images.githubusercontent.com/62075225/232344057-f9c40363-6d26-4363-b839-2bad4ff69ab5.png)

![image](https://user-images.githubusercontent.com/62075225/232343984-fc9ec8b2-952c-40f4-8f95-fc5172c66a77.png)

![image](https://user-images.githubusercontent.com/62075225/232343999-8dea616f-d27a-46e3-b05b-0fd4c3d1ab5b.png)


About AnswerMe
==============

The underlying principle behind **AnswerMe** is [**Entity Extraction**](https://sematext.com/blog/entity-extraction-with-spacy/), for which it uses **spaCy**.

The process of entity extraction involves the identification of the subject, predicate, and object from a given text. This is typically done using dependency parsing tools and methods.

One practical application of entity extraction is in question-answering systems, where the entities are used to extract answers from user queries.

The rudimentary approach that we have followed in AnswerMe is particularly effective for questions that start with words like 'who', 'what', 'when', and 'where'. To extract answers, the system matches common entities from the question with the context, constructs a knowledge graph which are used to answer the questions inputted by the user. However, it should be noted that the answers obtained using AnswerMe are currently limited to simple responses consisting of only a few words.

##### More on "Question Answering on Knowledge Graphs" -

[Introduction to Question Answering over Knowledge Graphs](https://yashuseth.wordpress.com/2019/10/08/introduction-question-answering-knowledge-graphs-kgqa/)

[Querying using simple knowledge graphs](https://medium.com/analytics-vidhya/querying-using-simple-knowledge-graphs-abeb13d05e48#:~:text=In%20simple%20words%2C%20a%20knowledge,what%20is%20a%20verb%2C%20etc.)

[Understanding Semantic Search — (Part 3: Introduction to Knowledge Graphs for Question Answering)](https://medium.com/analytics-vidhya/open-domain-question-answering-series-part-3-introduction-to-knowledge-graphs-for-question-5d3f8d78812e)

