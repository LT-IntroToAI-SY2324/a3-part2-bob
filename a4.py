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

if __name__ == "__main__":
    assert isinstance(schools_by_year(["1746"]), list), "schools_by_year not returning a list"
    assert isinstance(schools_by_year_range(["1770", "1850"]), list), "schools_by_year_range not returning a list"
    assert isinstance(schools_before_year(["1800"]), list), "schools_before_year not returning a list"
    assert isinstance(schools_after_year(["1700"]), list), "schools_after_year not returning a list"
    assert isinstance(schools_by_rate_higher(["20.5"]), list), "schools_by_rate_higher not returning a list"
    assert isinstance(schools_by_rate_lower(["73.4"]), list), "schools_by_rate_lower not returning a list"
    assert isinstance(schools_by_rate_range(["4", "60.7"]), list), "schools_by_rate_range not returning a list"
    assert isinstance(schools_by_size_bigger(["20,000"]), list), "schools_by_size_bigger not returning a list"
    assert isinstance(schools_by_size_smaller(["30,000"]), list), "schools_by_size_smaller not returning a list"
    assert isinstance(schools_by_size_range(["10,000", "17,000"]), list), "schools_by_size_range not returning a list"
    assert isinstance(schools_by_location([ "Norman, Oklahoma, USA"]), list), "schools_by_location not returning a list"
#School name
    #location
    #year founded
    # undergrad class size
    # acceptance rate
