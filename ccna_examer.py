

f = open('ccna-k.txt', 'r', encoding='utf-8')
strings = f.read()
f.close()

separator = ['QUESTION ', 'A.', 'Correct Answer: ']
qs = strings.split(separator[0])
filter = ['A. ', 'B. ', 'C. ', 'D. ', 'E. ', 'F. ', 'G. ']

questions = []
for q in qs[1:]:
  qq = q.split(separator[1], 1)
  tmp = ['%s%s'%(separator[0], qq[0])]##questions
  qqq = qq[-1].split(separator[2])
  chosens = []
  if qqq[0][0] != ' ':
    tp = [separator[1]]
    tp += qqq[0].split('\n')
    temp = []
    for i in tp:
      if i != '':
        temp.append(i)
    for i in range(len(temp)//2):
      ##chosens.append('%s %s'%(temp[i].replace(' ', ''), temp[len(temp)//2+i]))
      chosens.append('%s. %s'%(chr(65+i), temp[len(temp)//2+i]))

  else:
    xd = ''
    cont = '%s%s'%(separator[1], qqq[0])
    for i in filter:
      cont = cont.replace(i, 'ooxx'+i)
    chose = cont.split('ooxx')
    for c in chose:
      if c != '':
        chosens.append(c.replace('\n', ''))
  ##head = temp[:len(temp)//2]    
  ##tail = temp[len(temp)//2:]    
  tmp.append(chosens)##chosens
  tmp.append('%s%s'%(separator[2], qqq[-1]))##results
  ##ans = [i for i in qqq[-1].split()[0].split()[0]]
  ans = qqq[-1].split()[0]
  tmp.append(ans)##answers
  
  questions.append(tmp)

##format [questions, chosens, results, answers]  

print('\n\n\n')

for i in range(len(questions)):
  print(questions[i][0]) 
  for j in questions[i][1]:
    print(j) 
  uans = input('\nAnswers:')
  print('\n')
  print(questions[i][2])
  if ''.join(sorted(list(uans))).upper() == questions[i][-1]:
    print('correct!!!\n\n')
  else:
    print('wrong!!!\n\n')

  
  
