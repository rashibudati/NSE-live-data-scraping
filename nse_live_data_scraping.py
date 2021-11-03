import nsepy
import time

def get_required_columns(data_x):
    for i in data_x['data']:
        return [i.get('symbol'),i.get('open'),i.get('dayHigh'),i.get('dayLow'),i.get('lastPrice'),i.get('closePrice'),
                i.get('previousClose'),i.get('change'),i.get('pChange') + '%']


def doSomething():
    x = nsepy.live.get_quote('SBIN',series='EQ')
    y = get_required_columns(x)
    # print(y)
    time.sleep(10)
    yield y

if __name__ == '__main__':
    file_path = r'Book5.xlsx'
    file1 = open("nse_sbi.txt", "a")
    file1.write("'symbol','Open','High','Low','LTP','T Close','P Close','V change','P change'")
    while time.strftime("%H:%M:%S", time.localtime()) <= '15:30:00': ## as market closes at 15:30PM
        df = doSomething()
        for i in df:
            file1.write("\n")
            file1.write(','.join(map(str,i)))

