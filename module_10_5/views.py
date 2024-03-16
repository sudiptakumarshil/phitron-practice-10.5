from django.shortcuts import render


def index(request):
    return render(request, "index.html", {
        'data': [
            {
                "name": "Alice",
                "age": 25,
                "city": "Los Angeles",
                "email": "alice@example.com",
                "occupation": "Software Engineer",
                "salary": 80000,
                "birth_date": "1999-05-15",
                "friends": [1, 2, 3]
            },
            {
                "name": "Bob",
                "age": 35,
                "city": "San Francisco",
                "email": "bob@example.com",
                "occupation": "Data Scientist",
                "salary": 90000,
                "birth_date": "1999-05-15",
                "friends": [4,5,6]
            },
            {
                "name": "Charlie",
                "age": 28,
                "city": "Seattle",
                "email": "charlie@example.com",
                "occupation": "Graphic Designer",
                "salary": 60000,
                "birth_date": "1999-05-15",
                "friends": [7,8,9]
            }
        ]
    })
