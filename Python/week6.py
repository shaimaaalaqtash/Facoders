

grade_one= {'Sami': [19, 18, 19.5, 30, 10], 'Ahmad': [15, 14, 16, 21, 7], 'Faris': [18, 19, 17, 26, 9], 'Salem': [20, 20, 19, 30, 10], 'Mahmoud': [12, 13, 11, 18, 7]}

grade_two= {'Lana': [17, 19, 20, 28, 9], 'Dina': [18.5, 19.5, 20, 29, 10], 'Maha': [20, 20, 18, 26, 9], 'Abeer': [16, 18, 19.5, 25, 8]}

grade_three= {'Rima': [18, 19, 18, 26, 9], 'Tala': [20, 20, 19, 29, 10], 'Lamar': [19, 20, 18, 26, 9], 'Rola': [15, 14, 16, 19, 7], 'Naya': [9, 6, 11, 14, 7], 'Dalal': [1, 5, 2, 6, 7], 'Ola': [19.5, 20, 20, 29.5, 10]}

def students_names(room):
    names_list= list(room.keys())
    return names_list

def student_score(room, name):
    if name in room:
         markes=room.get(name)
         scores=sum(markes)
    return scores

def student_count(room):
    count=len(room)
    return count

while True:

    ch=input("Choose one: students_names, student_score, students_count")

    if ch=='students_names':
        room=input('Enter grade:')
        print(students_names(room))

    elif ch=='student_score':
        name,room =input('Enter name:'),input('Enter grade:')
        print(student_score(room, name))

    elif ch=='students_count':
        room =input('Enter grade:')
        print(student_count(room))

    a=input('done or more:')
    if a=='done':
        break
    elif a=='more':
        continue
