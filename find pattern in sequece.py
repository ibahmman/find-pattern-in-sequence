def lur (seq, pat, d):
    seq = seq.lower()
    pat = pat.lower()

    # لیست نهایی از پترن های یافت شده در جمله
    response = []
    for i in range(len(seq)):
        """
        حلقه به اندازه ی همه ی ایتم های جمله میچرخد
        """
        # شمارنده ی پترن
        pat_i = 0
        if seq[i] == pat[pat_i]:
            """
            اگر حرف یافت شده با حرف مورد نظر پترن برابر بود شرط زیر انجام میشود
            """
            # حرف ها در لیست زیر قرار میگیرند تا در آخر پردازش شوند
            temp = []
            # شمارنده ی کمکی ساخته میشود تا از حرف کنونی جمله تا زمانی ک حرف بعد را بیابد جملع پیمایش شود
            j = i
            # شمارنده ی کمکی برای d
            k = 0
            while k < d:
                """
                تا زمانی ک شمارنده کمکی از عدد محدود کننده کوچکتر باشد حلقه میچرخد
                حرف های جمله پیمایش میشوند و یکی یکی وارد لیست موقتی میشوند
                هر بار پیمایش به شمارنده های کمکی یک واحد افزایش میشود
                """
                temp.append(seq[j])
                j+=1
                k+=1
                if seq[j-1] == pat[pat_i + 1]:
                    """
                    اگر حرف کنونی برابر با حرف بعد پترن بود یعنی بخشی از راه را رفته ایم
                    پس دوباره بدنبال حرف بعد میگردیم
                    باید شمارنده کمکی صفر شود و شمارنده ی پترن یک واحد افزایش یابد
                    """
                    k = 0
                    pat_i = pat_i + 1 
                    break
            
            if temp[0] == pat[0] and temp[-1] == pat[-1]:
                """
                باید لیست موقتی را پردازش کنیم
                اگر اولین ایتم لیست با اولین ایتم پترن برابر بود
                و اخرین ایتم لیست هم با اخرین ایتم پترن برابر بود 
                یعنی کلمه ی درست یافت شده پس وارد لیست اصلی میشود
                اما پیش از ان شماره ی محل شروع را هم نیاز داریم یعنی i
                """
                # محل شروع کلمه
                start_index = i

                # کلمه ی ما در لیست است ما باید انرا به استرینک تبدیل کنیم متد جوین این کار را انجام میدهد
                txt = ''.join(temp)

                # یک تاپل میسازیم ک ایتم اول ان محل شروع و ایتم دوم ان کلمه ی ساخته شده باشد
                tup = (start_index, txt)

                # تاپل را به لیست اصلی اضافه میکنیم
                response.append(tup)

    return response

sequence = 'abcdopiutrasdasbaqsboabb'
pattern = 'ab'
d = 5
result = lur(sequence, pattern, d)

# sequence = input('enter sequence:')
# pattern = input('enter pattern:')
# d = int(input('enter d:'))

# request = lur(seq=sequence, pat=pattern, d=d)
# print(request)

file = open('result.txt', mode='w')
file = open('result.txt', mode='a')
for line in result:
    text = f'start in index: {line[0]} , {line[1]}\n'
    file.write(text)
file.close()