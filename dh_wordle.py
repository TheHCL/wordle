import random,os,requests,json

url="https://random-words-api.vercel.app/word"
os.system("cls")


while 1:
	x=requests.get(url)
	x=json.loads(x.text)
	x=x[0]['word'].lower()

	let=len(x)
	count=1
	
	att=""
	tr=[]
	while len(att)!=let or att!=x:
		
		print("There are "+str(let)+" letters\n")
		print(str(count)+" attempts\n")


		att=input("")
		if len(att)==let:

			tr.append(att)
			count+=1
			m=""
			for i in range(len(att)):
				if att[i]==x[i]:
					m+="O"
				elif att[i] in x:
					m+="*"
				else:
					m+="X"
			tr.append(m)
			os.system("cls")
			for i in tr:
				print(i)
			
			#print(x)
			if att==x:
				print("The answer is "+x+"\n")
				break


