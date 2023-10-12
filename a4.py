<<<<<<< HEAD
from schools import schools_db
=======
from schools import school_db
>>>>>>> 393df6640acbd5f2ef3265464cda560f8eecb20e
from match import match
from typing import List, Tuple, Callable, Any

def get_name(school: Tuple[str, str, int, int]) -> str:
    return school[0]
<<<<<<< HEAD
def get_location(movie: Tuple[str, str, int, int]) -> str:
    return school[1]
def get_year(movie: Tuple[str, str, int, int]) -> int:
    return school[2]
def get_size(movie: Tuple[str, str, int, int]) -> int:
    return school[3]
def get_rate(movie: Tuple[str, str, int, int]) -> int:
    return school[4]
=======
def get_location(school: Tuple[str, str, int, int]) -> str:
    return school[1]
def get_year(school: Tuple[str, str, int, int]) -> int:
    return school[2]
def get_size(school: Tuple[str, str, int, int]) -> int:
    return school[3]
def get_rate(school: Tuple[str, str, int, int]) -> int:
    return school[4]

>>>>>>> 393df6640acbd5f2ef3265464cda560f8eecb20e
def schools_by_year(matches: List[str]) -> List[str]:
    results = []
    for school in school_db:
        if int(matches[0]) == get_year(school):
            results.append(get_name(school))
            return results
def schools_by_year_range(matches: List[str]) -> List[str]:
    results = []
    for school in school_db:
        if int(matches[0]) <= get_year(school):
            results.append(get_name(school))
            return results
def schools_before_year(matches: List[str]) -> List[str]:
    results = []
    for school in school_db:
        if get_year(school)< int(matches[0]):
            results.append(get_name(school))
            return results
def schools_after_year(matches: List[str]) -> List[str]:
    results = []
    for school in school_db:
        if get_year(school)< int(matches[0]):
            results.append(get_name(school))
            return results
<<<<<<< HEAD


def schools_by_rate_higher(matches: List[str]) -> List[str]:
    results=[]
    for school in school_db:
        if get_rate(school)>int(matches[0]):
            results.append(get_name(school))
    return results
def schools_by_rate_lower(matches: List[str]) -> List[str]:
    results=[]
    for school in school_db:
        if get_rate(school)<int(matches[0]):
            results.append(get_name(school))
def schools_by_rate_range(matches: List[str]) -> List[str]:
    results=[]
    for school in school_db:
        if int(matches[0])<= get_rate(school)<=int(matches[1]):
            results.append(get_name(school))
    return results
def schools_by_size_bigger(matches: List[str]) -> List[str]: 
    results=[]
    for school in school_db:
        if get_size(school)>int(matches[0]):
            results.append(get_name(school))
    return results




=======
def schools_by_rate_higher(matches: List[str]) -> List[str]:
def schools_by_rate_lower(matches: List[str]) -> List[str]:
def schools_by_rate_range(matches: List[str]) -> List[str]:
def schools_by_size_bigger(matches: List[str]) -> List[str]:
def schools_by_size_smaller(matches: List[str]) -> List[str]: #Ewan
    to_return = []
    #Iterates through School_db where School is one Schools worth of data
    for school in school_db:
        #If the size of the school is less than the first element in matches
        if (get_size(school) < int(matches[0])):
            to_return.append(get_name(school))
    return to_return
def schools_by_size_range(matches: List[str]) -> List[str]: #Ewan
    #Includes boths bounds
    to_return = []
    # orders matches from smallest to largest
    if (matches[0] > matches[1]):
        place_holder = matches[0]
        matches[0] = matches[1]
        matches[1] = place_holder
    #Iterates through School_db where School is one Schools worth of data
    for school in school_db:
        #If the size of the school is greater than or equal to the first element in matches and less than or equal to the second element of matches
        if (get_size(school) >= matches[0] and get_size(school) <= matches[1]):
            to_return.append(get_name(school))
    return to_return
def schools_by_location(matches: List[str]) -> List[str]: #Ewan
    to_retrun = []
    #Iterates through School_db where School is one Schools worth of data
    for school in school_db:
        #If the location of the school is the same as element 1 of matches
        if (get_location(school) == matches[0]):
            to_return.append(get_name(school))
    return to_retrun
>>>>>>> 393df6640acbd5f2ef3265464cda560f8eecb20e


pa_list: List[Tuple[List[str], Callable[[List[str]], List[Any]]]] = [
    (str.split("what schools were founded in _"), schools_by_year),
    (str.split("what schools were founded between _ and _"), schools_by_year_range),
    (str.split("what shools were founded before _"), schools_before_year),
    (str.split("what schools were founded after _"), schools_after_year),
    (str.split("what schools have acceptance rates higher than _"), schools_by_rate_higher),
    (str.split("what schools have acceptance rates lower than _"), schools_by_rate_lower),
    (str.split("what schools have acceptance rates between _ and _"), schools_by_rate_range),
    (str.split("what schools have class sizes bigger than _"), schools_by_size_bigger),
    (str.split("what schools have class sizes smaller than _"), schools_by_size_smaller),
    (str.split("what schools have class sizes between _ and _"), schools_by_size_range),



    (str.split("what schools are in %"), schools_by_location),
<<<<<<< HEAD
    
    

=======
>>>>>>> 393df6640acbd5f2ef3265464cda560f8eecb20e

]

#School name
    #location
    #year founded
    # undergrad class size
    # acceptance rate
