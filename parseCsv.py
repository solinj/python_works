import csv


#extract raw datas from a csv file
#operate some usual processes on them
#return two lists of numbers extracted from these treatments

class parseCsv(object):
   def __init__(self):
      inp = 0

   #extract row datas from each line of the file
   def extractRawDatas(self):
      lomed = []
      lomedet = []
      with open('your_file.csv') as the_file:
         file_reader = csv.reader(the_file, delimiter=';') #use csv module
         counter = 0
         for row in file_reader:
         #escaping the 1st line (title of the rows) doesn't matter here
            lomed.append(self.extractNumbers(row[10])[1])
            lomedet += self.extractNumbers(row[10])[0]
            counter += 1
         #check if the entire file was parsed
         #print(str(counter) + " lines parsed")
         return lomed, lomedet

   # extract numbers before and after "+" sign
   # return them by list and string types
   def extractNumbers(self, raw_datas):
       first_num = ""
       second_num = ""
       if raw_datas[len(raw_datas) - 3] == "+":
           first_num = raw_datas[-2:]
           interm = raw_datas[:-3]
           second_num = interm.split('-')
       elif raw_datas[len(raw_datas) - 2] == "+":
           first_num = raw_datas[-1:]
           interm = raw_datas[:-2]
           second_num = interm.split('-')
       return second_num, first_num

   #count numbers from list and string previously returned
   #return two sorted dicts by ascending order
   def countNumbers(self, first_treated):
      limon = first_treated[0] #chce
      tapouz = first_treated[1] #comb
      dictim = {}
      dicta = {}
      for l in range(len(limon)):
         dictim.update({limon[l] : limon.count(limon[l])})
      dic = {key : value for key, value in sorted(dictim.items(), key = lambda item : item[1])}
      for t in range(len(tapouz)):
          dicta.update({tapouz[t] : tapouz.count(tapouz[t])})
      doc = {key : value for key, value in sorted(dicta.items(), key = lambda item : item[1])}
      return dic, doc

   #transform the two sorted dicts into two descending order lists
   def renderNumbers(self, dic_tuples):
      li = []
      lo = []

      [li.append(key) for key, value in dic_tuples[0].items()]
      [lo.append(key) for key, value in dic_tuples[1].items()]

      li.reverse()
      lo.reverse()
      return li, lo





if __name__ == '__main__':
    pc = parseCsv()
    first_res = pc.renderNumbers(pc.countNumbers(pc.extractRawDatas()))[0]
    second_res = pc.renderNumbers(pc.countNumbers(pc.extractRawDatas()))[1]
    print(f'Result is {first_res} and {second_res}.')
