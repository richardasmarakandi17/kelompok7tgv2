sequence = [4,1,13,7,0,2,8,11,3]
graph = {}
max_count = 0
LIS = []

def add_values_in_graph(sample_dict, key, list_of_values):
   if key not in sample_dict:
      sample_dict[key] = list()
   sample_dict[key].extend(list_of_values)
   return sample_dict

def create_graph():
   global graph
   for element in sequence:
      graph[element] = []

   for key in graph:
      flag = False
      for key2 in graph:
         if flag and key < key2:
            add_values_in_graph(graph, key, [key2])
         if key == key2:
            flag = True

def telusur(key, count, subseq):
   global max_count
   global LIS
   #jika ditemukan nilai pada key
   for value in graph[key]:
      subseq.append(value)
      if count >= max_count:
         if count > max_count:
            LIS.clear()
         max_count = count
         LIS.append(subseq.copy())
      telusur(value, count+1, subseq)
      subseq.pop()

create_graph()
for key in graph:
   count = 1
   subseq = [key]
   telusur(key, count+1, subseq)
print("Graph = " + str(graph))
print("\nLIS ARE = "+str(LIS))
