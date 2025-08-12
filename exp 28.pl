% --- Facts: student_teacher(Student, Teacher, SubjectCode) ---

student_teacher('Alice', 'Mr. Smith', 'CS101').
student_teacher('Bob', 'Mrs. Johnson', 'MA102').
student_teacher('Charlie', 'Mr. Smith', 'CS101').
student_teacher('David', 'Mr. Lee', 'PH103').
student_teacher('Emma', 'Mrs. Johnson', 'MA102').

% --- Rules to retrieve information ---

% Find teacher for a given student
find_teacher(Student, Teacher) :-
    student_teacher(Student, Teacher, _).

% Find subject code for a given student
find_subject_code(Student, SubjectCode) :-
    student_teacher(Student, _, SubjectCode).

% Find students taught by a particular teacher
find_students_by_teacher(Teacher, Student) :-
    student_teacher(Student, Teacher, _).

% Find students by subject code
find_students_by_subject(SubjectCode, Student) :-
    student_teacher(Student, _, SubjectCode).
