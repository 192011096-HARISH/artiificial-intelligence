% Predicate to represent a person
person(FirstName, LastName, Age, Occupation).

% Facts to represent people
person("John", "Doe", 32, "Doctor").
person("Jane", "Doe", 27, "Engineer").
person("Jim", "Smith", 45, "Teacher").

% Clause to find a person by their first name and last name
find_person(FirstName, LastName, Age, Occupation) :-
    person(FirstName, LastName, Age, Occupation).
