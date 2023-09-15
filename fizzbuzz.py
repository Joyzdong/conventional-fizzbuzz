def do_fizzbuzz(num:int):
    '''
    fizzbuzz 기능을 수행합니다.
    정해진 숫자에 대해, 
    3의 배수는 'fizz'
    5의 배수는 'buzz'
    15의 배수는 'fizzbuzz'
    나머지는 숫자 그대로를 출력합니다.
    '''
    
    for i in range(1, num+1):
        if i%3 == 0 or i%5 ==0:
            print('fizzbuzz' if i%15 == 0 else 'fizz' if i%3 == 0 else 'buzz')
        else:
            print(i)

if __name__ == '__main__':
    do_fizzbuzz(16)
