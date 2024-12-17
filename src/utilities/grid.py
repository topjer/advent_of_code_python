import re

def grid_parser(task_input: str, schema: dict[str, str]):
    """ Parser for 2d grids.

    It is assumed that the grid is provided as a single string with lines separated by '\n'

    Inputs
    ------
    task_input
        raw input string, lines separated by '\n'
    schema
        keys are name of the target variable, values are the search values to be used, only single
        character search values have been tested.

    Returns
    -------
        dictionary that contains the dimension of the grid as a tuple where the first number is the
        number or rows and the second the number of columns
        Additionally, it returns the coordinates of all matches for the search terms provided. If only
        one result is found, it is returned as a single point, else a set of points is returned.
    """
    dimension_col = task_input.find('\n')
    dimension_row = len(task_input.split())
    print(dimension_row, dimension_col)
    cleaned_input = task_input.replace('\n', '')
    result = dict()
    result['dimension'] = (dimension_row, dimension_col)
    for name, search_value in schema.items():
        temp = set(divmod(match.start(), dimension_row) for match in re.finditer(search_value, cleaned_input))
        if len(temp) == 1:
            result[name] = temp.pop()
        else:
            result[name] = temp

    return result
