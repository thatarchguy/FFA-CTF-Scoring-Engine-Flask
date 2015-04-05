## Free-For-All CTF Scoring Engine
I wrote this as an example for a friend to learn flask. 

Converted from an old php webapp I wrote when I learned php.
-----
### Purpose
----
In online capture the flag competitions you usually register a user, go to a jeopardy style question panel, and submit the flag/answer.

I wanted an engine that has no question base, just machines/apps ridden with flags that can all be submitted through one form. 
Like the root pass would be a flag, portknocking would reveal a flag, etc...

So it would just be a "Free-For-All"

That's where this scoring engine comes into play.

### Setup
----

```
pip install -r requirements.txt
python manage.py createdb
python manage.py runserver -h 0.0.0.0:80
```


Adding flags is a manual task for now:
```
python manage.py shell
flag = models.Flags(flag="flag-ABDCF22", points=20)
db.session.add(flag)
db.session.commit()
```
