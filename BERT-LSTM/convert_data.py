path = './'
f_src_list = ['train.enzh.src', 'dev.enzh.src', 'test.enzh.src']
f_mt_list = ['train.enzh.mt', 'dev.enzh.mt', 'test.enzh.mt']
src = []
mt = []
for f_src, f_mt in zip(f_src_list,f_mt_list):
    fin_src = open(f_src,'r', encoding='utf8')
    fin_mt = open(f_mt,'r', encoding='utf8')
    fout = open(path+f_src+'.input','a', encoding='utf8')
    for i in fin_src:
        line_c = i.strip() + ' ||| ' + fin_mt.readline().strip() + '\n'
        fout.write(line_c)
    fin_src.close()
    fin_mt.close()
    fout.close()

