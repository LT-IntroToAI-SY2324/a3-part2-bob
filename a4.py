from schools import school_db
from match import match
from typing import List, Tuple, Callable, Any

def get_name(school: Tuple[str, str, int, int]) -> str:
    return school[0]
def get_location(school: Tuple[str, str, int, int]) -> str:
    return school[1]
def get_year(school: Tuple[str, str, int, int]) -> int:
    return school[2]
def get_size(school: Tuple[str, str, int, int]) -> int:
    return school[3]
def get_rate(school: Tuple[str, str, int, int]) -> int:
    return school[4]

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
    return results

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

def schools_by_size_smaller(matches: List[str]) -> List[str]:
    to_return = []
    #Iterates through School_db where School is one Schools worth of data
    for school in school_db:
        #If the size of the school is less than the first element in matches
        if (get_size(school) < int(matches[0])):
            to_return.append(get_name(school))
    return to_return
    
def schools_by_size_range(matches: List[str]) -> List[str]:
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

def schools_by_location(matches: List[str]) -> List[str]:
    to_return = []
    #Iterates through School_db where School is one Schools worth of data
    for school in school_db:
        #If the location of the school is the same as element 1 of matches
        if (get_location(school) == matches[0]):
            to_return.append(get_name(school))
        return to_return


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


    (str.split("where is %"), location_by_school),
    (str.split("what schools are in %"), schools_by_location),

]

def search_pa_list(src: List[str]) -> List[str]:
    """Takes source, finds matching pattern and calls corresponding action. If it finds
    a match but has no answers it returns ["No answers"]. If it finds no match it
    returns ["I don't understand"].

    Args:
        source - a phrase represented as a list of words (strings)

    Returns:
        a list of answers. Will be ["I don't understand"] if it finds no matches and
        ["No answers"] if it finds a match but no answers
    """
    for pat, act in pa_list:
        mat=match(pat,src)
        if mat is not None: 
            answer=act(mat)
            return answer if answer else["No answers"]
        return["I don't understand"]


def query_loop() -> None:
    """The simple query loop. The try/except structure is to catch Ctrl-C or Ctrl-D
    characters and exit gracefully.
    """
    print("Welcome to the school database!\n")
    while True:
        try:
            print()
            query = input("Your query? ").replace("?", "").lower().split()
            answers = search_pa_list(query)
            for ans in answers:
                print(ans)

        except (KeyboardInterrupt, EOFError):
            break

    print("\nSo long!\n")


if __name__ == "__main__":
    assert isinstance(schools_by_year(["1746"]), list), "schools_by_year not returning a list"
    assert isinstance(schools_by_year_range(["1770", "1850"]), list), "schools_by_year_range not returning a list"
    assert isinstance(schools_before_year(["1800"]), list), "schools_before_year not returning a list"
    assert isinstance(schools_after_year(["1900"]), list), "schools_after_year not returning a list"
    assert isinstance(schools_by_rate_higher(["20.5"]), list), "schools_by_rate_higher not returning a list"
    assert isinstance(schools_by_rate_lower(["10"]), list), "schools_by_rate_lower not returning a list"
    assert isinstance(schools_by_rate_range(["10", "12"]), list), "schools_by_rate_range not returning a list" #megan
    assert isinstance(schools_by_size_bigger(["40000"]), list), "schools_by_size_bigger not returning a list"
    assert isinstance(schools_by_size_smaller(["5000"]), list), "schools_by_size_smaller not returning a list"
    assert isinstance(schools_by_size_range(["5000", "6000"]), list), "schools_by_size_range not returning a list"
    assert isinstance(schools_by_location([ "Norman, Oklahoma, USA"]), list), "schools_by_location not returning a list"
    
    assert sorted (search_pa_list(["what", "schools", "have", "acceptance", "rates", "between", "10", "and","12"])) == sorted(
        [ "Cornell University", "University of California, Berkely"]
    ), "failed search_pa_list test 7"
    assert sorted (search_pa_list(["what", "schools", "have", "class", "sizes", "bigger", "than", "40000"])) == sorted(
        [ "University of California, Los Angeles (UCLA)"]
    ), "failed search_pa_list test 8"
     assert sorted (search_pa_list(["what", "schools", "have", "class", "sizes", "smaller", "than", "_"])) == sorted(
        ["Massachusetts Institute of Technology (MIT)"]
    ), "failed search_pa_list test 9"
     assert sorted (search_pa_list(["what", "schools", "have", "class", "sizes", "between", "_", "and", "_"])) == sorted(
        [ "Yale University", "Princeton University"]
    ), "failed search_pa_list test 10"
     assert sorted (search_pa_list(["what", "schools", "are", "in", "%"])) == sorted(
        [ "University of Oklahoma"]
    ), "failed search_pa_list test 11"
    

#School name
    #location
    #year founded
    # undergrad class size
    # acceptance rate
