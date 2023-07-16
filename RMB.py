d = {'1' : u'壹', '2' : u'贰', '3' : u'叁', '4' : u'肆', '5' : u'伍',
     '6' : u'陆', '7' : u'柒', '8' : u'捌', '9' : u'玖', 'ten' : u'拾',
     'hundred' : u'佰', 'thousand' : u'仟', 'tenThousand' : u'万', '0' : u'零', 'yuan' : u'圆', '-' : u'负'}
a = int(input("请输入要转换的金额（正负一亿之间）："))
stringRMB = str(abs(a))
index = i = 0
ge = shi = bai = qian = wan = shiwan = baiwan = qianwan = fuhao = ''
L = [ge, shi, bai, qian, wan, shiwan, baiwan, qianwan]
fuhao = d['-'] if a < 0 else ''
if a >= 0:
    while index < 8:
        L[index] = d[stringRMB[len(stringRMB)-index-1]] if len(stringRMB) > index else ''
        index += 1
else:
    while index < 8:
        L[index] = d[stringRMB[len(stringRMB)-index-1]] if len(stringRMB) > index else ''
        index += 1
L.reverse()
if a >= 0:
    output = fuhao + L[0] + (u'仟' if L[0] != '' else '') + L[1] + (u'佰' if (L[1] != '' and L[1] != u'零') else '') + L[2] + (u'拾' if (L[2] != '' and L[2] != u'零') else '') + (L[3] if L[3] != u'零' else '') + (u'万' if L[3] != '' else '') + L[4] + (u'仟' if (L[4] != '' and L[4] != u'零') else '') + L[5] + (u'佰' if (L[5] != '' and L[5] != u'零') else '') + L[6] + (u'拾' if (L[6] != '' and L[6] != u'零') else '') + (L[7] if L[7] != u'零' else '') + u'圆'
    while i < len(output)-1:
        if output[i] == output[i+1] == u'零':
            List = list(output)
            List[i] = 'B'
            output = ''.join(List)
        i += 1
    output = output.replace('B', '')
    i = 0
    while i < len(output)-1:
        if (output[i] == u'零' and output[i+1] == u'万') or (output[i] == u'零' and output[i+1] == u'圆'):
            List = list(output)
            List[i] = 'B'
            output = ''.join(List)
        i += 1
    output = output.replace('B', '')
else:
    output = fuhao + L[0] + (u'仟' if L[0] != '' else '') + L[1] + (u'佰' if (L[1] != '' and L[1] != u'零') else '') + L[2] + (u'拾' if (L[2] != '' and L[2] != u'零') else '') + (L[3] if L[3] != u'零' else '') + (u'万' if L[3] != '' else '') + L[4] + (u'仟' if (L[4] != '' and L[4] != u'零') else '') + L[5] + (u'佰' if (L[5] != '' and L[5] != u'零') else '') + L[6] + (u'拾' if (L[6] != '' and L[6] != u'零') else '') + (L[7] if L[7] != u'零' else '') + u'圆'
    while i < len(output)-1:
        if output[i] == output[i+1] == u'零':
            List = list(output)
            List[i] = 'B'
            output = ''.join(List)
        i += 1
    output = output.replace('B', '')
    i = 0
    while i < len(output)-1:
        if output[i] == u'零' and (output[i+1] == u'万' or output[i+1] == u'圆'):
            List = list(output)
            List[i] = 'B'
            output = ''.join(List)
        i += 1
    output = output.replace('B', '')
print(output if a != 0 else u'零圆')