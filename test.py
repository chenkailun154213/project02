
from datetime import datetime

def from_file_get_data(file_name):
    f = None
    try:
        f = open(file_name,'r')
        line = f.readline()
        user_data = eval(line)
        return user_data
    except Exception as e:
        print(e)
    finally:
        if not f:
            f.close()








if __name__ == '__main__':

    result = from_file_get_data('user_data.txt')
    print(type(result))
    print(result)
    print(datetime.now())