def schools_by_year(matches: List[str]) -> List[str]:
def schools_by_year_range(matches: List[str]) -> List[str]:
def schools_before_year(matches: List[str]) -> List[str]:
def schools_after_year(matches: List[str]) -> List[str]:
def schools_by_rate_higher(matches: List[str]) -> List[str]:
def schools_by_rate_lower(matches: List[str]) -> List[str]:
def schools_by_rate_range(matches: List[str]) -> List[str]:
def schools_by_size_bigger(matches: List[str]) -> List[str]:
def schools_by_size_smaller(matches: List[str]) -> List[str]:
def schools_by_size_range(matches: List[str]) -> List[str]:
def location_by_school(matches: List[str]) -> List[str]:
def schools_by_location(matches: List[str]) -> List[str]:
def rate_by_school(matches: List[str]) -> List[str]:
def size_by_school(matches: List[str]) -> List[str]:


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
    (str.split("what is the acceptance rate of %"), rate_by_school),
    (str.split("what is the class size of %"), size_by_school),
    (str.split("what year was % founded"), year_by_school),
    
    


]

#School name
    #location
    #year founded
    # undergrad class size
    # acceptance rate