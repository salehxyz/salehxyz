We want to manage a movie collection:
- the movies will have a title, a genre (maybe more than one), year, the review, list of actors, a watch counter, borrowed (true or false), and borrower name.
- We can interact witht he movie by:
    - watching the movie (counter increases)
    - To write a review
    - set any of the fields (except flag, borrower, and counter, which are changed by different actions)
    - Borrowing the movie (set the borrower and update the status)
    - Retrun the movie (set the borrow to "" and update the status)
    - List the details of the movie

In addtion, the list of the actors needs to be stored seperately with name, date of birth, and nationality. and it can be updated.


```python
class Actors:
    def __init__(self,name,birth_date,nationality):
        self.name = name
        self.birth_date = birth_date
        self.nationality = nationality
    def actor_details(self):
        print(self.name, "  from:", self.nationality ,"  Born on:",self.birth_date)

```

Thought: If I only could make the adding actor part dynamic, so that I can run a function and add like 3 actors,
the issue is that I need to have a dynamic variable so that each actor data is added as A1, A2, A3,...
To do so I need to have a variable that has its second part as a variable so that it increases as need actors are added. Hummm...


```python
# global actor_i

# def add_actor():
#     global actor_i
#     global A
#     global B
#     global C
#     A = input("what is actor's name? ")
#     B = input ("What is actor birthday (MM/DD/YY)?")
#     C = input("What is actor nationality? ")
#     actor_i +=1
#     print("actor ID to use is:", actor_i)
#     print("Assign Actor Class to a variable names 'A' followed by ID as", actor_i)
    
```


```python
#add_actor()
```

The next part is the add the Movie Class:


```python
class Movie:
    genre = list()
    actors_list = list()

    def __init__(self, title, genre, year, review, actors_list, count_watched=0, borrowed=False, br_name=""):
        self.actors_list = actors_list
        self.review = review
        self.title = title
        self.genre = genre
        self.year = year

    def watch(self):
        self.count_watched +=1

    def borrow_movie(self,n):
        self.borrowed = True
        self.br_name = n

    def return_movie(self):
        self.borrowed = True
        self.br_name = ""

    def movie_details(self):
        print("Movie: ",self.title,"    Year:",self.year, "\n"
            "Genre: ",self.genre,"\n"
              "List of Actors:\n", end = "")
        for i in self.actors_list:
            print(i,"\n",end="")
        
```

Now lets add the actors:


```python
A1 = Actors("jaffar","10/21/55","India")
A2 = Actors("Gholi","11/22/68","Turkey")
A3 = Actors("Dina Smith","02/25/89","USA")
```


```python
A1.actor_details()
```

    jaffar   from: India   Born on: 10/21/55
    

Now lets add a movie:


```python
m1 = Movie("gone with the wind",["drama","comedy"],1985,"It was a nice movie",[A1.name,A2.name])
```


```python
m1.borrow_movie("James")
```


```python
print(m1.borrowed)
```

    True
    


```python
m1.movie_details()
```

    Movie:  gone with the wind     Year: 1985 
    Genre:  ['drama', 'comedy'] 
    List of Actors:
    jaffar 
    Gholi 
    
